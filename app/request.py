from . import create_app
import requests, json
from .models import Quotes

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/')
    return response
    # if response.status_code == 200:
    #     quote = response.json()
        # return quote