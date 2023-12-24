# Sockets

## What are Sockets?

A socket is an endpoint for sending and receiving data across a network. It acts as a gateway for data flow between different processes, either on the same machine (Inter Process Communication or IPC) or across different machines (network sockets). In Unix-like systems, sockets are implemented similarly to files, enabling read-write operations over the network.

### Network Sockets

Network sockets abstract away the complexities of network communication. They're like handlers managing connections between devices over a network. Each socket is bound to a combination of an IP address and a port number, uniquely identifying a communication endpoint.

## Client-Server Socket Architecture

The client-server architecture is a widespread model for network communication where multiple clients request and receive services from a centralized server. In the context of socket programming, this architecture involves clients and servers communicating over a network using sockets.

### Server and Client

**Server**: A server is a program or device that provides a service to other programs or devices (clients). It listens for requests, processes them, and sends back responses.

**Client**: A client is a program or device that requests services from the server.

#### Communication Flow:

1. The server is started and is ready for clients to connect with.
2. Clients initiate communication by making requests to the server.
3. The server listens on a specific port for incoming requests, processes them, and sends back responses.

#### Handling Multiple Clients:

- Servers often handle multiple client connections simultaneously.
  - Techniques like multi-threading or non-blocking sockets are used to manage multiple connections.
- Stateless vs. Stateful:
  - **Stateless**: Each client request is treated as an independent transaction, not dependent on previous requests (e.g., HTTP).
  - **Stateful**: The server keeps track of the state of interaction with a client across multiple requests (e.g., FTP sessions).

### Use Cases

- **Web Applications**: Using HTTP/HTTPS for client-server communication.
- **Online Gaming**: Real-time data exchange between players and game servers.
- **Chat Applications**: Instant messaging between clients through a central server.

## Network Sockets: TCP and UDP

### TCP (Transmission Control Protocol)

TCP is one of the main protocols in the TCP/IP network suite. It's a connection-oriented, reliable protocol used primarily for transmitting data over the internet. When data is sent over a TCP connection, the receiver acknowledges receipt of the packets, and if any packet is lost, TCP retransmits it.

#### Key Features:

- **Connection-Oriented:** A connection is established between the sender and receiver before any data is transmitted.
- **Reliability**: Ensures all data is transmitted accurately and in order.
- **Error Checking**: Uses checksums to ensure data integrity.
- **Ordered Data Transfer**: Guarantees that data arrives in the same order it was sent.

#### How TCP Works

- **Three-Way Handshake**: TCP uses a three-way handshake process to establish a connection. This involves the exchange of SYN (synchronize) and ACK (acknowledge) packets.
- **Data Transfer**: Once the connection is established, data packets are sent. Each packet includes a sequence number for proper ordering.
- **Termination**: The connection is terminated using a FIN (finish) packet.

### UDP (User Datagram Protocol)

UDP is another core member of the TCP/IP suite. Unlike TCP, it is connectionless and does not guarantee reliable delivery of packets. It's a simpler, faster protocol used in situations where speed is more critical than reliability.

#### Key Features:

- **Connectionless**: No need to establish a connection before sending data.
- **Low Overhead**: No congestion control, flow control, or connection setup.
- **Unreliable**: Does not guarantee packet delivery, order, or error checking.
- **Efficient**: Ideal for situations where speed is more critical than accuracy.

#### How UDP Works

- **Packet Sending**: UDP packets, called datagrams, are sent independently. Each datagram is self-contained with no sequence numbers or acknowledgments.
- **No Error Recovery**: If a packet is lost, UDP does not resend it.

### Comparison Between TCP and UDP

| Feature        | TCP                                      | UDP                                           |
|----------------|------------------------------------------|-----------------------------------------------|
| **Reliability**    | High (with acknowledgments)              | Low (no acknowledgments)                      |
| **Connection**     | Connection-oriented                      | Connectionless                                |
| **Speed**          | Slower due to overhead                   | Faster due to minimal overhead                |
| **Data Integrity** | High (error checking and correction)     | Lower (no error correction)                   |
| **Use Case**       | Data that requires reliability and order | Real-time applications where speed is crucial |

## Creating a Server and Client

### Common Socket Methods

`socket()`

- **Purpose**: Creates a new socket, which is an endpoint for sending and receiving data.
- **Functionality**:
  - Non-blocking function
  - Initializes a socket with specified address family and type.
  - `AF_INET` for IPv4, `AF_INET6` for IPv6.
  - `SOCK_STREAM` for TCP (reliable, connection-oriented), `SOCK_DGRAM` for UDP (unreliable, connectionless).
- **Example**:
    ```python
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ```

`bind()`

- **Purpose**: Associates the socket with a specific network interface and port number.
- **Functionality**:
  - Non-blocking function
  - Binds a socket to an address (IP) and port, specifying where it should listen for incoming connections (server-side).
  - Essential for servers to set up a fixed endpoint.
- **Example**:
    ```python
    s.bind(('127.0.0.1', 8080))
    ```

`listen()`

- **Purpose**: Enables a server socket to accept incoming connections.
- **Functionality**:
  - Non-blocking. It sets the socket to listening mode but does not wait for connections.
  - Configures how many incoming connections the socket can queue.
  - Transitions the socket into a listening state, waiting for connection requests.
- **Example**:
    ```python
    s.listen()
    ```

`accept()`

- **Purpose**: Accepts an incoming connection request from a client.
- **Functionality**:
  - Blocking. It waits for an incoming connection and blocks the program flow until a connection is made.
  - Returns a new socket object representing the connection and a tuple with the client's address.
  - Used in a loop to handle multiple client connections (server-side).
- **Example**:
    ```python
    client_socket, addr = s.accept()
    ```

`connect()`

