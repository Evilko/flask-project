from peewee import IntegrityError, DoesNotExist

from app import auth
from flask import Blueprint, render_template, redirect
from flask.views import MethodView
from flask import request
from flask import session
User = auth.get_user_model()

bp = Blueprint('main_auth', __name__, template_folder='templates')


class RegisterView(MethodView):
    def get(self):
        return render_template('register.html')

    def post(self):
        try:
            User.create(
                username=request.form['login'],
                password=request.form['password'],
                email=request.form['email'],
                active=True,
                admin=False
            )
            return redirect('/login')
        except IntegrityError:
            return redirect('/')


class LoginView(MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        try:
            user = User.get(
                User.username == request.form['login'],
                User.username == request.form['password']
            )
            session['auth'] = True
            return redirect('/')
        except DoesNotExist:
            return redirect('/')


class LogoutView(MethodView):
    def get(self):
        try:
            session['auth'] = False
        except KeyError:
            pass
        return redirect('/')


bp.add_url_rule(
    '/register',
    view_func=RegisterView.as_view(
        name='register',
    ),
)

bp.add_url_rule(
    '/login',
    view_func=LoginView.as_view(
        name='login',
    ),
)

bp.add_url_rule(
    '/logout',
    view_func=LogoutView.as_view(
        name='logout',
    ),
)
