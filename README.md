# Daily Mood Check-in

Daily is a small, privacy-focused web application for students who want to record how they feel and revisit their reflections. A student creates an account, chooses one of five moods, can add a short note, and can review or delete previous check-ins.

## Current scope

- Email-and-password registration, login and logout.
- One check-in per account per local calendar day using five labelled moods.
- Optional notes of up to 200 characters.
- Persistent private history with per-entry deletion and clear-all controls.
- Responsive, keyboard-accessible screens with reduced-motion support.
- A gentle, dismissible support prompt after the most negative mood is selected.

Passwords are stored as one-way hashes. Mood entries are stored in SQLite and are always queried through the signed-in user, so one account cannot read or delete another account's history.

## Technology

- Python and Flask for server-rendered screens, signed sessions and JSON endpoints.
- SQLite for account and mood-entry persistence.
- Vanilla HTML, CSS and JavaScript for the interface.
- Gunicorn and Nginx for an AWS EC2 deployment.
- Pytest and GitHub Actions for automated checks.

## Run locally

Python 3.10 or newer is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
flask --app 'fullstack:create_app()' run --debug
```

Open <http://127.0.0.1:5000>. The SQLite database is created automatically at `instance/daily.db`. The health check is available at <http://127.0.0.1:5000/health>.

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Run tests

```bash
source .venv/bin/activate
pytest -q
```

## Project structure

```text
fullstack.py             Canonical Flask application entry point
backend/                 Application factory and SQLite persistence boundary
frontend/templates/      Authentication, check-in and history templates
frontend/static/         Vanilla CSS and JavaScript
database/schema.sql      Users and mood-entry schema
deploy/                  Systemd and Nginx production templates
docs/zorentia-generation Historical generator reports and manifest
tests/                   Authentication, API and frontend contract tests
wsgi.py                  Compatibility WSGI entry point
```

## Configuration

Daily reads the following environment variables:

| Variable | Purpose | Local default |
| --- | --- | --- |
| `DAILY_ENV` | Set to `production` on EC2 | `development` |
| `SECRET_KEY` | Signs authentication sessions; required in production | Development-only value |
| `DATABASE_PATH` | Absolute SQLite database location | `instance/daily.db` |
| `SESSION_COOKIE_SECURE` | Restricts the session cookie to HTTPS | `false` |

## Deploy to AWS EC2

The supplied files target an Ubuntu EC2 instance. The database is stored outside the Git working copy at `/var/lib/daily/daily.db`, so pulling a new release does not replace account data.

### 1. Prepare the instance

Configure the EC2 security group to allow SSH (`22`) only from a trusted administrator IP, HTTP (`80`) for initial setup, and HTTPS (`443`) before public use. Then install the runtime packages:

```bash
sudo apt update
sudo apt install -y git nginx python3-venv openssl
```

### 2. Install the application

Clone the repository to `/opt/daily`, create the environment and run the tests:

```bash
sudo mkdir -p /opt/daily
sudo chown ubuntu:www-data /opt/daily
git clone git@github.com:DanielHuynh611/daily-mood-check-in.git /opt/daily
cd /opt/daily
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Create a production secret with `openssl rand -hex 32`. Then create `/etc/daily.env` as root with permissions `600` and the following content:

```dotenv
SECRET_KEY=replace-with-the-generated-secret
SESSION_COOKIE_SECURE=false
```

Keep `SESSION_COOKIE_SECURE=false` only during the initial HTTP smoke test. Change it to `true` after HTTPS is enabled.

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

Systemd creates `/var/lib/daily` for the application. Starting the service creates the database schema automatically. Verify the public endpoint with:

```bash
curl http://YOUR_EC2_PUBLIC_IP/health
```

### 4. Add HTTPS before public use

Point a domain at the instance, replace `_` in `deploy/nginx.conf` with that domain, and use an ACME client such as Certbot to issue and renew a TLS certificate. Set `SESSION_COOKIE_SECURE=true` in `/etc/daily.env`, then restart Daily:

```bash
sudo systemctl restart daily
```

### Updating the deployment

```bash
cd /opt/daily
sudo -u ubuntu git pull --ff-only
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

Stop the service briefly, copy the database to a protected backup location, and restart it:

```bash
sudo systemctl stop daily
sudo cp /var/lib/daily/daily.db /var/lib/daily/daily-backup.db
sudo systemctl start daily
```

Do not commit the database or `/etc/daily.env` to Git.

## Privacy and limitations

- Daily stores email addresses and mood entries on the application server.
- The current version does not include email verification or password recovery.
- Users can delete individual entries or clear their mood history; account deletion is not currently included.
- Daily is a reflection tool, not a medical or crisis-support service.
- No analytics, advertising scripts or third-party frontend libraries are loaded.
