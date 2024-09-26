# Real-Time Chat with Python (Client-Server)

## Description
This project implements a real-time chat system using Python, based on a client-server architecture. The system allows multiple clients to connect to a central server and communicate with each other in real-time. The server manages connections and message distribution, while the clients interact through a graphical user interface (GUI) built with Tkinter. The project uses **sockets** for network communication and **threading** to handle multiple clients concurrently.

## Features
- **Client-Server Architecture**: Clients connect to a central server that manages communication.
- **Real-time Messaging**: Messages are sent and received in real-time between clients.
- **Graphical User Interface (GUI)**: Clients use a user-friendly interface built with Tkinter.
- **Multi-client Support**: The server handles multiple clients simultaneously using threading.
- **Custom Commands**: Clients can use predefined commands like `/saludar`, `/despedirse`, and `/emoji` to send specific messages.
- **Threaded Message Reception**: The client can receive messages in the background while interacting with the chat.

## Technologies Used
- **Python**: Main programming language used to implement both client and server.
- **Tkinter**: Python's standard library for creating the graphical user interface (GUI) for the clients.
- **Socket**: Used for network communication between the client and the server.
- **Threading**: To handle multiple clients concurrently and to manage message reception in the background for each client.


## Installation

### Prerequisites
Make sure you have Python 3.x installed on your system. You can download Python from the official website [here](https://www.python.org/downloads/).

### Steps to Install
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/angela-mera/Real-Time-Chat-Client-Server-Model.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Real-Time-Chat-Client-Server-Model/Chat
   ```

3. Install any required Python libraries if not available:
   - For Tkinter (should be included with Python):
     ```bash
     sudo apt-get install python3-tk  # for Linux
     ```
   - For Windows users, Tkinter is typically installed with Python by default. If you encounter any issues, you can refer to the [Tkinter documentation](https://docs.python.org/3/library/tkinter.html).

4. Now the project is ready to run

## Usage

### Running the Server
1. Start the server by running the following command in the terminal:
   ```bash
   python3 server.py
   ```

2. The server will start listening for client connections on `localhost` at port `9099`. The terminal will show messages when clients connect and when messages are broadcasted.

### Running the Client
1. Open a new terminal window for each client.
2. Run the following command to start the client:
   ```bash
   python3 client.py
   ```
3. The client will prompt you to enter your name.
4. After entering your name, the GUI window will appear where you can send and receive messages.

### Commands Available for Clients
- **/saludar**: Sends a greeting to all clients.
- **/despedirse**: Sends a goodbye message.
- **/emoji**: Sends a smiley emoji.
- **/finalizar chat**: Disconnects the client from the chat and closes the window.

### Example Flow
1. Start the server in one terminal.
2. Run two or more clients in separate terminals, and connect them to the server.
3. The clients can send messages to each other, and they will appear in real-time on each connected client’s window.
4. Use custom commands like `/saludar` or `/emoji` to send predefined messages.

## Code Structure

```bash
Real-Time-Chat-Python-Client-Server/
│
├── client.py            # Client-side script with Tkinter GUI
├── server.py            # Server-side script to handle multiple clients
├── README.md            # Project documentation
└── LICENSE              # License for the project
```
- **client.py**: Contains the logic for connecting to the server, receiving and sending messages, and the Tkinter GUI for the chat interface.
- **server.py**: Manages multiple client connections, handles message broadcasting, and processes special commands.
  
