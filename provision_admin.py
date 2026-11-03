"""Create the first hosted administrator from one-time deployment secrets.

Render runs this once after the first successful Blueprint deployment. The
three BOOTSTRAP_ADMIN_* values must be deleted from the service environment
after provisioning. This module never prints the password or secret values.
"""

import os

from app import app, validate_email
from models import DEPARTMENTS, User, db


def main():
    name = os.environ.get("BOOTSTRAP_ADMIN_NAME", "").strip()
    email = os.environ.get("BOOTSTRAP_ADMIN_EMAIL", "").strip().lower()
    password = os.environ.get("BOOTSTRAP_ADMIN_PASSWORD", "")

    if not name or len(name) < 3:
        raise SystemExit("Set BOOTSTRAP_ADMIN_NAME to the administrator's full name.")
    if not validate_email(email):
        raise SystemExit("Set BOOTSTRAP_ADMIN_EMAIL to a valid email address.")
    if len(password) < 14:
        raise SystemExit("BOOTSTRAP_ADMIN_PASSWORD must be at least 14 characters.")

    with app.app_context():
        db.create_all()
        if User.query.filter_by(role="admin").first():
            print("An administrator already exists; no account was changed.")
            return
        if User.query.filter_by(email=email).first():
            raise SystemExit("That email already belongs to another account; no account was changed.")

        user = User(
            name=name,
            email=email,
            department="IT" if "IT" in DEPARTMENTS else DEPARTMENTS[0],
            role="admin",
            password=password,
        )
        db.session.add(user)
        db.session.commit()
        print("Initial administrator provisioned. Remove BOOTSTRAP_ADMIN_* values from the service environment now.")


if __name__ == "__main__":
    main()