- **Purpose**: Initiates a connection to a remote server.
- **Functionality**:
-  Blocking in normal circumstances. It actively attempts to establish a connection  to the server's IP and port and blocks until the connection is established or fails.
  - Establishes a connection to a TCP server (client-side).
- **Example**:
    ```python
    s.connect(('127.0.0.1', 8080))
    ```

`send()`

- **Purpose**: Sends data through the socket to a connected peer.
- **Functionality**:
  - Blocking. It sends all data in bytes over the socket or an error occurs.
  - Ensures the data is sent, possibly calling the method multiple times if all data is not sent in one call.
- **Example**:
    ```python
    s.send(b'Hello, world')
    ```

`recv()`

- **Purpose**: Receives data from the socket.
- **Functionality**:
  - Blocking. It waits for data to be received. If no data is available, it blocks the execution until at least some data is received.
- **Example**:
    ```python
    data = s.recv(1024)
    ```

`close()`
- **Purpose**: Closes the socket, releasing the resources.
- **Functionality**:
  - Non-blocking. It closes the socket and returns immediately.
  - Terminates the connection in both directions.
  - Frees up the resources associated with the socket.
- **Example**:
    ```python
    s.close()
    ```

### Creating a Server

```python
# server.py
import socket

# create a socket
# AF_INET specifies the address family (IPv4 in this case).
# SOCK_STREAM indicates that it is a TCP socket.
HOST, PORT = '127.0.0.1', 65432
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the address & port
server_socket.bind((HOST, PORT))

# set in listen mode for incoming connections
server_socket.listen()

# wait for incomming connections
client_socket, addr = server_socket.accept()

# wait until received all data
request = client_socket.recv(1024)
data = request.decode("utf-8") # convert bytes to string
print(f"Server: Received: {data}")

# send message and terminate connection
client_socket.sendall("Terminating server...")
client_socket.close()

# close the socket (cleanup & terminate)
server_socket.close()
```

### Creating a Client

```python
# client.py
import socket

# create a socket
# AF_INET specifies the address family (IPv4 in this case).
# SOCK_STREAM indicates that it is a TCP socket.
HOST, PORT = '127.0.0.1', 65432
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the existing server socket
client_socket.connect((HOST, PORT))

# send message to the server
client_socket.sendall(b'Hello, world')

# wait until received message
request = client_socket.recv(1024)
data = request.decode("utf-8") # convert bytes to string
print(f"Client: Received: {data}")

print('Received', repr(data))

# close the socket (cleanup & terminate)
client_socket.close()
```

## Handling Multiple Client Connections

```python
import socket
import threading

# Function to handle each client connection
def handle_client(client_socket):
    try:
        # receive data
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.sendall("Received data!")
    finally:
        client_socket.close()

def run():
    # setup the server
    print("Server initializing on {}:{}".format(HOST, PORT))
    HOST, PORT = '127.0.0.1', 65432
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server listening...")

    # listen for connections
    try:
        while True:
            # wait until client connects
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            # start new thread to handle connection
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    finally:
        server_socket.close()

if __name__ == "__main__":
    run()
```

## Using asyncio For Network Communication

`asyncio` is a Python library that provides a framework for writing single-threaded concurrent code using coroutines, multiplexing I/O access using the async and await syntax.

## Streams 

Streams in `asyncio` provide an abstraction for working with network IO. They allow you to write asynchronous code for handling network connections, such as reading from and writing to sockets, without directly dealing with the lower-level details of the protocol.

Streams are particularly useful for developing network applications where you need to handle multiple connections efficiently.

### Core Concepts of asyncio Streams

The main classes used in `asyncio` streams are `StreamReader` and `StreamWriter`. 
`StreamReader` is used for reading data from a stream, while `StreamWriter` is for writing data to a stream.

`TCP` and `UDP`: asyncio supports both TCP (reliable, connection-oriented protocol) and UDP (unreliable, connectionless protocol) streams.

### Creating a TCP Server

You can use `asyncio.start_server` to create an asynchronous TCP server. This server will handle incoming connections and can read from and write to these connections.

Example:
```python
import asyncio
from asyncio import StreamReader, StreamWriter

async def server_handle_client(reader: StreamReader, writer: StreamWriter):
    # Wait for message from a client
    data = await reader.read(100)  # Read up to 100 bytes
    message = data.decode('utf8')
    address = writer.get_extra_info('peername')
    print(f"Server: Received {message} from {address}")

    # Send a response to the client
    print("Server: Sending response to client...")
    new_message = "Sever is termenating..."
    new_data = new_message.encode('utf8')
    writer.write(new_data)
    await writer.drain()

    # Close the connection
    writer.close()

async def main():
    server = await asyncio.start_server(server_handle_client, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())
```

In this example, asyncio.start_server is used to create a server that listens on localhost (`127.0.0.1`) on port `8888`. For each client connection, `server_handle_client` coroutine is called with `StreamReader` and `StreamWriter` instances.

### Creating a TCP Client

To create a TCP client that connects to a server, use `asyncio.open_connection`. This returns `StreamReader` and `StreamWriter` objects for communication with the server.

Example:


```python
import asyncio

async def tcp_echo_client():
    # Connect to the server
    await asyncio.sleep(1)  # Give the server time to start
    reader, writer = await asyncio.open_connection(addres, port)

    # Send a message to the server
    print("Client: Sending message...")
    message = 'Hello World!'
    writer.write(message.encode('utf8'))
    await writer.drain()

    # Receive a response
    data = await reader.read(100)
    print(f"Client: Reveived from Server: {data.decode('utf8')}")

    # Close the connection
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client())
```

In this client example, `asyncio.open_connection` is used to connect to the server running on `127.0.0.1:8888`. The client sends a message, waits for a response, and then closes the connection.