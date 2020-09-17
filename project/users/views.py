#users/views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from project import db
from project.models import User
from project.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from project.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)

# register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

# login
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() #.fist --> there should be only one user, but .fist gives him in the right format (instead of list array of results)

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('you are now logged in!')
            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('core.index')
            return redirect(next)
    flash('UserName or Password not correct. Try again!')
    return render_template('login.html', form=form)

# logout
@users.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for("core.index"))

# account
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():

    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.login'))

    elif request.method =="GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)


