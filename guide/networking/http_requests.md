# HTTP Requests

## Introduction to HTTP Requests

### Overview of HTTP

HTTP (Hypertext Transfer Protocol) is the foundational protocol used by the World Wide Web. It defines how messages are formatted and transmitted, and what actions web servers and browsers should take in response to various commands. HTTP uses a client-server model where the client (usually a web browser) requests resources (like HTML documents, images, etc.), and the server provides these resources, often interacting with backend systems to deliver dynamic content.

### HTTP Request Basics

An HTTP request is made by a client to request an action on a resource (identified by a URL) on a server. Each request consists of the following parts:

- **Method**: An HTTP method, often called a verb, indicates the desired action to be performed on the resource. The common methods include GET, POST, PUT, DELETE, PATCH, etc.

- **URL** (Uniform Resource Locator): The address of the resource on the server.

- **Headers**: Provide additional information (metadata) about the request or about the client itself. For example, Content-Type header tells the server about the format of the data in the request body.

- **Body (optional)**: Contains data sent to the server. This part is optional and usually used with methods like POST or PUT.

#### Example:

- The following request creates a new user with the provided name and email.
- The Content-Type: application/json header indicates that the data being sent is in JSON format.

Request line (Method + URL):

```
POST /api/users HTTP/1.1
```

Header:

```
Host: exampleapi.com
Content-Type: application/json
```

Body:

```
{
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
}
```

## Types of HTTP Requests

HTTP methods are used to specify the desired action to be performed on a given resource. Each method has a specific, defined purpose and plays a crucial role in the interaction between the client and the server. Here's a more detailed look at the key HTTP methods:

- **GET**: Requests data from a specified resource. GET requests should only retrieve data and have no other effect.
- **POST**: Sends data to the server to create a new resource. Data is included in the body of the request.
- **PUT**: Sends data to update an existing resource. The PUT method is idempotent, meaning that sending the same request multiple times will not have different effects.
- **DELETE**: Removes the specified resource.
- **PATCH**: Applies partial modifications to a resource.

### Response to an HTTP Request

After the server processes an HTTP request, it returns an HTTP response. The response typically contains:

- **Status Code**: Indicates the outcome of the request. For example, 200 OK for success, 404 Not Found for an invalid URL, and 500 Internal Server Error for server errors.

- **Response Headers**: Similar to request headers, these headers provide information about the server and about the response.

- **Response Body**: Contains the resource data requested by the client or a message body.

### About HTTP Methods:

#### GET

- **Purpose**: The GET method is used to retrieve data from a server at a specified resource.
- **Usage**: When you make a GET request, you are asking the server to send back the data for the specified resource. This is the most common HTTP method.
- **Characteristics**:
  - **Safe**: It does not alter the state of the resource (read-only).
  - **Idempotent**: Multiple identical requests will have the same effect as a single request.
- **Example**: Get a list of books from a bookstore API: `GET /api/books`.
- **Response**:
    ```json
    [
        {"id": 1, "title": "1984", "author": "George Orwell"},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
    ]
    ```

#### POST

- **Purpose**: The POST method is used to send data to the server to create a new resource.
- **Usage**: It's commonly used when submitting form data or uploading a file. POST requests usually carry payload data in the request body.
- **Characteristics**:
  - **Not Safe**: It changes the server state by creating a new resource.
  - **Not Idempotent**: Making several identical POST requests will result in multiple resources being created.
- **Example**: Add a new book to the bookstore.
    ```json
    POST /api/books
    Content-Type: application/json
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }
    ```
- **Respone**:
    ```python
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }
    ```

#### PUT

