import Foundation

struct GameScore {
    let status: GameStatus
    let statusDetail: String
    let homeTeam: String
    let homeScore: String?
    let awayTeam: String
    let awayScore: String?
}

enum GameStatus {
    case pre, live, final
}

actor ESPNService {
    static let shared = ESPNService()

    private let sportMap: [String: (sport: String, league: String)] = [
        "NFL":   ("football",   "nfl"),
        "NCAAF": ("football",   "college-football"),
        "NBA":   ("basketball", "nba"),
        "NCAAB": ("basketball", "mens-college-basketball"),
        "MLB":   ("baseball",   "mlb"),
        "NHL":   ("hockey",     "nhl"),
        "Soccer":("soccer",     "eng.1"),
        "MMA":   ("mma",        "ufc"),
    ]

    func fetchScore(sport: String, homeTeam: String, awayTeam: String, gameDate: Date) async -> GameScore? {
        guard let mapping = sportMap[sport] else { return nil }

        let fmt = DateFormatter()
        fmt.dateFormat = "yyyyMMdd"
        let dates = Array(Set([fmt.string(from: gameDate), fmt.string(from: Date())]))

        for date in dates {
            let urlStr = "https://site.api.espn.com/apis/site/v2/sports/\(mapping.sport)/\(mapping.league)/scoreboard?dates=\(date)"
            guard
                let url = URL(string: urlStr),
                let (data, _) = try? await URLSession.shared.data(from: url),
                let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
                let events = json["events"] as? [[String: Any]]
            else { continue }

            for event in events {
                guard
                    let competitions = event["competitions"] as? [[String: Any]],
                    let comp = competitions.first,
                    let competitors = comp["competitors"] as? [[String: Any]],
                    competitors.count >= 2
                else { continue }

                let home = competitors.first { $0["homeAway"] as? String == "home" }
                let away = competitors.first { $0["homeAway"] as? String == "away" }

                guard
                    let home, let away,
                    let homeName = (home["team"] as? [String: Any])?["displayName"] as? String,
                    let awayName = (away["team"] as? [String: Any])?["displayName"] as? String,
                    (matches(homeName, homeTeam) || matches(homeName, awayTeam)),
                    (matches(awayName, awayTeam) || matches(awayName, homeTeam))
                else { continue }

                let statusType = (comp["status"] as? [String: Any])?["type"] as? [String: Any]
                let state = statusType?["state"] as? String ?? "pre"
                let detail = statusType?["shortDetail"] as? String ?? statusType?["description"] as? String ?? ""

                return GameScore(
                    status: state == "in" ? .live : state == "post" ? .final : .pre,
                    statusDetail: detail,
                    homeTeam: homeName,
                    homeScore: home["score"] as? String,
                    awayTeam: awayName,
                    awayScore: away["score"] as? String
                )
            }
        }
        return nil
    }

    private func matches(_ a: String, _ b: String) -> Bool {
        let clean: (String) -> String = { $0.lowercased().filter { $0.isLetter || $0.isNumber } }
        let ca = clean(a), cb = clean(b)
        return ca.contains(cb) || cb.contains(ca)
    }
}
