from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from google.auth.transport.requests import Request

# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

# Authenticate a credential with the service account
credentials = service_account.Credentials.from_service_account_file("./key.json", scopes=scopes)

# Use the credentials object to authenticate a Requests session.
authed_session = AuthorizedSession(credentials)
response = authed_session.get("https://<DATABASE_NAME>.firebaseio.com/users/ada/name.json")

# Or, use the token directly, as described in the "Authenticate with an
# access token" section below. (not recommended)
request = Request()
credentials.refresh(request)
access_token = credentials.token
# print(access_token)