- **Purpose**: PUT is used to update an existing resource or create a new resource if it does not exist. It usually includes the full data of the resource.
- **Usage**: The client sends data that updates the entire resource at the specified URI.
- **Characteristics**:
  - **Not Safe**: It modifies the server state.
  **Idempotent**: Repeated requests with the same data will result in the same state of the resource (e.g., updating a user's details).
- **Example**: Update information about a book.
    ```json
    PUT /api/books/3
    Content-Type: application/json
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    }
    ```
- **Response**:
```json
{
    "id": 3,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}
```

#### PATCH

- **Purpose**: PATCH is used for modifying an existing resource, but it updates only the specified parts of the resource, not the entire resource.
- **Usage**: This is particularly useful for large resources, where you may want to update just a part of the resource.
- **Characteristics**:
  - **Not Safe**: It modifies the server state.
  - **Idempotent**: Applying the same PATCH request multiple times will result in the same resource state.
- **Example**: Update the year of a particular book.
    ```json
    PATCH /api/books/3
    Content-Type: application/json
    {
        "year": 2023
    }
    ```
- **Response**:
    ```json
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 2023
    }
    ```

#### DELETE

- **Purpose**: DELETE is used to remove a resource from the server.
- **Usage**: It is a straightforward method used when you want to delete the resource identified by the request URI.
- **Characteristics**:
  - **Not Safe**: It changes the server state by removing the resource.
  - **Idempotent**: Deleting the same resource multiple times results in the same outcome, the resource is removed.
- **Example**: Delete a book from the bookstore. `DELETE /api/books/3`
- **Response**: Response: Usually, DELETE requests might not return a body. Instead, they might return a status code like 204 No Content to indicate successful deletion.

## REST API and RESTful API

### What is REST?

REST (Representational State Transfer) API is a set of guidelines and best practices for creating scalable web services. REST APIs are designed around the use of standard HTTP protocols and methods to make requests and receive responses. In a RESTful system, resources (like data or objects) are represented and manipulated using these standard HTTP methods.

### RESTful API

A RESTful API adheres to the REST architectural style and constraints. These APIs are characterized by their use of standard HTTP methods, ability to operate over any protocol that provides standard HTTP semantics (like HTTPS), and their stateless nature.

### Principles of REST

- **Resource-Based**: In REST, everything is a resource, and each resource is accessed via a unique URI (Uniform Resource Identifier).

- **Stateless Operations**: Each HTTP request from a client to a server must contain all the information needed to understand the request. The server does not store any client context between requests.

- **Use of HTTP Methods**: REST APIs primarily use HTTP methods (GET, POST, PUT, PATCH, DELETE) to perform CRUD operations.

- **Representation of Resources**: Resources are typically represented in formats like JSON or XML. When a client requests a resource, it receives the representation, not the resource itself.

### How REST APIs Differ from HTTP

While REST APIs use HTTP as a transport protocol, they are not merely a collection of HTTP requests. The difference lies in their architectural style and guiding principles:

- **HTTP is the Protocol**: HTTP defines how messages are formatted and transmitted over the web, and how web servers and browsers should respond to various commands.

- **REST is an Architectural Style**: REST is a set of constraints and principles applied to the design of web services, using HTTP for communication. It is a way of leveraging HTTP actions to make them meaningful in terms of CRUD operations.

- **REST APIs are Designed for Resource Manipulation**: RESTful services are characterized by their approach to resource handling, adhering to a set of principles that make the web services scalable, simple, and modular.

## Creating HTTP Requests in Python

### Creating an Endpoint Server with Flask

To handle HTTP requests in a RESTful manner, we need to create an endpoint server. This server will listen for HTTP requests (like GET and POST) and respond appropriately. The Flask module in Python is an excellent tool for this purpose because it's lightweight and easy to use, yet powerful enough for complex tasks.

Installing Flask Library:

```python
pip install Flask
```

Create the Flask App:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

data: str = "value"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({'data': data})

@app.route('/data', methods=['POST'])
def post_data():
    global data
    request_data = request.get_json()  # Get JSON data from request
    if 'data' in request_data:
        data = request_data['data']  # Update the global data variable
        return jsonify({'message': 'Data updated successfully', 'new_data': data})
    else:
        return jsonify({'message': 'No data field in request'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

In this application:
- The GET /users endpoint returns a list of users.
- The POST /users endpoint adds a new user to the users dictionary.

Running the Flask Application:
- Execute the script to start the Flask server.
- By default, Flask will run on http://127.0.0.1:5000/.

### Creating HTTP Requests in Python Using requests Module

Python's `requests` library is a popular choice for HTTP requests due to its simplicity and ease of use.

Installing Requests Library:

```python
pip install requests
```

#### Making a GET Request

To retrieve data (users) from your Flask server:

```python
import requests

response = requests.get('http://127.0.0.1:5000/users')
if response.status_code == 200:
    print("Users:", response.json())
else:
    print("Failed to fetch users")
```

### Making a POST Request

To add a new user:

```python
new_user = {"name": "Jane Doe", "email": "jane@example.com"}

response = requests.post('http://127.0.0.1:5000/users', json=new_user)
if response.status_code == 201:
    print("User added:", response.json())
else:
    print("Failed to add user")
```

## Common Status Codes

HTTP status codes are standardized responses in the Hypertext Transfer Protocol (HTTP) used to indicate the result of a client's request to a server. These status codes are part of the HTTP response sent by the server in response to a request made by the client. They are grouped into several classes, indicated by the first digit, and can provide quick insight into the outcome of the request. Here's an overview of the most common HTTP status codes:

### 1xx: Informational Responses

- **100 Continue**: The initial part of a request has been received, and the client should continue with the request or ignore it if it is already finished.

### 2xx: Success

- **200 OK**: The standard response for successful requests. The actual response will depend on the request method used.
- **201 Created**: The request has been fulfilled, and a new resource has been created.
- **202 Accepted**: The request has been accepted for processing, but the processing has not been completed.
- **204 No Content**: The server successfully processed the request, but is not returning any content.

### 3xx: Redirection

- **301 Moved Permanently**: The requested resource has been permanently moved to a new URL provided by the Location header.
- **302 Found**: The requested resource resides temporarily under a different URL.
- **304 Not Modified**: Indicates that the resource has not been modified since the last request.

### 4xx: Client Errors

- **400 Bad Request**: The server cannot or will not process the request due to a client error (e.g., malformed request syntax).
- **401 Unauthorized**: Authentication is required, and the client has failed to provide it.
- **403 Forbidden**: The client does not have permission to access the requested resource.
- **404 Not Found**: The requested resource could not be found.
- **405 Method Not Allowed**: The request method is not supported for the requested resource.

### 5xx: Server Errors

- **500 Internal Server Error**: A generic error message indicating an unexpected condition encountered by the server.
- **501 Not Implemented**: The server does not support the functionality required to fulfill the request.
- **503 Service Unavailable**: The server is currently unable to handle the request due to temporary overloading or maintenance.

## Error Handling in RESTful APIs

TODO
TODO
TODO

## Authentication and Authorization

TODO
TODO
TODO

- Basic Authentication
- Token-Based Authentication (JWT)

## HTTPS Security Practices

TODO
TODO
TODO

## API Versioning

TODO
TODO
TODO

## Rate Limiting

TODO
TODO
TODO

## Representational State Transfer (REST) vs. Other Architectures

TODO
TODO
TODO