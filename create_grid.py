import sys
from sqlalchemy.ext import serializer
from kingdom.models import Grid, db
from kingdom import kingdom, bcrypt

class GridLayout:
    def __init__(self, x):
        self.size = [1 for a in range(x)]

def main():
    """Main entry point for script."""
    with kingdom.app_context():
        db.metadata.create_all(db.engine)
        grid = GridLayout(25)
        grid.size[5] = 5
        user = Grid(grid=serializer.dumps(grid), size=25, user_id=1)
        db.session.add(user)
        db.session.commit()
        print('User added.')



if __name__ == '__main__':
    sys.exit(main())