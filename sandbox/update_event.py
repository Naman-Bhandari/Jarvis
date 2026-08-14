from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]
TOKEN_PATH = "credentials/token.json"

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build("calendar", "v3", credentials=creds)

event_id = "app42deqolilrgip9jpmf2mvg0"

updated_event = {
    'summary': 'GYM',
    'start': {"dateTime": "2026-08-15T19:00:00+05:30", "timeZone": "Asia/Kolkata"},
    "end": {"dateTime": "2026-08-15T20:00:00+05:30", "timeZone": "Asia/Kolkata"}
}

# your .update() call goes here

updates = service.events().update(calendarId="primary",eventId=event_id,body=updated_event).execute()

print("Event updated:", updates.get("htmlLink"))