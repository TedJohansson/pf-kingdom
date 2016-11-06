#!/usr/bin/env python
"""Create a new admin user able to view the /reports endpoint."""
from getpass import getpass
import sys

from flask import current_app
from kingdom import kingdom, bcrypt
from kingdom.models import User, db

def main():
    """Main entry point for script."""
    with kingdom.app_context():
        db.metadata.create_all(db.engine)
        if User.query.all():
            print('A user already exists! Create another? (y/n):',)
            create = 'y'
            if create == 'n':
                return

        print('Enter email address: '),
        email = 'ted.johansson@test.com'
        password = getpass()
        assert password == getpass('Password (again):')

        user = User(username='Test', email=email, password=bcrypt.generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        print('User added.')



if __name__ == '__main__':
    sys.exit(main())