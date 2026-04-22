import { NextRequest, NextResponse } from 'next/server';

const ESPN_SPORT_MAP: Record<string, { sport: string; league: string }> = {
  NFL: { sport: 'football', league: 'nfl' },
  NCAAF: { sport: 'football', league: 'college-football' },
  NBA: { sport: 'basketball', league: 'nba' },
  NCAAB: { sport: 'basketball', league: 'mens-college-basketball' },
  MLB: { sport: 'baseball', league: 'mlb' },
  NHL: { sport: 'hockey', league: 'nhl' },
  Soccer: { sport: 'soccer', league: 'eng.1' },
  MMA: { sport: 'mma', league: 'ufc' },
};

export interface GameScore {
  id: string;
  status: 'pre' | 'in' | 'post';
  statusDetail: string;
  clock: string | null;
  period: string | null;
  homeTeam: string;
  homeScore: string | null;
  awayTeam: string;
  awayScore: string | null;
  completed: boolean;
}

function normalize(name: string): string {
  return name.toLowerCase().replace(/[^a-z0-9]/g, '');
}

function teamsMatch(espnName: string, betName: string): boolean {
  const a = normalize(espnName);
  const b = normalize(betName);
  return a.includes(b) || b.includes(a) || a === b;
}

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const sport = searchParams.get('sport') || 'NFL';
  const homeTeam = searchParams.get('home_team') || '';
  const awayTeam = searchParams.get('away_team') || '';
  const gameDate = searchParams.get('game_date') || '';

  const mapping = ESPN_SPORT_MAP[sport];
  if (!mapping) {
    return NextResponse.json({ error: 'Sport not supported' }, { status: 400 });
  }

  // Build ESPN scoreboard URL — try the game date first, fallback to today
  const dates = [gameDate.replace(/-/g, ''), new Date().toISOString().slice(0, 10).replace(/-/g, '')];
  const uniqueDates = [...new Set(dates)];

  for (const date of uniqueDates) {
    const url = `https://site.api.espn.com/apis/site/v2/sports/${mapping.sport}/${mapping.league}/scoreboard?dates=${date}`;
    let data: Record<string, unknown>;
    try {
      const res = await fetch(url, { next: { revalidate: 30 } });
      data = await res.json();
    } catch {
      continue;
    }

    const events = (data.events as unknown[]) || [];
    for (const event of events) {
      const e = event as Record<string, unknown>;
      const competitions = (e.competitions as unknown[]) || [];
      for (const comp of competitions) {
        const c = comp as Record<string, unknown>;
        const competitors = (c.competitors as unknown[]) || [];
        if (competitors.length < 2) continue;

        const home = competitors.find((x) => (x as Record<string, unknown>).homeAway === 'home') as Record<string, unknown> | undefined;
        const away = competitors.find((x) => (x as Record<string, unknown>).homeAway === 'away') as Record<string, unknown> | undefined;
        if (!home || !away) continue;

        const homeName = String((home.team as Record<string, unknown>)?.displayName || '');
        const awayName = String((away.team as Record<string, unknown>)?.displayName || '');

        const homeMatch = teamsMatch(homeName, homeTeam) || teamsMatch(homeName, awayTeam);
        const awayMatch = teamsMatch(awayName, awayTeam) || teamsMatch(awayName, homeTeam);

        if (!homeMatch || !awayMatch) continue;

        const status = c.status as Record<string, unknown>;
        const statusType = status?.type as Record<string, unknown>;
        const stateVal = String(statusType?.state || 'pre') as 'pre' | 'in' | 'post';

        const score: GameScore = {
          id: String(e.id || ''),
          status: stateVal,
          statusDetail: String(statusType?.shortDetail || statusType?.description || ''),
          clock: status?.displayClock ? String(status.displayClock) : null,
          period: status?.period ? String(status.period) : null,
          homeTeam: homeName,
          homeScore: home.score != null ? String(home.score) : null,
          awayTeam: awayName,
          awayScore: away.score != null ? String(away.score) : null,
          completed: Boolean(statusType?.completed),
        };

        return NextResponse.json(score);
      }
    }
  }

  return NextResponse.json({ error: 'Game not found' }, { status: 404 });
}
