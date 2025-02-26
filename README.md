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

## UML Sequence Diagram

Below is the UML Sequence Diagram for the Object Sorting Microservice:

![UML Sequence Diagram](uml_sequence_diagram.png)
