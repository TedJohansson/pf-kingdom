from flask import render_template, flash, redirect, session, url_for, request, g, abort
from flask_login import login_user, logout_user, current_user, login_required
from kingdom import kingdom, db, lm, bcrypt
from .forms import LoginForm, GridForm
from .models import User, Buildings

@kingdom.route('/', methods=['GET', 'POST'])
@kingdom.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    list_buildings = Buildings.query.values(Buildings.name)
    user = g.user
    grid = 25
    building_img = 'Bank'
    if request.method == 'POST':
        form = GridForm(request.form)
        building_img = request.form['building_name']
    return render_template('index.html',
                           title='Home',
                           user=user,
                           grid=grid,
                           buildings=list_buildings,
                           building_img=building_img)

@kingdom.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def user_loader(id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(id)

# route for handling the login page logic
@kingdom.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is not None and bcrypt.check_password_hash(
            user.password, request.form['password']
        ):
            login_user(user)
            flash('You were logged in. Go Crazy.')
            return redirect(url_for('index'))

        else:
            error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)