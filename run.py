#!flask/bin/python
from kingdom import kingdom
class GridLayout:
    def __init__(self, x):
        self.size = [0 for a in range(x)]
kingdom.run(debug=True)