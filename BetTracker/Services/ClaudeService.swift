import Foundation
import UIKit

struct ParsedBet: Decodable {
    let sport: String
    let homeTeam: String
    let awayTeam: String
    let gameDate: String
    let betType: String
    let betDescription: String
    let odds: String?
    let stake: Double?
    let potentialPayout: Double?

    enum CodingKeys: String, CodingKey {
        case sport
        case homeTeam = "home_team"
        case awayTeam = "away_team"
        case gameDate = "game_date"
        case betType = "bet_type"
        case betDescription = "bet_description"
        case odds, stake
        case potentialPayout = "potential_payout"
    }
}

enum ClaudeError: LocalizedError {
    case imageConversionFailed, apiError(Int), parseError, missingAPIKey

    var errorDescription: String? {
        switch self {
        case .imageConversionFailed: "Could not process image."
        case .apiError(let code): "API request failed (HTTP \(code))."
        case .parseError: "Could not read bet details from image."
        case .missingAPIKey: "Add your Anthropic API key in Settings first."
        }
    }
}

actor ClaudeService {
    private let apiKey: String
    private let endpoint = URL(string: "https://api.anthropic.com/v1/messages")!

    init(apiKey: String) {
        self.apiKey = apiKey
    }

    func parseBetSlip(_ image: UIImage) async throws -> ParsedBet {
        guard let data = image.jpegData(compressionQuality: 0.8) else {
            throw ClaudeError.imageConversionFailed
        }
        let base64 = data.base64EncodedString()
        let today = ISO8601DateFormatter().string(from: Date()).prefix(10)

        let body: [String: Any] = [
            "model": "claude-sonnet-4-6",
            "max_tokens": 1024,
            "messages": [[
                "role": "user",
                "content": [
                    [
                        "type": "image",
                        "source": ["type": "base64", "media_type": "image/jpeg", "data": base64]
                    ],
                    [
                        "type": "text",
                        "text": """
                        Extract the bet details from this sportsbook screenshot. Return ONLY valid JSON:
                        {
                          "sport": "NFL"|"NBA"|"MLB"|"NHL"|"NCAAF"|"NCAAB"|"Soccer"|"MMA"|"Boxing"|"Other",
                          "home_team": "full team name",
                          "away_team": "full team name",
                          "game_date": "YYYY-MM-DD",
                          "bet_type": "Moneyline"|"Spread"|"Over/Under"|"Parlay"|"Prop"|"Futures"|"Other",
                          "bet_description": "e.g. Lakers -4.5 or Over 220.5",
                          "odds": "+150" or null,
                          "stake": 25.00 or null,
                          "potential_payout": 75.00 or null
                        }
                        If date not visible use today: \(today)
                        """
                    ]
                ]
            ]]
        ]

        var req = URLRequest(url: endpoint)
        req.httpMethod = "POST"
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        req.setValue(apiKey, forHTTPHeaderField: "x-api-key")
        req.setValue("2023-06-01", forHTTPHeaderField: "anthropic-version")
        req.httpBody = try JSONSerialization.data(withJSONObject: body)

        let (responseData, response) = try await URLSession.shared.data(for: req)
        let statusCode = (response as? HTTPURLResponse)?.statusCode ?? 0
        guard statusCode == 200 else { throw ClaudeError.apiError(statusCode) }

        guard
            let json = try? JSONSerialization.jsonObject(with: responseData) as? [String: Any],
            let content = (json["content"] as? [[String: Any]])?.first,
            let text = content["text"] as? String,
            let range = text.range(of: #"\{[\s\S]*\}"#, options: .regularExpression),
            let jsonData = String(text[range]).data(using: .utf8)
        else { throw ClaudeError.parseError }

        return try JSONDecoder().decode(ParsedBet.self, from: jsonData)
    }
}
