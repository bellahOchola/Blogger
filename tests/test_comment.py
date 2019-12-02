import unittest
from app.models import Comment, User
from app import db

class TestComment(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_comment = Comment(user_id = 56, comment = 'such a wonderful blog')

    def tearDown(self):
        '''
        method  that runs after each test case
        '''
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'such a wonderful blog')
        self.assertEquals(self.new_comment.user_id,56)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment(self):
        self.new_comment.save_comment()
        comment = Comment.get_comments(1)
        self.assertTrue(comment is not None)