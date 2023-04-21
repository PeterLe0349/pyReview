import requests, json
from requests import Session


def get_user_data(user, session):
    """get github user data"""
    url = f"https://api.github.com/users/{user}"
    response = session.get(url)
    return response

class FakeSession:
    def get(self, url):
        return "TESTING"

# session = FakeSession()
session = Session()
response = get_user_data("fierem", session)
decoded_response = response.json()
data = decoded_response
print(data)