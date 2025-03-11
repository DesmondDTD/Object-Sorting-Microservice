# Object Sorting Microservice

Communication Contract
Request Format:
Endpoint: /sort
Method: POST
Request Body:
data: A list of objects that you want to sort. Each object must contain the key that will be used for sorting.
key: The key in the object by which the data will be sorted (e.g., "price").
order: The order in which you want to sort the data. Possible values: "asc" for ascending, "desc" for descending. Default is "asc".
Example Request:
json
Copy
{
  "data": [
    {"stock": "AAPL", "price": "$145.32"},
    {"stock": "GOOGL", "price": "$2753.56"},
    {"stock": "MSFT", "price": "$299.79"}
  ],
  "key": "price",
  "order": "desc"
}
How to Send a Request Programmatically:
To send a POST request to the microservice, you can use libraries like requests in Python. Here is an example of how to send a request to sort the stock data by price in descending order:

python
Copy
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
Response Format:
sorted_data: The sorted list of objects based on the specified key and order.
index: A list representing the 1-based index of the sorted items.
Example Response:
json
Copy
{
  "sorted_data": [
    {"stock": "GOOGL", "price": "$2753.56"},
    {"stock": "MSFT", "price": "$299.79"},
    {"stock": "AAPL", "price": "$145.32"}
  ],
  "index": [1, 2, 3]
}
How to Receive Data Programmatically:
After sending a request, you can receive and parse the JSON response like so:

python
Copy
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

if response.status_code == 200:
    data = response.json()
    print(f"Sorted Data: {data['sorted_data']}")
    print(f"Indexes: {data['index']}")
else:
    print(f"Error: {response.json()}")

![UML Sequence Diagram](uml_sequence_diagram.png)
