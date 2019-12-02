from . import main
from flask import render_template,redirect,url_for, request, flash
from .forms import BlogForm, CommentForm
from flask_login import login_required,current_user
from ..models import Writer, Blogs, Comment, Subscriber
from ..request import get_quotes
from ..email import mail_message


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

		new_blog = Blogs(blog_title = title, blog_content = content, writer = current_user)
		new_blog.save_blog()
		return redirect (url_for('.index'))

	return render_template('blog.html', blog_form = form)


@main.route('/comments/<blog_id>', methods = ['GET', 'POST'])
def comment(blog_id):
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id)
        new_comment.save_comment()
        return redirect(url_for('.index'))
    return render_template('comments.html', comment_form =comment_form)


@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to D-Blog","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))
