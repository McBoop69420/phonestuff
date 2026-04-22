'use client';

import { useEffect, useState, useCallback } from 'react';
import type { Bet } from '@/lib/db';
import type { GameScore } from '@/app/api/score/route';

interface Props {
  bet: Bet;
  onDelete: (id: number) => void;
}

const SPORT_EMOJI: Record<string, string> = {
  NFL: '🏈',
  NCAAF: '🏈',
  NBA: '🏀',
  NCAAB: '🏀',
  MLB: '⚾',
  NHL: '🏒',
  Soccer: '⚽',
  MMA: '🥊',
  Boxing: '🥊',
  Other: '🎯',
};

function StatusBadge({ score }: { score: GameScore | null | 'loading' | 'error' }) {
  if (score === 'loading') {
    return <span className="text-xs text-gray-400 animate-pulse">Loading score...</span>;
  }
  if (score === 'error' || score === null) {
    return <span className="text-xs text-gray-500">Score unavailable</span>;
  }

  const { status, statusDetail, homeTeam, homeScore, awayTeam, awayScore } = score;

  const dotColor =
    status === 'in' ? 'bg-green-400 animate-pulse' : status === 'post' ? 'bg-gray-400' : 'bg-yellow-400';

  return (
    <div className="mt-3 rounded-lg bg-gray-800 p-3">
      <div className="flex items-center gap-2 mb-2">
        <span className={`inline-block w-2 h-2 rounded-full ${dotColor}`} />
        <span className="text-xs text-gray-400 uppercase tracking-wide">{statusDetail}</span>
      </div>
      <div className="flex justify-between items-center text-sm">
        <span className="text-white font-medium truncate max-w-[40%]">{awayTeam}</span>
        <span className="text-xl font-bold text-white tabular-nums">
          {awayScore ?? '–'} &nbsp;·&nbsp; {homeScore ?? '–'}
        </span>
        <span className="text-white font-medium truncate max-w-[40%] text-right">{homeTeam}</span>
      </div>
    </div>
  );
}

export default function BetCard({ bet, onDelete }: Props) {
  const [score, setScore] = useState<GameScore | null | 'loading' | 'error'>('loading');
  const [deleting, setDeleting] = useState(false);

  const fetchScore = useCallback(async () => {
    try {
      const params = new URLSearchParams({
        sport: bet.sport,
        home_team: bet.home_team,
        away_team: bet.away_team,
        game_date: bet.game_date,
      });
      const res = await fetch(`/api/score?${params}`);
      if (!res.ok) {
        setScore(null);
        return;
      }
      setScore(await res.json());
    } catch {
      setScore('error');
    }
  }, [bet.sport, bet.home_team, bet.away_team, bet.game_date]);

  useEffect(() => {
    fetchScore();
    // Refresh every 30 seconds for live games
    const interval = setInterval(fetchScore, 30_000);
    return () => clearInterval(interval);
  }, [fetchScore]);

  async function handleDelete() {
    setDeleting(true);
    await fetch('/api/bets', { method: 'DELETE', body: JSON.stringify({ id: bet.id }), headers: { 'Content-Type': 'application/json' } });
    onDelete(bet.id);
  }

  const emoji = SPORT_EMOJI[bet.sport] || '🎯';
  const gameDate = new Date(bet.game_date + 'T12:00:00').toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' });

  return (
    <div className="rounded-xl border border-gray-700 bg-gray-900 p-4 flex flex-col gap-1">
      <div className="flex items-start justify-between gap-2">
        <div className="flex items-center gap-2 min-w-0">
          <span className="text-xl">{emoji}</span>
          <div className="min-w-0">
            <p className="text-white font-semibold text-sm leading-tight truncate">
              {bet.away_team} @ {bet.home_team}
            </p>
            <p className="text-gray-400 text-xs">{bet.sport} · {gameDate}</p>
          </div>
        </div>
        <button
          onClick={handleDelete}
          disabled={deleting}
          className="text-gray-600 hover:text-red-400 transition-colors text-lg leading-none flex-shrink-0"
          aria-label="Delete bet"
        >
          ×
        </button>
      </div>

      <div className="mt-2 flex flex-wrap gap-2 items-center">
        <span className="rounded-full bg-blue-900 text-blue-300 text-xs px-2 py-0.5">{bet.bet_type}</span>
        <span className="text-gray-300 text-sm">{bet.bet_description}</span>
        {bet.odds && <span className="text-yellow-400 text-sm font-mono">{bet.odds}</span>}
      </div>

      {(bet.stake || bet.potential_payout) && (
        <div className="flex gap-4 text-xs text-gray-400 mt-1">
          {bet.stake && <span>Stake: <span className="text-white">${bet.stake.toFixed(2)}</span></span>}
          {bet.potential_payout && <span>To win: <span className="text-green-400">${bet.potential_payout.toFixed(2)}</span></span>}
        </div>
      )}

      <StatusBadge score={score} />
    </div>
  );
}
