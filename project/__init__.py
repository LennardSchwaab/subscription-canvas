from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

####################
##initialize app ###
####################

app = Flask(__name__)

app.config['SECRET_KEY'] = '4.Null'  ##needed for forms, exchange with enrivonment varialbe later!
app.config['SESSION_TYPE'] = 'filesystem'

#####################
####DATABASE SETUP###
#####################
# Often people will also separate these into a separate config.py files

ENV = "test_prod_db" #choose mode: dev, prod or else its production on heroku
if ENV == "dev":
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SPTBZ5ZAtO3lub4akXSh@localhost/dsdb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/data_mtc'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://ywyqfmeidiqxzj:772bc41a7bacdba1a3275638d60e2d3ef409a9c0f9a33c17a42b4f7c6cb7fc22@ec2-176-34-123-50.eu-west-1.compute.amazonaws.com:5432/dbd08n32h822al'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#########################
### LOGIN CONFIGS #######
#########################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

# NOTE! These imports need to come after you've defined db, otherwise you will
# get errors in your models.py files.
## Grab the blueprints from the other views.py files for each "app"
from project.canvas.views import canvas_blueprint
from project.quick_check.views import check_blueprint

from project.core.views import core
from project.users.views import users
from project.error_pages.handlers import error_pages

app.register_blueprint(canvas_blueprint, url_prefix='/canvas')
app.register_blueprint(check_blueprint, url_prefix='/check')

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
