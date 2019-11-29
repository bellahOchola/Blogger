from . import create_app
import requests
from .models import 

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    