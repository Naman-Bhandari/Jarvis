import datetime
import datetime
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]
TOKEN_PATH = "credentials/token.json"


class CalendarClient:
    def __init__(self):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
        self.service = build("calendar", "v3", credentials=creds)

    def list_events(self, days=7, max_results=10):
        now_dt = datetime.datetime.now(datetime.UTC)
        time_min = now_dt.isoformat()
        time_max = (now_dt + datetime.timedelta(days=days)).isoformat()

        events_result = self.service.events().list(
            calendarId="primary",
            timeMin=time_min,
            timeMax=time_max,
            maxResults=max_results,
            singleEvents=True,
            orderBy="startTime"
        ).execute()

        return events_result.get("items", [])