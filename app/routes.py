from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from sqlalchemy import desc

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')