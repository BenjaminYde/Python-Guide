# Introduction to Networking

Networking involves the interconnection of multiple devices (known as hosts) to transmit, exchange, and receive data and resources. This interconnection can be achieved through wired or wireless means and enables devices to communicate over various distances.

## Networking Hardware

### Internet Service Providers (ISPs)

- **Function**: ISPs are companies that provide individuals and organizations access to the Internet.

- **Services**: Beyond just internet access, many ISPs also offer related services such as web hosting, email hosting, and domain registration.

- **Connectivity Methods**: They use various technologies to deliver internet connectivity, including DSL (Digital Subscriber Line), cable modem, fiber optics, satellite, and wireless connections.

### Modems

- **Primary Function**: A modem (short for modulator-demodulator) is a device that a acts as a translator between the digital world of computers and the analog world of cable networks.
  
- **ISP Connection**: The modem connects a user's local network to their Internet Service Provider (ISP). It serves as the initial entry point to the internet from a home or office network.

### Routers

- **Function**: Routers are devices that route data packets between different networks. They determine the best path for data to travel across networks to reach their destination.

- **Features**: Routers typically include features like NAT, DHCP services, and firewall protection.

### Switches and Hubs

- **Function**: Switches are used within a network to connect various devices like computers, printers, and servers, creating a local area network (LAN).

- **Types**: Managed and unmanaged switches, with the former offering greater control over network traffic.

**Hub**: A basic networking device that connects multiple Ethernet devices, making them act as a single network segment. When a hub receives data, it sends it to all connected devices, regardless of the intended recipient.

### Wireless Access Points (WAPs)

- **Function**: WAPs allow wireless-capable devices to connect to a wired network using Wi-Fi or Bluetooth.
  
- **Deployment**: Used in both home and business networks to expand wireless network coverage.

### Network Interface Cards (NICs)

- **Function**: A hardware component, either integrated into the motherboard or added as an expansion card, that enables a computer or device to connect to a network.

- **Types**: Different NICs are available for wired (Ethernet NIC) and wireless (Wi-Fi NIC) connections.

![](./_img/network.png)

### Network Cabling and Wireless Technology

#### Ethernet Cables (Twisted Pair Cables):

- **Cat5, Cat5e**: Supports up to 1 Gbps; Cat5e reduces interference.
- **Cat6, Cat6a**: Higher performance, up to 10 Gbps, with Cat6a supporting longer distances.
- **Cat7**: High frequency, supporting 10 Gbps over 100 meters.
- **Usage**: Common in local area networks (LANs) for connecting computers, routers, and switches.

#### Fiber Optic Cables:

- **Function**: Use light to transmit data, offering high speeds and long-distance transmission.
- **Types**:
  - **Single-mode fiber**: For long-distance, high-speed transmission, suitable for WANs.
  - **Multi-mode fiber**: For shorter distances, used in LANs.
- **Advantages**: High bandwidth, long-distance capability, and immunity to electromagnetic interference.
- **Applications**: Ideal for backbone networks and data centers where high data rates are required.

#### Coaxial Cables:

- **Design**: Central metal conductor, insulator, metal shield, and plastic covering.
- **Use**: Common for cable TV and internet services.

#### Wi-Fi Standards

- **Explanation**: Wi-Fi standards are set by the IEEE (Institute of Electrical and Electronics Engineers) and include 802.11a, b, g, n, ac, and ax.
- **Differences**: Each standard differs in terms of speed, range, frequency, and capacity, with newer standards offering improvements over the previous ones. For example, 802.11ac provides faster speeds and better range than 802.11n.

## Network Types

### Local Area Network (LAN)

- **Definition**: A LAN connects computers and devices within a relatively small and specific area like a home, office, or building. 
- **Characteristics**: 
  - High data transfer rates.
  - Usually owned, controlled, and managed by a single person or organization.
  - Networking devices used include routers, switches, and hubs.
  - Common technologies: Ethernet for wired LANs, Wi-Fi for wireless LANs.

### Wide Area Network (WAN)

- **Definition**: A WAN covers a broader geographical area, often comprising multiple cities, countries, or even continents. For example, businesses with many international branch offices use a WAN to connect office networks together. The world’s largest WAN is the internet because it is a collection of many international networks that connect to each other.
- **Characteristics**:
  - Connects multiple LANs, typically through the internet.
  - Slower data transfer rates compared to LANs due to the larger distances.
  - Usually owned and managed by multiple organizations or service providers.
  - Common uses include enterprise networks, government networks, and the internet itself.

### Metropolitan Area Network (MAN)

- **Definition**: A MAN spans a larger area than a LAN but is usually confined to a city or a metropolitan area.
- **Characteristics**:
  - Designed to extend over an entire city or metropolitan area.
  - Often used to connect multiple LANs within a city to share resources or for internet connectivity.
  - Higher capacity than LAN and typically operated by a single entity or service provider.

