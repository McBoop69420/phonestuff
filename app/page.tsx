'use client';

import { useState, useEffect } from 'react';
import type { Bet } from '@/lib/db';
import BetCard from '@/components/BetCard';
import UploadForm from '@/components/UploadForm';

export default function Home() {
  const [bets, setBets] = useState<Bet[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/bets')
      .then((r) => r.json())
      .then((data) => {
        setBets(data);
        setLoading(false);
      });
  }, []);

  function handleBetAdded(bet: Bet) {
    setBets((prev) => [bet, ...prev]);
  }

  function handleBetDeleted(id: number) {
    setBets((prev) => prev.filter((b) => b.id !== id));
  }

  const cutoff = new Date(Date.now() - 86400_000);
  const active = bets.filter((b) => new Date(b.game_date + 'T23:59:59') >= cutoff);
  const past = bets.filter((b) => new Date(b.game_date + 'T23:59:59') < cutoff);

  return (
    <div className="min-h-screen bg-gray-950 text-white">
      <div className="max-w-md mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-2xl font-bold tracking-tight">Bet Tracker</h1>
          <p className="text-gray-400 text-sm mt-1">Upload a bet slip to track your game live</p>
        </div>

        <UploadForm onBetAdded={handleBetAdded} />

        <div className="mt-8">
          {loading ? (
            <div className="text-center text-gray-500 py-12">Loading bets...</div>
          ) : bets.length === 0 ? (
            <div className="text-center text-gray-600 py-12">
              <p className="text-4xl mb-3">🎯</p>
              <p className="text-sm">No bets yet. Upload your first slip above.</p>
            </div>
          ) : (
            <>
              {active.length > 0 && (
                <section className="mb-6">
                  <h2 className="text-xs uppercase tracking-widest text-gray-500 mb-3">Active / Upcoming</h2>
                  <div className="flex flex-col gap-3">
                    {active.map((bet) => (
                      <BetCard key={bet.id} bet={bet} onDelete={handleBetDeleted} />
                    ))}
                  </div>
                </section>
              )}
              {past.length > 0 && (
                <section>
                  <h2 className="text-xs uppercase tracking-widest text-gray-500 mb-3">Past</h2>
                  <div className="flex flex-col gap-3 opacity-70">
                    {past.map((bet) => (
                      <BetCard key={bet.id} bet={bet} onDelete={handleBetDeleted} />
                    ))}
                  </div>
                </section>
              )}
            </>
          )}
        </div>
      </div>
    </div>
  );
}
