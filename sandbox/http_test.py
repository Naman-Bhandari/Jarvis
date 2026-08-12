import requests

response1 = requests.put(url="https://postman-echo.com/put", json={
    "title": "Gym",
    "time": "19:00"
})
response2 = requests.delete(url="https://postman-echo.com/delete")

print("Status1:", response1.status_code," Status2:", response2.status_code, "JSON:", response1.json(), response2.json())