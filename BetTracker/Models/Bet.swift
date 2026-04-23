import SwiftData
import Foundation

@Model
final class Bet {
    var id: UUID
    var sport: String
    var homeTeam: String
    var awayTeam: String
    var gameDate: Date
    var betType: String
    var betDescription: String
    var odds: String?
    var stake: Double?
    var potentialPayout: Double?
    var createdAt: Date

    init(
        sport: String,
        homeTeam: String,
        awayTeam: String,
        gameDate: Date,
        betType: String,
        betDescription: String,
        odds: String? = nil,
        stake: Double? = nil,
        potentialPayout: Double? = nil
    ) {
        self.id = UUID()
        self.sport = sport
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.gameDate = gameDate
        self.betType = betType
        self.betDescription = betDescription
        self.odds = odds
        self.stake = stake
        self.potentialPayout = potentialPayout
        self.createdAt = Date()
    }
}
