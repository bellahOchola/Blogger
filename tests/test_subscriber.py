import unittest
from app.models import Subscriber
from app import db

class TestSubscriber(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_subscriber = Subscriber(email = 'bee@gmail.com')

    def tearDown(self):
        '''
        method  that runs after each test case
        '''
        Subscriber.query.delete()

    def save_subscriber(sefl):
        '''
        method that helps test if subscriber is saved
        '''
        self.new_subscriber.save_subscriber()
        self.assertTrue(len(Subscriber.query.all())>0)
