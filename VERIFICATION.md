# Verification

Verified locally on 3 October 2026.

## Automated checks

```text
17 passed in 0.81s
```

The tests cover registration, password hashing, login and logout, protected routes, CSRF enforcement, persistence across application instances, one-entry-per-day enforcement, server-side validation, account ownership, individual and clear-all deletion, security headers, static assets and frontend contracts.

## Additional checks

- Python modules compile successfully.
- The frontend JavaScript passes `node --check`.
- Flask resolves the canonical `fullstack:create_app()` factory and lists every expected route.
- Gunicorn accepts `fullstack:create_app()` as its production application factory.
- `GET /health` returns HTTP 200 and `{"service":"daily","status":"ok"}`.
- The rendered authentication, check-in and history pages contain the expected navigation, form controls, accessibility attributes and asset links.
- Production responses include a Content Security Policy, frame protection, MIME-sniffing protection, a no-referrer policy and restricted browser permissions.
- The SQLite schema is created automatically and isolates entries by authenticated user.

The historical Zorentia generation reports are preserved under `docs/zorentia-generation/` and do not describe the final runtime.