### Virtual Private Network (VPN)

- **Definition**: A VPN extends a private network across a public network, enabling users to send and receive data as if their devices were directly connected to the private network.
- **Characteristics**:
  - Provides secure and encrypted connections for greater privacy.
  - Allows remote users secure access to their organization's network.
  - Commonly used for secure communications, especially for remote work.

### Virtual LANs (VLANs)

- **Definition**: A VLAN is a subcategory of LAN which groups together a collection of devices from different physical LANs to form a single broadcast domain.
- **Characteristics**:
  - VLANs are configured through software rather than hardware, making them extremely flexible.
  - Enhances network efficiency and security by segmenting networks into smaller parts.
  - Useful in large organizations for separating different departments or types of traffic, like separating voice and data traffic.

## Data Transmission Methods:

In networking, data transmission methods are crucial in determining how information is distributed across the network. These methods include unicast, broadcast, and multicast, each serving different purposes based on the network's needs.

### Unicast

- **Definition**: Unicast is a one-to-one transmission method where data is sent from one sender to one specific receiver.
- **Characteristics**:
  - **Direct Communication**: Data packets are sent directly to a specific destination IP address.
  - **Efficiency in Point-to-Point Communication**: Ideal for direct communication between two devices, like a client-server interaction.
  - **Traffic Control**: Since data is sent to a specific destination, unicast does not consume unnecessary network bandwidth.
- **Use Cases**: Common in most internet communications, such as web browsing, email, and file transfers.

### Broadcast

- **Definition**: Broadcast is a one-to-all transmission method where data is sent from one sender to all possible receivers within the network or a network segment.
- **Characteristics**:
  - **Network-Wide Communication**: Data packets are sent to all devices on the network.
  - **No Specific Destination Address**: The destination address is typically set as the broadcast address (e.g., `255.255.255.255` in IPv4), indicating all nodes.
  - **Best Effort Delivery**: There is no acknowledgment from the receiving devices.
- **Use Cases**: Used for network-wide announcements or services discovery, like DHCP requests to find a DHCP server when a device first connects to a network.

### Multicast

- **Definition**: Multicast involves sending data from one sender to multiple selected receivers simultaneously.
- **Characteristics**:
  - **Group Communication**: Data is sent to predefined groups of hosts. Each group is identified by a specific multicast IP address.
  - **Efficient Use of Bandwidth**: Multicast reduces the bandwidth usage by simultaneously delivering a single stream of data to multiple recipients.
  - **Controlled Reception**: Only devices that have joined the multicast group will receive the data.
- **Use Cases**: Common in streaming media (like IPTV), online gaming, and real-time applications where the same data needs to be delivered to multiple recipients.

### Network Protocols:

Rules and standards that define how data is transmitted and received.
Common protocols include TCP/IP, HTTP, FTP, and SMTP.
Network tunneling

## Understanding IP Addresses and Ports

### IP Addresses

An IP address is a unique identifier assigned to each device on a network.
There are two standards: IPv4 (e.g., 192.168.1.1) and IPv6 (e.g., 2001:db8::1).
IP addresses enable devices to locate and identify each other on a network.

Pv4 Exhaustion and IP Address Allocation
Challenges of IPv4 Exhaustion: Discussing the limitations of IPv4 and its impact on the Internet.
IP Address Allocation: How IP addresses are allocated and managed globally.

### Ports

A port is a virtual point where network connections start and end.
Ports are identified by numbers (e.g., HTTP traffic typically uses port 80).
They help differentiate between multiple services or applications running on the same device.

- What ports are available
- What ports can i use for my application
- How do i know if another app is using this port

### MAC Addresses

**Definition and Role**: Explain what MAC addresses are and how they uniquely identify network interfaces.
**Address Resolution Protocol (ARP)**: How MAC addresses are used in conjunction with IP addresses.

TODO: go more in depth

## IPv4 vs. IPv6

Differences and Advantages: Comparing IPv4 and IPv6, including addressing schemes, security features, and performance implications.
Transition Mechanisms: Strategies for transitioning from IPv4 to IPv6 networks.

### DNS and DHCP

Domain Name System (DNS): Translating domain names to IP addresses.
Dynamic Host Configuration Protocol (DHCP): Automatic assignment of IP addresses to devices on a network.

## Basic Network Security

Network security involves measures to protect data during transmission and includes:

Firewalls: Filtering incoming and outgoing network traffic.
Encryption: Encoding data to prevent unauthorized access.
Authentication Protocols: Ensuring only authorized users can access the network.
Common Threats: Types of network attacks (e.g., DDoS, MITM, packet sniffing).
Wi-Fi Security Protocols: Details about WEP, WPA, WPA2, and WPA3.

## Network Redundancy and Load Balancing

Designing Redundant Networks: Techniques to ensure network availability and fault tolerance.
Load Balancing Strategies: Methods for distributing network traffic across multiple servers.