import SwiftUI
import PhotosUI

struct AddBetView: View {
    let onAdd: (Bet) -> Void

    @Environment(\.dismiss) private var dismiss
    @State private var selectedItem: PhotosPickerItem?
    @State private var state: ViewState = .idle
    @State private var errorMessage: String?

    enum ViewState { case idle, processing, error }

    var body: some View {
        NavigationStack {
            ZStack {
                Color.black.ignoresSafeArea()

                VStack(spacing: 24) {
                    Spacer()

                    Image(systemName: "photo.badge.plus")
                        .font(.system(size: 64)).foregroundStyle(.blue)

                    VStack(spacing: 8) {
                        Text("Upload Bet Slip")
                            .font(.title2).fontWeight(.semibold).foregroundStyle(.white)
                        Text("Choose a photo from your library")
                            .font(.subheadline).foregroundStyle(.gray).multilineTextAlignment(.center)
                    }

                    if state == .processing {
                        VStack(spacing: 12) {
                            ProgressView().tint(.blue)
                            Text("Reading your bet slip…")
                                .font(.subheadline).foregroundStyle(.gray)
                        }
                        .padding()
                    }

                    if let msg = errorMessage {
                        Text(msg)
                            .font(.subheadline).foregroundStyle(.red)
                            .multilineTextAlignment(.center).padding(.horizontal)
                    }

                    Spacer()

                    if state != .processing {
                        PhotosPicker(selection: $selectedItem, matching: .images) {
                            Label("Choose Photo", systemImage: "photo.on.rectangle")
                                .font(.headline)
                                .frame(maxWidth: .infinity).padding()
                                .background(Color.blue).foregroundStyle(.white)
                                .clipShape(RoundedRectangle(cornerRadius: 14))
                        }
                        .padding(.horizontal).padding(.bottom)
                    }
                }
                .padding()
            }
            .navigationTitle("Add Bet")
            .navigationBarTitleDisplayMode(.inline)
            .toolbarBackground(Color.black, for: .navigationBar)
            .toolbarColorScheme(.dark, for: .navigationBar)
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button("Cancel") { dismiss() }.foregroundStyle(.gray)
                }
            }
            .onChange(of: selectedItem) { _, item in
                guard let item else { return }
                Task { await processImage(item) }
            }
        }
        .preferredColorScheme(.dark)
    }

    private func processImage(_ item: PhotosPickerItem) async {
        state = .processing
        errorMessage = nil

        guard
            let data = try? await item.loadTransferable(type: Data.self),
            let image = UIImage(data: data)
        else {
            await MainActor.run { state = .error; errorMessage = "Could not load image." }
            return
        }

        let apiKey = UserDefaults.standard.string(forKey: "anthropic_api_key") ?? ""
        guard !apiKey.isEmpty else {
            await MainActor.run { state = .error; errorMessage = "Add your Anthropic API key in Settings first." }
            return
        }

        do {
            let parsed = try await ClaudeService(apiKey: apiKey).parseBetSlip(image)
            let fmt = DateFormatter()
            fmt.dateFormat = "yyyy-MM-dd"
            let gameDate = fmt.date(from: parsed.gameDate) ?? Date()

            let bet = Bet(
                sport: parsed.sport,
                homeTeam: parsed.homeTeam,
                awayTeam: parsed.awayTeam,
                gameDate: gameDate,
                betType: parsed.betType,
                betDescription: parsed.betDescription,
                odds: parsed.odds,
                stake: parsed.stake,
                potentialPayout: parsed.potentialPayout
            )
            await MainActor.run { onAdd(bet); dismiss() }
        } catch {
            await MainActor.run { state = .error; errorMessage = error.localizedDescription }
        }
    }
}
