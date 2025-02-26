import requests

url = "http://127.0.0.1:5000/sort"

payload = {
    "data": [
        {"stock": "AAPL", "price": "$145.32"},
        {"stock": "GOOGL", "price": "$2753.56"},
        {"stock": "MSFT", "price": "$299.79"}
    ],
    "key": "price",
    "order": "desc"
}

response = requests.post(url, json=payload)
print(response.json())
