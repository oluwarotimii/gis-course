from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import requests
from config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

app = Flask(__name__)
app.config.from_object(Config)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Dummy user class, in a real app, you would connect to a DB
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    # In a real app, you would fetch the user from your database
    return User(user_id, 'dummy_username')

# Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

# Login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Register route
@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # Call JupyterHub API to create the user
        hub_url = f"{app.config['JUPYTERHUB_URL']}/hub/api/users/{form.username.data}"
        response = requests.post(hub_url, headers={
            'Authorization': f'token {app.config["JUPYTERHUB_API_TOKEN"]}'
        }, json={
            'name': form.username.data,
            'admin': False
        })
        
        if response.status_code == 201:
            flash('Your account has been created! You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error creating user in JupyterHub.', 'danger')

    return render_template('register.html', form=form)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # Authenticate with JupyterHub
        hub_url = f"{app.config['JUPYTERHUB_URL']}/hub/api/login"
        auth_data = {
            'username': username,
            'password': password
        }
        response = requests.post(hub_url, json=auth_data)

        if response.status_code == 200:
            user = User(id=1, username=username)
            login_user(user)
            return redirect(f"{app.config['JUPYTERHUB_URL']}/hub/home")
        else:
            flash('Login failed. Please check your username and password.', 'danger')

    return render_template('login.html', form=form)

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
