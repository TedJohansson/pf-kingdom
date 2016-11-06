from flask import render_template
from kingdom import kingdom

@kingdom.route('/')
@kingdom.route('/index')
def index():
    grid = 25

    return render_template('index.html',
                           title='Home',
                           grid=grid)

