from . import main
from flask import render_template,redirect,url_for
from .forms import BlogForm
from flask_login import login_required,current_user
from ..models import User, Blogs
from ..request import get_quotes


@main.route('/')
def index():
	vlogs = Blogs.query.all()
	quotes = get_quotes()
	title = 'Blog'
	return render_template('index.html',title = title, vlogs = vlogs, quotes = quotes)


@main.route('/blog', methods = ['GET', 'POST'])
@login_required
def blog():
	form = BlogForm()
	if form.validate_on_submit():
		title = form.title.data
		content = form.content.data

		new_blog = Blogs(blog_title = title, blog_content = content, user = current_user)
		new_blog.save_blog()
		return redirect (url_for('.index'))

	return render_template('blog.html', blog_form = form)

