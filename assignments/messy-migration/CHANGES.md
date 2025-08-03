# Refactoring Report: User Management API

## Major Issues Identified
- **SQL Injection:** Original code used string interpolation for SQL queries, exposing the app to SQL injection.
- **Plaintext Passwords:** User passwords were stored and compared in plaintext.
- **No Input Validation:** No checks for email format, password strength, or required fields.
- **Poor Error Handling:** No proper HTTP status codes or JSON error responses.
- **Monolithic Structure:** All logic was in a single file with global DB connection/cursor.
- **Insecure DB Connection:** Use of `check_same_thread=False` could cause concurrency issues.

## Changes Made
- **Code Organization:** Split into `app/` package with `main.py` (routes), `models.py` (DB logic), `db.py` (DB connection), and `utils.py` (validation, hashing).
- **Security:**
  - All SQL queries use parameterized statements to prevent SQL injection.
  - Passwords are hashed using Werkzeug before storage and checked securely on login.
  - Input validation for email format and password length.
- **Best Practices:**
  - Proper HTTP status codes and JSON error messages.
  - Error handling for missing fields and DB errors.
  - No global DB connection; each request uses a context-managed connection.
- **Testing:** Added `test_api.py` for basic endpoint coverage.
- **Documentation:** This file and code comments/docstrings.

## Assumptions & Trade-offs
- Assumed SQLite is sufficient for this exercise; in production, use PostgreSQL or similar.
- Did not implement user registration/email uniqueness checks for brevity.
- Did not add logging or environment-based config (e.g., for DB path/secrets).
- Kept the API contract unchanged for compatibility.

## With More Time
- Migrate to a more robust DB and use an ORM (e.g., SQLAlchemy).

## Tools Used
- **VS Code Copilot/AI:** For code refactoring, patching, and documentation.
- **curl/Postman:** For manual API endpoint testing.
- **Python unittest:** For automated endpoint testing in `test_api.py`.
- **Flask:** For running the API server.
- **Werkzeug:** For password hashing and security.

## Purpose of Tools
- **Copilot/AI:** Refactored code, improved security, and generated documentation.
- **curl/Postman:** Verified endpoint behavior and error handling.
- **unittest:** Ensured endpoints work as expected and catch regressions.
- **Flask/Werkzeug:** Provided the web framework and security utilities.

## AI-Generated Code
- All refactored code was reviewed and tested.
- Some AI-generated code was modified for clarity, security, and best practices (e.g., parameterized queries, error handling, password hashing).
- Any code that did not meet requirements (e.g., insecure SQL, plaintext passwords) was rejected or replaced.
- Add more comprehensive tests (edge cases, error paths).
- Add logging and environment-based configuration.
- Enforce unique emails and add user registration constraints.
- Use Flask blueprints for further modularity.
- Add rate limiting, CORS, and production-ready deployment configs.
- Migrate to a more robust DB and use an ORM (e.g., SQLAlchemy).

---
**Contact:** For questions, see code comments or reach out to the maintainer.
