from flask import Flask
from .config import TrackerSettings
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from alembic.config import Config as AlembicConfig
from alembic import command
from pathlib import Path
from flask_login import LoginManager
from .models import User, db as postgres_db
from .auth import auth as auth_blueprint
from .main import main as main_blueprint

def create_app(settings: TrackerSettings = None) -> Flask:
    if settings is None:
        settings = TrackerSettings()

    app = Flask(__name__)
    app.config.from_mapping(
        SETTINGS=settings,
        SECRET_KEY=settings.secret_key.get_secret_value(),
        SQLALCHEMY_DATABASE_URI=settings.db_url.get_secret_value(),
        FLASK_APP=settings.flask_app,
    )
    
    with app.app_context():
        initialize_db(app, postgres_db, settings)
        initialize_blueprints(app)
        initialize_login(app)

    return app


def initialize_db(app: Flask, db: SQLAlchemy, settings: TrackerSettings) -> Flask:
    Migrate(app, db)
    db.init_app(app)

    if settings.migrate_db:
        alembic_cfg = AlembicConfig(Path(__file__).parent / "migrations" / "alembic.ini")
        alembic_cfg.set_main_option("script_location", str(Path(__file__).parent / "migrations"))
        command.upgrade(alembic_cfg, "head")
    else:
        db.create_all()
    return app


def initialize_login(app: Flask) -> Flask:
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    return app

def initialize_blueprints(app: Flask) -> Flask:
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return app
