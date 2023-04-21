from unittest.mock import patch
import requests
import anothergithub2

print(requests.Session)

with patch("requests.Session") as mock:
    print("Patching Started")
    print(requests.Session)
    print("Patching finished")

print(requests.Session)

payload = {"name": "Secret user"}

with patch("requests.Session") as mock:
    mock.return_value.get.return_value.json.return_value = payload
    print(anothergithub2.get_user_name("fierem"))

with patch("anothergithub2.Session") as mock:
    mock.return_value.get.return_value.json.return_value = payload
    print(anothergithub2.get_user_name("fierem"))