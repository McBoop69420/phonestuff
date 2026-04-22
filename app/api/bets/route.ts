import { NextRequest, NextResponse } from 'next/server';
import Anthropic from '@anthropic-ai/sdk';
import { getAllBets, insertBet, deleteBet } from '@/lib/db';

const client = new Anthropic();

export async function GET() {
  const bets = getAllBets();
  return NextResponse.json(bets);
}

export async function POST(req: NextRequest) {
  const formData = await req.formData();
  const file = formData.get('image') as File;
  if (!file) {
    return NextResponse.json({ error: 'No image provided' }, { status: 400 });
  }

  const bytes = await file.arrayBuffer();
  const base64 = Buffer.from(bytes).toString('base64');
  const mediaType = (file.type || 'image/jpeg') as 'image/jpeg' | 'image/png' | 'image/gif' | 'image/webp';

  const response = await client.messages.create({
    model: 'claude-sonnet-4-6',
    max_tokens: 1024,
    messages: [
      {
        role: 'user',
        content: [
          {
            type: 'image',
            source: { type: 'base64', media_type: mediaType, data: base64 },
          },
          {
            type: 'text',
            text: `Extract the bet details from this sportsbook screenshot. Return ONLY valid JSON with these fields:
{
  "sport": "NFL" | "NBA" | "MLB" | "NHL" | "NCAAF" | "NCAAB" | "Soccer" | "MMA" | "Boxing" | "Other",
  "home_team": "full team name",
  "away_team": "full team name",
  "game_date": "YYYY-MM-DD",
  "bet_type": "Moneyline" | "Spread" | "Over/Under" | "Parlay" | "Prop" | "Futures" | "Other",
  "bet_description": "human-readable description of the bet, e.g. 'Lakers -4.5' or 'Over 220.5 points'",
  "odds": "+150" or "-110" etc (as string, null if not visible),
  "stake": 25.00 (number, null if not visible),
  "potential_payout": 75.00 (number, null if not visible)
}
If you cannot determine home vs away, put the favored or first-listed team as home_team.
If the game date is not shown but a time is, use today's date (${new Date().toISOString().split('T')[0]}).`,
          },
        ],
      },
    ],
  });

  const text = response.content[0].type === 'text' ? response.content[0].text : '';
  const jsonMatch = text.match(/\{[\s\S]*\}/);
  if (!jsonMatch) {
    return NextResponse.json({ error: 'Could not parse bet from image' }, { status: 422 });
  }

  let parsed: Record<string, unknown>;
  try {
    parsed = JSON.parse(jsonMatch[0]);
  } catch {
    return NextResponse.json({ error: 'Invalid JSON from vision model' }, { status: 422 });
  }

  const bet = insertBet({
    sport: String(parsed.sport || 'Other'),
    home_team: String(parsed.home_team || ''),
    away_team: String(parsed.away_team || ''),
    game_date: String(parsed.game_date || new Date().toISOString().split('T')[0]),
    bet_type: String(parsed.bet_type || 'Other'),
    bet_description: String(parsed.bet_description || ''),
    odds: parsed.odds ? String(parsed.odds) : undefined,
    stake: typeof parsed.stake === 'number' ? parsed.stake : undefined,
    potential_payout: typeof parsed.potential_payout === 'number' ? parsed.potential_payout : undefined,
  });

  return NextResponse.json(bet, { status: 201 });
}

export async function DELETE(req: NextRequest) {
  const { id } = await req.json();
  if (!id) return NextResponse.json({ error: 'No id' }, { status: 400 });
  deleteBet(Number(id));
  return NextResponse.json({ ok: true });
}
