# Verification

Verified locally on 3 October 2026.

## Automated checks

```text
18 passed in 0.82s
```

The tests cover registration, password hashing, login and logout, protected routes, CSRF enforcement, persistence across application instances, one-entry-per-day enforcement, server-side validation, account ownership, individual and clear-all deletion, security headers, static assets, frontend contracts and MySQL DDL compilation.

## Additional checks

- Python modules compile successfully.
- The frontend JavaScript passes `node --check`.
- Flask resolves the canonical `fullstack:create_app()` factory and lists every expected route.
- Gunicorn accepts `fullstack:create_app()` as its production application factory.
- `GET /health` returns HTTP 200 and `{"service":"daily","status":"ok"}`.
- The rendered authentication, check-in and history pages contain the expected navigation, form controls, accessibility attributes and asset links.
- Production responses include a Content Security Policy, frame protection, MIME-sniffing protection, a no-referrer policy and restricted browser permissions.
- SQLAlchemy creates or verifies the MySQL tables at startup, and all entry queries are scoped to the authenticated user.

The historical Zorentia generation reports are preserved under `docs/zorentia-generation/` and do not describe the final runtime.
