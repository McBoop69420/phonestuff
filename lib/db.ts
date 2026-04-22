import Database from 'better-sqlite3';
import path from 'path';
import fs from 'fs';

const DB_DIR = path.join(process.cwd(), 'data');
const DB_PATH = path.join(DB_DIR, 'bets.db');

if (!fs.existsSync(DB_DIR)) {
  fs.mkdirSync(DB_DIR, { recursive: true });
}

const db = new Database(DB_PATH);

db.exec(`
  CREATE TABLE IF NOT EXISTS bets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sport TEXT NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    game_date TEXT NOT NULL,
    bet_type TEXT NOT NULL,
    bet_description TEXT NOT NULL,
    odds TEXT,
    stake REAL,
    potential_payout REAL,
    espn_game_id TEXT,
    status TEXT DEFAULT 'upcoming',
    created_at TEXT DEFAULT (datetime('now'))
  )
`);

export interface Bet {
  id: number;
  sport: string;
  home_team: string;
  away_team: string;
  game_date: string;
  bet_type: string;
  bet_description: string;
  odds: string | null;
  stake: number | null;
  potential_payout: number | null;
  espn_game_id: string | null;
  status: string;
  created_at: string;
}

export interface NewBet {
  sport: string;
  home_team: string;
  away_team: string;
  game_date: string;
  bet_type: string;
  bet_description: string;
  odds?: string;
  stake?: number;
  potential_payout?: number;
  espn_game_id?: string;
}

export function insertBet(bet: NewBet): Bet {
  const stmt = db.prepare(`
    INSERT INTO bets (sport, home_team, away_team, game_date, bet_type, bet_description, odds, stake, potential_payout, espn_game_id)
    VALUES (@sport, @home_team, @away_team, @game_date, @bet_type, @bet_description, @odds, @stake, @potential_payout, @espn_game_id)
  `);
  const result = stmt.run(bet);
  return getBetById(result.lastInsertRowid as number)!;
}

export function getBetById(id: number): Bet | undefined {
  return db.prepare('SELECT * FROM bets WHERE id = ?').get(id) as Bet | undefined;
}

export function getAllBets(): Bet[] {
  return db.prepare('SELECT * FROM bets ORDER BY created_at DESC').all() as Bet[];
}

export function deleteBet(id: number): void {
  db.prepare('DELETE FROM bets WHERE id = ?').run(id);
}

export function updateBetGameId(id: number, espn_game_id: string): void {
  db.prepare('UPDATE bets SET espn_game_id = ? WHERE id = ?').run(espn_game_id, id);
}
