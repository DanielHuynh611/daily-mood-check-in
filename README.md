# Daily Mood Check-in

Daily is a small, privacy-focused web application for students who want to record how they feel without creating an account. A student chooses one of five moods, can add a short note, and can review previous check-ins in reverse chronological order.

## Current scope

- One check-in per local calendar day using five labelled mood choices.
- Optional notes of up to 200 characters.
- A private history with per-entry deletion and clear-all controls.
- Responsive, keyboard-accessible screens with reduced-motion support.
- A gentle, dismissible support prompt after the most negative mood is selected.

Mood entries never leave the browser. They are stored under the versioned `localStorage` key `daily.moodEntries.v1`; the Flask server receives no mood, note or history data. There is consequently no user account, authentication flow or server-side database.

## Technology

- Python and Flask for server-delivered HTML and the health endpoint.
- Vanilla HTML, CSS and JavaScript for the interface and browser-local persistence.
- Gunicorn and Nginx for an AWS EC2 production deployment.
- Pytest and GitHub Actions for automated checks.

## Run locally

Python 3.10 or newer is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
flask --app 'backend:create_app()' run --debug
```

Open <http://127.0.0.1:5000>. The history screen is at <http://127.0.0.1:5000/history>, and the deployment health check is at <http://127.0.0.1:5000/health>.

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
backend/                 Flask application factory
frontend/templates/      Shared check-in and history template
frontend/static/         Vanilla CSS and JavaScript
database/schema.sql      Records the intentional no-database design
deploy/                  Systemd and Nginx production templates
docs/zorentia-generation Historical generator reports and manifest
tests/                   Flask and frontend contract tests
wsgi.py                  Gunicorn entry point
```

## Deploy to AWS EC2

The supplied configuration targets an Ubuntu EC2 instance. The application itself needs no AWS database or persistent volume because user entries remain in each visitor's browser.

### 1. Prepare the instance

Use an Ubuntu LTS instance and configure its security group to allow:

- SSH (`22`) only from a trusted administrator IP.
- HTTP (`80`) from the intended audience.
- HTTPS (`443`) when TLS is configured.

Connect to the instance, then install the runtime packages:

```bash
sudo apt update
sudo apt install -y git nginx python3-venv
```

### 2. Install the application

The repository is private. On the EC2 instance, create a dedicated SSH key and add the displayed public key under **GitHub repository → Settings → Deploy keys** with read-only access:

```bash
ssh-keygen -t ed25519 -C "daily-ec2" -f /home/ubuntu/.ssh/daily_deploy -N ""
cat /home/ubuntu/.ssh/daily_deploy.pub
```

Then clone and configure the working copy to keep using that key:

```bash
sudo mkdir -p /opt/daily
sudo chown ubuntu:www-data /opt/daily
GIT_SSH_COMMAND="ssh -i /home/ubuntu/.ssh/daily_deploy -o IdentitiesOnly=yes" git clone git@github.com:DanielHuynh611/daily-mood-check-in.git /opt/daily
cd /opt/daily
git config core.sshCommand "ssh -i /home/ubuntu/.ssh/daily_deploy -o IdentitiesOnly=yes"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Run a production smoke test before registering the service:

```bash
.venv/bin/gunicorn --bind 127.0.0.1:8000 wsgi:app
```

In another terminal, `curl http://127.0.0.1:8000/health` should return `{"service":"daily","status":"ok"}`.

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

Point a domain name at the EC2 instance, replace `_` in `deploy/nginx.conf` with that domain, and use an ACME client such as Certbot to issue and renew a TLS certificate. HTTPS is important because mood notes are sensitive even though they stay in the browser.

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

## Privacy and limitations

- History is specific to one browser profile on one device and is not synced.
- Clearing browser site data removes the history permanently.
- Daily is a reflection tool, not a medical or crisis-support service.
- No analytics, advertising scripts or third-party frontend libraries are loaded.
