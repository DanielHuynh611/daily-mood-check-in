CREATE TABLE IF NOT EXISTS users (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(254) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at DATETIME(6) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uq_users_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS mood_entries (
    id CHAR(36) NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    entry_date DATE NOT NULL,
    mood VARCHAR(20) NOT NULL,
    note VARCHAR(200) NOT NULL DEFAULT '',
    created_at DATETIME(6) NOT NULL,
    PRIMARY KEY (id),
    KEY ix_mood_entries_user_created (user_id, created_at DESC),
    CONSTRAINT fk_mood_entries_user
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    CONSTRAINT uq_mood_entries_user_date UNIQUE (user_id, entry_date),
    CONSTRAINT ck_mood_entries_mood
        CHECK (mood IN ('very_happy', 'happy', 'neutral', 'sad', 'very_sad')),
    CONSTRAINT ck_mood_entries_note_length CHECK (CHAR_LENGTH(note) <= 200)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
