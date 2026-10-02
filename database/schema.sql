PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL COLLATE NOCASE UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS mood_entries (
    id TEXT PRIMARY KEY,
    user_id INTEGER NOT NULL,
    entry_date TEXT NOT NULL,
    mood TEXT NOT NULL,
    note TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL,
    CONSTRAINT fk_mood_entries_user
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    CONSTRAINT uq_mood_entries_user_date UNIQUE (user_id, entry_date),
    CONSTRAINT ck_mood_entries_date
        CHECK (entry_date GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
    CONSTRAINT ck_mood_entries_mood
        CHECK (mood IN ('very_happy', 'happy', 'neutral', 'sad', 'very_sad')),
    CONSTRAINT ck_mood_entries_note_length CHECK (length(note) <= 200)
);

CREATE INDEX IF NOT EXISTS ix_mood_entries_user_created
    ON mood_entries (user_id, created_at DESC);
