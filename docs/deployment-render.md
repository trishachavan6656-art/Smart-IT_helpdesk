# Render deployment

The repository includes a Render Blueprint (`render.yaml`) for a Flask web
service and PostgreSQL database. It enables HTTPS-only session cookies,
generates a secret key, disables sample-data seeding, checks `/healthz`, and
provisions the first administrator with a one-time hook.

## Deploy from a Git repository

1. Put the project files at the root of a GitHub repository and push the
   reviewed deployment branch. Do not commit `.env`, databases, virtual
   environments, passwords, or Flask secrets.
2. In Render, choose **New → Blueprint**, connect that repository, and select
   its `render.yaml`.
3. When prompted for the `BOOTSTRAP_ADMIN_*` values, enter the intended admin
   name, email, and a unique password of at least 14 characters. These values
   are sent to Render as secret environment variables; do not put them in the
   YAML file or Git.
4. Create the Blueprint and wait for both the database and first web deploy to
   finish. The initial deployment hook creates the administrator. Then delete
   all three `BOOTSTRAP_ADMIN_*` variables from the web service's environment
   and save the change so Render redeploys without the bootstrap credentials.
5. Open the generated HTTPS service URL and sign in as the administrator.
   Register employee accounts from the app. Add engineer accounts by changing
   an existing account's role from **User management**.
6. Verify the administrator read-only boundary, employee ticket ownership,
   engineer resolution actions, `/healthz`, and the intended public demo data
   policy before sharing the link.

The Blueprint uses Render's free web and Postgres plans so the initial
classroom deployment does not select a paid tier. Free web services sleep
after inactivity and their first request may take about a minute to wake up;
free Postgres expires 30 days after creation and has no backups. Treat this as
a short-lived class/demo deployment. For a service expected to retain tickets,
upgrade the database and web service to paid plans, configure backups, and
verify a restore before accepting real employee data. [Render's free-plan
limitations](https://render.com/docs/free)

## Local production-start check

From the project root with dependencies installed:

```powershell
$env:SECRET_KEY = (python -c "import secrets; print(secrets.token_hex(32))")
$env:DATABASE_URL = "sqlite:///instance/helpdesk.db"
$env:SESSION_COOKIE_SECURE = "0"
gunicorn render_start:app --workers 1 --threads 4 --timeout 120
```

The `SESSION_COOKIE_SECURE=0` setting is only for local HTTP. The Render
Blueprint sets it to `1` because its public URL uses HTTPS.

## Monitoring setup

`/metrics` is a public Prometheus scrape endpoint and contains bounded HTTP
request, error, and duration aggregates. It does not expose ticket bodies or
user names. The provided Prometheus and Grafana files are configuration
examples: deploy a collector/dashboard separately if live monitoring is
required, and restrict metrics exposure at the network layer where possible.
