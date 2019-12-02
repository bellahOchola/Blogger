import unittest
from app.models import Blogs, Writer
from app import db

class TestBlog(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_blog = Blogs(blog_id = 234, blog_title = 'tech', blog_content = 'technology has greatly revolutionised the universe', posted = '24/11/2019', writer_id = 34)

    def tearDown(self):
        '''
        method  that runs after each test case
        '''
        Blogs.query.delete()
        Writer.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.blog_id,234)
        self.assertEquals(self.new_blog.blog_title,'tech')
        self.assertEquals(self.new_blog.writer_id,34)
        self.assertEquals(self.new_blog.blog_content,'technology has greatly revolutionised the universe')

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blogs.query.all())>0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blogs()
        blog = Blogs.get_blog(1)
        self.assertTrue(blog is not None)

    