import SwiftUI
import SwiftData

@main
struct BetTrackerApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Bet.self)
    }
}
