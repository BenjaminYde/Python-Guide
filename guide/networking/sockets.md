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