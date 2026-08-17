from jarvis.calendar_client import CalendarClient

client = CalendarClient()
events = client.list_events(days=14)

for event in events:
    start = event["start"].get("dateTime",event["start"].get("date"))
    print(event["id"],"-", start, "-", event["summary"])
