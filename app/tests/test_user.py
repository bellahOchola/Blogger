import unittest
from .models import *
from app import db

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_user = User(username = 'bellah',  fullname = 'bellah ochola' email = 'bellah@gmail.com', password = 'bee' )
        self.new_blog = Blogs(blog_id = '234', blog_title = 'tech', blog_content = 'technology has greatly revolutionised the universe', posted = '24/11/2019', writer_id = '34')
        self.new_comment = Comment(user_id = '56', comment = 'such a wonderful blog')
        self.new_subscriber = Subscriber(email = 'bee@gmail.com')

    def tearDown(self):
        '''
        method  that runs after each test case
        '''
        User.query.delete()
        Blogs.query.delete()
        Comment.query.delete()
        Subscriber.query.delete()

