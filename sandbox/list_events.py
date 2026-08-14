import datetime
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]
TOKEN_PATH = "credentials/token.json"

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

if creds.expired and creds.refresh_token:
    creds.refresh(Request())

service = build("calendar", "v3", credentials=creds)

now_dt = datetime.datetime.now(datetime.UTC)
time_min = now_dt.isoformat()
time_max = (now_dt + datetime.timedelta(days=14)).isoformat()

events_result = service.events().list(
    calendarId="primary",
    timeMin=time_min,
    timeMax=time_max,
    maxResults=10,
    singleEvents=True,
    orderBy="startTime"
).execute()


events = events_result.get("items", [])

if not events:
    print("No upcoming events found.")
else:
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(start, "-", event["summary"])