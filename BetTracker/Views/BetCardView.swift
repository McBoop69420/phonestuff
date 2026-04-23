import SwiftUI

struct BetCardView: View {
    let bet: Bet
    let onDelete: () -> Void

    @State private var score: GameScore?
    @State private var scoreState: ScoreState = .loading

    enum ScoreState { case loading, loaded, unavailable }

    private let timer = Timer.publish(every: 30, on: .main, in: .common).autoconnect()

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            // Header
            HStack(alignment: .top) {
                VStack(alignment: .leading, spacing: 2) {
                    HStack(spacing: 6) {
                        Text(sportEmoji).font(.title3)
                        Text("\(bet.awayTeam) @ \(bet.homeTeam)")
                            .font(.subheadline).fontWeight(.semibold).foregroundStyle(.white)
                            .lineLimit(1)
                    }
                    Text("\(bet.sport) · \(bet.gameDate.formatted(date: .abbreviated, time: .omitted))")
                        .font(.caption).foregroundStyle(.gray)
                }
                Spacer()
                Button(action: onDelete) {
                    Image(systemName: "xmark")
                        .font(.caption).foregroundStyle(.gray)
                        .padding(6)
                        .background(Color.white.opacity(0.08))
                        .clipShape(Circle())
                }
            }

            // Bet details
            HStack(spacing: 8) {
                Text(bet.betType)
                    .font(.caption2).foregroundStyle(.blue)
                    .padding(.horizontal, 8).padding(.vertical, 3)
                    .background(Color.blue.opacity(0.15)).clipShape(Capsule())
                Text(bet.betDescription)
                    .font(.subheadline).foregroundStyle(Color(white: 0.85))
                if let odds = bet.odds {
                    Text(odds)
                        .font(.subheadline).fontWeight(.medium).foregroundStyle(.yellow)
                        .fontDesign(.monospaced)
                }
            }

            // Stake / payout
            if bet.stake != nil || bet.potentialPayout != nil {
                HStack(spacing: 16) {
                    if let stake = bet.stake {
                        Text(String(format: "Stake: $%.2f", stake))
                            .font(.caption).foregroundStyle(.gray)
                    }
                    if let payout = bet.potentialPayout {
                        Text(String(format: "To win: $%.2f", payout))
                            .font(.caption).foregroundStyle(.green)
                    }
                }
            }

            scoreView
        }
        .padding()
        .background(Color(white: 0.1))
        .clipShape(RoundedRectangle(cornerRadius: 16))
        .task { await loadScore() }
        .onReceive(timer) { _ in Task { await loadScore() } }
    }

    @ViewBuilder
    private var scoreView: some View {
        switch scoreState {
        case .loading:
            HStack(spacing: 6) {
                ProgressView().scaleEffect(0.7)
                Text("Loading score…").font(.caption).foregroundStyle(.gray)
            }
        case .unavailable:
            Text("Score unavailable").font(.caption).foregroundStyle(Color(white: 0.4))
        case .loaded:
            if let score { scoreboard(score) }
        }
    }

    private func scoreboard(_ score: GameScore) -> some View {
        VStack(spacing: 6) {
            HStack(spacing: 6) {
                Circle()
                    .fill(dotColor(score.status))
                    .frame(width: 7, height: 7)
                Text(score.statusDetail)
                    .font(.caption2).foregroundStyle(.gray).textCase(.uppercase).tracking(0.5)
            }
            .frame(maxWidth: .infinity, alignment: .leading)

            HStack {
                Text(score.awayTeam)
                    .font(.subheadline).fontWeight(.medium).foregroundStyle(.white)
                    .lineLimit(1).frame(maxWidth: .infinity, alignment: .leading)
                Text("\(score.awayScore ?? "–")  ·  \(score.homeScore ?? "–")")
                    .font(.title3).fontWeight(.bold).foregroundStyle(.white).fontDesign(.monospaced)
                Text(score.homeTeam)
                    .font(.subheadline).fontWeight(.medium).foregroundStyle(.white)
                    .lineLimit(1).frame(maxWidth: .infinity, alignment: .trailing)
            }
        }
        .padding(10)
        .background(Color.white.opacity(0.05))
        .clipShape(RoundedRectangle(cornerRadius: 10))
    }

    private func dotColor(_ status: GameStatus) -> Color {
        switch status {
        case .pre: .yellow
        case .live: .green
        case .final: Color(white: 0.5)
        }
    }

    private var sportEmoji: String {
        switch bet.sport {
        case "NFL", "NCAAF": "🏈"
        case "NBA", "NCAAB": "🏀"
        case "MLB": "⚾"
        case "NHL": "🏒"
        case "Soccer": "⚽"
        case "MMA", "Boxing": "🥊"
        default: "🎯"
        }
    }

    private func loadScore() async {
        let result = await ESPNService.shared.fetchScore(
            sport: bet.sport, homeTeam: bet.homeTeam, awayTeam: bet.awayTeam, gameDate: bet.gameDate
        )
        await MainActor.run {
            if let result { score = result; scoreState = .loaded }
            else { scoreState = .unavailable }
        }
    }
}
