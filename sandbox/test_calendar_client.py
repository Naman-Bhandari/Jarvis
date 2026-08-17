from jarvis.calendar_client import CalendarClient

client = CalendarClient()
events = client.list_events(days=14)

for event in events:
    start = event["start"].get("dateTime",event["start"].get("date"))
    print(event["id"],"-", start, "-", event["summary"])

new_event = client.create_event(
    summary="DSA Practice",
    start_time="2026-08-20T21:00:00+05:30",
    end_time="2026-08-20T22:00:00+05:30"
)

print("Created:", new_event.get("htmlLink"))