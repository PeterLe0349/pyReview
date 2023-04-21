from unittest.mock import Mock
import unittest
import requests
from requests import Session
import json

fake_response = Mock()
fake_response.json = Mock(return_value={"name": "Mario Corchero"})
fake_session = Mock()
fake_session.get = Mock(return_value=fake_response)
response_payload = {"name": "Mario Corchero"}
fake_session = Mock(**{"get.return_value.json.return_value": response_payload})

print(fake_session.get().json() )

def get_user_name(user):
    """get github user data"""
    url = f"https://api.github.com/users/{user}"
    session = Session()
    response = session.get(url)
    json_response = response.json()
    return json_response["name"]

