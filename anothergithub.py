from unittest.mock import Mock
import unittest
import requests
from requests import Session
import json

def get_user_name(user, session):
    """get github user data"""
    url = f"https://api.github.com/users/{user}"
    response = session.get(url)
    json_response = response.json()
    return json_response["name"]

class FakeSession:
    def get(self, url):
        return FakeResponse()
    
class FakeResponse:
    def json(self):
        return {"name": "Peter Lexus"}
    
fake_session = FakeSession()

fake_response = Mock()
fake_response.json = Mock(return_value={"name": "Peter Lexus"})

fake_session = Mock()
fake_session.get = Mock(return_value=fake_response)
# print(fake_response.json)
assert "Peter Lexus" == get_user_name("fierem", fake_session)