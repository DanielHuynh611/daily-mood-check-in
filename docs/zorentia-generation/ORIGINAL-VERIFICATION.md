# Verification results

Start with the report for the part of the application you are working on:

- [Architecture](verification/architecture.md): contracts, coverage and retained validation attempts.
- [Database](verification/database.md): SQL generation, recorded failures and execution limits.
- [Backend](verification/backend.md): static checks, affected files and generation/repair history.
- For a full-stack download, open `verification/frontend.md` and `verification/fullstack.md`
  (linked directly in `README-FULLSTACK.md`). They contain frontend checks, route conflicts,
  commands, exit codes and captured output.

Reports describe this package's snapshots. They do not update after you edit the files.
Passed checks only cover their stated scope. Historical failed attempts are distinguished
from current findings. Missing evidence and checks not run are stated explicitly.
Reports do not certify production readiness or complete business functionality.
