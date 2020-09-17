#
from project import app
from flask import render_template, Flask, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required


#home page = index page
@app.route('/')
def index():
    return render_template('home.html')

#welcome page for first log in
@app.route('/welcome')
@login_required
def welcome():
    return render_template('home.html')
    #return render_template('home.html')

#run app
if __name__ == '__main__':
    app.run()