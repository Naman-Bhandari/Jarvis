from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]
TOKEN_PATH = "credentials/token.json"

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build("calendar", "v3", credentials=creds)

event = {
    'summary': 'GYM',
    'start': {"dateTime": "2026-08-15T18:00:00+05:30", "timeZone": "Asia/Kolkata"},
    "end": {"dateTime": "2026-08-15T19:00:00+05:30", "timeZone": "Asia/Kolkata"}
}

created_event = service.events().insert(calendarId="primary", body=event).execute()

print("Event created:", created_event.get("htmlLink"))