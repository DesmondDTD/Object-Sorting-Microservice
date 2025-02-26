# Object Sorting Microservice

## How to Use the Microservice

### Request Format:
- **Endpoint:** `/sort`
- **Method:** `POST`
- **Payload:**
  ```json
  {
    "data": [{"stock": "AAPL", "price": "$145.32"}, ...],
    "key": "price",
    "order": "desc"
  }
