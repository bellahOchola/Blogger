from . import main
from flask import render_template,redirect
from .forms import BlogForm
from flask_login import login_required,current_user
from ..models import User


@main.route('/')
def index():

	title = 'Blog'
	return render_template('index.html',title = title)


@main.route('/blog', methods = ['GET', 'POST'])
@login_required
def blog():
	form = BlogForm()
	if form.validate_on_submit():
		title = form.title.data
		content = form.content.data
