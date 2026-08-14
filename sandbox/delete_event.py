from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]
TOKEN_PATH = "credentials/token.json"

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build("calendar", "v3", credentials=creds)

deletes = service.events().delete(calendarId="primary",eventId="ggmpfb0vft3uriv6mek1b3rab8").execute()
print("Event Deleted")