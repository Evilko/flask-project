from flask_session import Session

from settings import Config
from flask_peewee.db import Database
from flask_peewee.auth import Auth
from flask_peewee.admin import Admin
from flask import Flask, session
from os import getenv


app = Flask(
        __name__.split('.')[0],
        static_url_path='/static',
        static_folder=f'{Config.PROJECT_PATH}/static',
        template_folder=f'{Config.PROJECT_PATH}/templates'
    )

app.config.from_object(Config)

db = Database(app)
auth = Auth(app, db)
admin = Admin(app, auth)


def create_database():
    from src.blog.models import Note
    Note.create_table(fail_silently=True)
    auth.User.create_table(fail_silently=True)


def admin_register():
    from src.blog.models import Note
    admin.register(Note)
    admin.register(auth.get_user_model())
    admin.setup()


def register_blueprints():
    from src.blog.views import bp as blog_bp
    from src.auth.views import bp as auth_bp
    app.register_blueprint(blog_bp)
    app.register_blueprint(auth_bp)


def create_admin():
    user_admin = auth.User(username='admin', email='', admin=True, active=True)
    user_admin.set_password('admin')
    user_admin.save()


Session(app)

create_database()
admin_register()
register_blueprints()

if getenv('CREATE_ADMIN'):
    create_admin()

if __name__ == '__main__':
    app.run()
