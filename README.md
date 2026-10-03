# Daily Mood Check-in

Daily is a small, privacy-focused web application for students who want to record how they feel and revisit their reflections. A student creates an account, chooses one of five moods, can add a short note, and can review or delete previous check-ins.

## Current scope

- Email-and-password registration, login and logout.
- One check-in per account per local calendar day using five labelled moods.
- Optional notes of up to 200 characters.
- Persistent private history with per-entry deletion and clear-all controls.
- Responsive, keyboard-accessible screens with reduced-motion support.
- A gentle, dismissible support prompt after the most negative mood is selected.

Passwords are stored as one-way hashes. Mood entries are stored in MySQL and are always queried through the signed-in user, so one account cannot read or delete another account's history.

## Technology

- Python and Flask for server-rendered screens, signed sessions and JSON endpoints.
- SQLAlchemy Core and MySQL Connector/Python for database access.
- MySQL 8 with InnoDB and `utf8mb4` for persistent account and mood-entry data.
- Vanilla HTML, CSS and JavaScript for the interface.
- Gunicorn and Nginx for an AWS EC2 deployment.
- Pytest and GitHub Actions for automated checks.

## MySQL setup

Open MySQL as an administrator:

```bash
sudo mysql
```

Create the database and application user. Replace the example password with a strong URL-safe password:

```sql
CREATE DATABASE IF NOT EXISTS `app-db`
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'appuser'@'localhost'
  IDENTIFIED BY 'replace-with-a-secure-password';

GRANT ALL PRIVILEGES ON `app-db`.* TO 'appuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Apply the schema:

```bash
mysql -u appuser -p app-db < database/schema.sql
```

## Run locally

Python 3.10 or newer is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
# Edit .env and replace DATABASE_PASSWORD and the example JWT secret.
flask --app 'fullstack:create_app()' run --debug
```

Open <http://127.0.0.1:5000>. The health check is available at <http://127.0.0.1:5000/health>.

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Run tests

```bash
source .venv/bin/activate
pytest -q
```

The test suite uses an isolated database adapter and does not alter the development or production MySQL database.

## Project structure

```text
fullstack.py             Canonical Flask application entry point
backend/                 Application factory and SQLAlchemy persistence boundary
frontend/templates/      Authentication, check-in and history templates
frontend/static/         Vanilla CSS and JavaScript
database/schema.sql      MySQL users and mood-entry schema
deploy/                  Systemd and Nginx production templates
docs/zorentia-generation Historical generator reports and manifest
tests/                   Authentication, API and frontend contract tests
wsgi.py                  Compatibility WSGI entry point
```

## Configuration

Daily reads the following environment variables:

| Variable | Purpose | Requirement |
| --- | --- | --- |
| `DAILY_ENV` | Set to `production` on EC2 | Optional locally |
| `JWT_SECRET` | Signs authentication sessions | Required in production |
| `JWT_ISSUER` | Deployment identity expected by the Zorentia workflow | Defaults to `zorentia-app` |
| `DATABASE_URL` | SQLAlchemy MySQL connection URL | Required |
| `SESSION_COOKIE_SECURE` | Restricts the session cookie to HTTPS | Enable after HTTPS setup |

If the database password contains URL-reserved characters, percent-encode it before placing it in `DATABASE_URL`.

## Deploy to AWS EC2

The supplied files target an Ubuntu EC2 instance with MySQL installed on the same server.

### 1. Prepare the instance

Configure the EC2 security group to allow SSH (`22`) only from a trusted administrator IP, HTTP (`80`) for initial setup, and HTTPS (`443`) before public use. Do not expose MySQL port `3306` publicly.

```bash
sudo apt update
sudo apt install -y git nginx mysql-server python3-venv openssl
sudo systemctl enable --now mysql
```

### 2. Install the application

```bash
cd ~
git clone git@github.com:DanielHuynh611/daily-mood-check-in.git
cd ~/daily-mood-check-in
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Create the database and user using the earlier MySQL setup commands, then apply `database/schema.sql`.

Generate the Flask session secret:

```bash
openssl rand -hex 32
```

Create the repository-level `.env` file used by the Zorentia workflow:

```dotenv
DATABASE_URL=mysql+mysqlconnector://appuser:YOUR_DATABASE_PASSWORD@localhost:3306/app-db
JWT_SECRET=replace-with-the-generated-secret
JWT_ISSUER=zorentia-app
```

Protect it from other users:

```bash
chmod 600 .env
```

`SESSION_COOKIE_SECURE` defaults to `false` for the initial HTTP smoke test. Add `SESSION_COOKIE_SECURE=true` after HTTPS is enabled.

### 3. Enable Gunicorn and Nginx

```bash
sudo cp deploy/daily.service /etc/systemd/system/daily.service
sudo cp deploy/nginx.conf /etc/nginx/sites-available/daily
sudo ln -s /etc/nginx/sites-available/daily /etc/nginx/sites-enabled/daily
sudo rm -f /etc/nginx/sites-enabled/default
sudo systemctl daemon-reload
sudo systemctl enable --now daily
sudo nginx -t
sudo systemctl reload nginx
```

Verify the public endpoint:

```bash
curl http://YOUR_EC2_PUBLIC_IP/health
```

### 4. Add HTTPS before public use

Point a domain at the instance, replace `_` in `deploy/nginx.conf` with that domain, and use an ACME client such as Certbot to issue and renew a TLS certificate. Add `SESSION_COOKIE_SECURE=true` to `.env`, then restart Daily:

```bash
sudo systemctl restart daily
```

### Updating the deployment

```bash
cd ~/daily-mood-check-in
git pull --ff-only origin main
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
sudo systemctl restart daily
```

Check status and logs with:

```bash
systemctl status daily
journalctl -u daily -n 100 --no-pager
```

### Backing up persistent data

```bash
mysqldump -u appuser -p --single-transaction app-db > daily-app-backup.sql
```

Do not commit database backups or `.env` to Git.

## Privacy and limitations

- Daily stores email addresses and mood entries in the application database.
- The current version does not include email verification or password recovery.
- Users can delete individual entries or clear their mood history; account deletion is not currently included.
- Daily is a reflection tool, not a medical or crisis-support service.
- No analytics, advertising scripts or third-party frontend libraries are loaded.
