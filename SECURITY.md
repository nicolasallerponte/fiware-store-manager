# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| latest (main) | ✅ |
| older tags | ❌ |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

If you discover a security vulnerability, please report it privately by:

1. Opening a [GitHub Security Advisory](https://github.com/nicolasallerponte/fiware-store-manager/security/advisories/new) in this repository
2. Or emailing the maintainer directly (see GitHub profile)

Please include:

- A description of the vulnerability
- Steps to reproduce it
- Potential impact
- Any suggested fixes if you have them

You can expect a response within **72 hours**. Once the vulnerability is confirmed, we will work on a fix and coordinate disclosure.

---

## Security Considerations for Deployment

This project is a **development/academic application** and is not hardened for production. Before deploying in any real environment, consider:

- **Flask secret key**: Set a strong `SECRET_KEY` in your `.env` file. Do not use the default development key.
- **Debug mode**: Disable `DEBUG=True` in production. Never expose the Werkzeug debugger publicly.
- **Database**: SQLite is not suitable for concurrent production workloads. Migrate to PostgreSQL or MongoDB via Orion.
- **Docker**: The provided `docker-compose.yml` is for development only. It exposes ports directly and has no authentication on MongoDB.
- **Environment variables**: Never commit `.env` to version control. Use `.env.example` as a template.
- **HTTPS**: The development server does not use HTTPS. Use a reverse proxy (nginx, Caddy) with TLS in production.

---

## Dependencies

Keep dependencies up to date. Run periodically:

```bash
pip list --outdated
```
