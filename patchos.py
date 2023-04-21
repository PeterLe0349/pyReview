import os
from unittest.mock import patch

def get_unix_user():
    print(os.getenv("USER"))

get_unix_user()

with patch.dict(os.environ, {"USER": "root"}):
    get_unix_user()