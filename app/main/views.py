from . import main
from flask import render_template,redirect
# from .forms import PomodForm
from flask_login import login_required,current_user
from ..models import User


@main.route('/')
def index():

	title = 'Blog'
	return render_template('index.html',title = title)
