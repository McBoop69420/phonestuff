import SwiftUI
import SwiftData

struct ContentView: View {
    @Environment(\.modelContext) private var modelContext
    @Query(sort: \Bet.createdAt, order: .reverse) private var bets: [Bet]
    @State private var showingAddBet = false
    @State private var showingSettings = false

    private var activeBets: [Bet] {
        let cutoff = Calendar.current.date(byAdding: .day, value: -1, to: Date()) ?? Date()
        return bets.filter { $0.gameDate >= cutoff }
    }

    private var pastBets: [Bet] {
        let cutoff = Calendar.current.date(byAdding: .day, value: -1, to: Date()) ?? Date()
        return bets.filter { $0.gameDate < cutoff }
    }

    var body: some View {
        NavigationStack {
            ZStack {
                Color.black.ignoresSafeArea()

                if bets.isEmpty {
                    emptyState
                } else {
                    betList
                }
            }
            .navigationTitle("Bet Tracker")
            .navigationBarTitleDisplayMode(.large)
            .toolbarBackground(Color.black, for: .navigationBar)
            .toolbarColorScheme(.dark, for: .navigationBar)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button { showingSettings = true } label: {
                        Image(systemName: "gear").foregroundStyle(.gray)
                    }
                }
                ToolbarItem(placement: .bottomBar) {
                    Button { showingAddBet = true } label: {
                        Label("Add Bet", systemImage: "plus.circle.fill")
                            .font(.headline)
                    }
                    .buttonStyle(.borderedProminent)
                    .tint(.blue)
                }
            }
            .sheet(isPresented: $showingAddBet) {
                AddBetView { bet in modelContext.insert(bet) }
            }
            .sheet(isPresented: $showingSettings) {
                SettingsView()
            }
        }
        .preferredColorScheme(.dark)
    }

    private var emptyState: some View {
        VStack(spacing: 12) {
            Text("🎯").font(.system(size: 60))
            Text("No bets yet")
                .font(.title3).foregroundStyle(.white)
            Text("Tap the button below to upload your first bet slip")
                .font(.subheadline).foregroundStyle(.gray)
                .multilineTextAlignment(.center).padding(.horizontal, 40)
        }
    }

    private var betList: some View {
        ScrollView {
            LazyVStack(spacing: 12, pinnedViews: .sectionHeaders) {
                if !activeBets.isEmpty {
                    Section {
                        ForEach(activeBets) { bet in
                            BetCardView(bet: bet) { modelContext.delete(bet) }
                        }
                    } header: { sectionHeader("Active / Upcoming") }
                }
                if !pastBets.isEmpty {
                    Section {
                        ForEach(pastBets) { bet in
                            BetCardView(bet: bet) { modelContext.delete(bet) }.opacity(0.7)
                        }
                    } header: { sectionHeader("Past") }
                }
            }
            .padding()
        }
    }

    private func sectionHeader(_ title: String) -> some View {
        HStack {
            Text(title)
                .font(.caption).fontWeight(.semibold).foregroundStyle(.gray)
                .textCase(.uppercase).tracking(1.5)
            Spacer()
        }
        .padding(.horizontal).padding(.vertical, 4)
        .background(Color.black)
    }
}
