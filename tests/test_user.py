import unittest
from app.models import Writer
from app import db

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_user = Writer(username = 'bellah',  full_name = 'bellah ochola', email = 'bellah@gmail.com', pass_word = 'bee' )

    def tearDown(self):
        '''
        method  that runs after each test case
        '''
        Writer.query.delete()

    def test_save_user(self):
        db.session.add(self)
        db.session.commit()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_user.username, 'bellah')
        self.assertEquals(self.new_user.full_name, 'bellah ochola')
        self.assertEquals(self.new_user.email, 'bellah@gmail.com')
       

