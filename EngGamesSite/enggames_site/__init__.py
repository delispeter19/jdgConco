from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from enggames_site.config import Config

# ======= Build App and DB =======================

# Init Extensions
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'admins.login'
login_manager.login_message_category = 'info'
mail = Mail()

migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)

    # Set Configs
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    # Import and Register blueprints
    from enggames_site.admins.endpoints import admins
    from enggames_site.events.endpoints import events
    from enggames_site.main.endpoints import main
    from enggames_site.restApi.endpoints import api
    from enggames_site.errors.handlers import errors
    app.register_blueprint(admins)
    app.register_blueprint(events)
    app.register_blueprint(main)
    app.register_blueprint(api)
    app.register_blueprint(errors)

    return app


def create_manager():
    manager = Manager(create_app())
    manager.add_command('db', MigrateCommand)

    return manager
