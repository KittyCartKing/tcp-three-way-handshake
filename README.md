# 🤝 TCP Three-Way Handshake Simulation

---

## 📖 What is a Three-Way Handshake?

The TCP three-way handshake is the process used to establish a reliable connection between a client and server before data transmission begins.

### 🔄 The Process

```
┌─────────────────────────────────────────────────────────────────┐
│                    TCP THREE-WAY HANDSHAKE                      │
└─────────────────────────────────────────────────────────────────┘

     ┌──────────┐                              ┌──────────┐
     │  CLIENT  │                              │  SERVER  │
     └────┬─────┘                              └────┬─────┘
          │                                         │
          │   ┌─────────────────────────────┐       │
          │   │  STEP 1: SYN                │       │
          │   │  "Hey, I want to connect!"  │       │
          │──────────────────────────────────────►  │
          │   │  seq = x                    │       │
          │   └─────────────────────────────┘       │
          │                                         │
          │   ┌─────────────────────────────┐       │
          │   │  STEP 2: SYN-ACK            │       │
          │   │  "OK! I acknowledge you"    │       │
          │  ◄──────────────────────────────────────│
          │   │  seq = y, ack = x+1         │       │
          │   └─────────────────────────────┘       │
          │                                         │
          │   ┌─────────────────────────────┐       │
          │   │  STEP 3: ACK                │       │
          │   │  "I acknowledge you too!"   │       │
          │──────────────────────────────────────►  │
          │   │  ack = y+1                  │       │
          │   └─────────────────────────────┘       │
          │                                         │
          │   ┌─────────────────────────────┐       │
          │   │  ✅ CONNECTION ESTABLISHED  │       │
          │   └─────────────────────────────┘       │
     ┌────┴─────┐                              ┌────┴─────┐
     │  CLIENT  │                              │  SERVER  │
     └──────────┘                              └──────────┘
```

---

## 🎯 Quick Summary

| Step | Direction | Flags | Message |
|:----:|:---------:|:-----:|:--------|
| 1️⃣ | Client → Server | `SYN` | "I want to connect" |
| 2️⃣ | Server → Client | `SYN-ACK` | "OK, I acknowledge you" |
| 3️⃣ | Client → Server | `ACK` | "I acknowledge you too" |

---

## 📋 Requirements

| Requirement | Version |
|:------------|:--------|
| 🐍 Python | 3.x |
| 💻 OS | Windows / macOS / Linux |
| 🌐 Network | Localhost (127.0.0.1) |

---

## 🚀 How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/KittyCartKing/tcp-three-way-handshake.git
cd tcp-three-way-handshake
```

### Step 2: Open Two Terminal Windows

```
┌─────────────────────┐    ┌─────────────────────┐
│     TERMINAL 1      │    │     TERMINAL 2      │
│      (Server)       │    │      (Client)       │
│                     │    │                     │
│  $ python server.py │    │  $ python client.py │
│                     │    │                     │
└─────────────────────┘    └─────────────────────┘
```

### Step 3: Start the Server First

```bash
python server.py
```

### Step 4: Run the Client

```bash
python client.py
```

### Step 5: Watch the Magic! ✨

---

## 📺 Example Output

### 🖥️ Server Terminal

```
//~~ Server Side ~~//
Waiting for client connection...

[1] SYN/seq=1234
[3] ACK/seq=1568

========================================
✅ CONNECTION ESTABLISHED!
========================================

Three-way handshake complete.
Server is now connected to client.
```

### 💻 Client Terminal

```
//~~ Client Side ~~//
Connecting to server...

[2] SYN/seq=1567 ACK/seq=1235

========================================
✅ CONNECTION ESTABLISHED!
========================================

Three-way handshake complete.
Client is now connected to server.
```
### Snapshot of ouput on Windows machine

<img width="493" height="111" alt="Server_Client output" src="https://github.com/user-attachments/assets/62845f4f-69d8-4125-9952-6da68d0129e0" />




### 📊 What Just Happened?

```
┌─────────────────────────────────────────────────────────────────┐
│ TIMELINE                                                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CLIENT                           SERVER                        │
│    │                                │                           │
│    │  ──── [1] SYN/seq=1234 ────►   │  Server receives SYN     │
│    │                                │                           │
│    │  ◄─ [2] SYN/seq=1567 ──────   │  Server sends SYN-ACK    │
│    │        ACK/seq=1235            │                           │
│    │                                │                           │
│    │  ──── [3] ACK/seq=1568 ────►   │  Server receives ACK     │
│    │                                │                           │
│    │       ✅ CONNECTED! ✅          │                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ How It Works

### 🖥️ Server (server.py)

```
┌────────────────────────────────────────┐
│            SERVER WORKFLOW             │
├────────────────────────────────────────┤
│                                        │
│  1. 🔌 Create socket                   │
│          │                             │
│          ▼                             │
│  2. 📍 Bind to port 1337               │
│          │                             │
│          ▼                             │
│  3. 👂 Listen for connections          │
│          │                             │
│          ▼                             │
│  4. ⏳ Wait for client (accept)        │
│          │                             │
│          ▼                             │
│  5. 📥 Receive SYN                     │
│          │                             │
│          ▼                             │
│  6. 📤 Send SYN-ACK                    │
│          │                             │
│          ▼                             │
│  7. 📥 Receive ACK                     │
│          │                             │
│          ▼                             │
│  8. ✅ Connection established!         │
│                                        │
└────────────────────────────────────────┘
```

### 💻 Client (client.py)

```
┌────────────────────────────────────────┐
│            CLIENT WORKFLOW             │
├────────────────────────────────────────┤
│                                        │
│  1. 🔌 Create socket                   │
│          │                             │
│          ▼                             │
│  2. 🔗 Connect to server               │
│          │                             │
│          ▼                             │
│  3. 📤 Send SYN                        │
│          │                             │
│          ▼                             │
│  4. 📥 Receive SYN-ACK                 │
│          │                             │
│          ▼                             │
│  5. 📤 Send ACK                        │
│          │                             │
│          ▼                             │
│  6. ✅ Connection established!         │
│                                        │
└────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
tcp-three-way-handshake/
│
├── 🖥️  server.py      # Server-side implementation
├── 💻  client.py      # Client-side implementation
├── 📖  README.md      # Project documentation
└── 🚫  .gitignore     # Git ignore file
```

---

## ⚠️ Important Notes

> **🪟 Linux Users**
>
> Change `os.system("cls")` to `os.system("clear")` in both files.

> **🔌 Port Already in Use?**
>
> If port 1337 is busy, change the port number in both files to something else (e.g., 1338).

> **📶 Connection Refused?**
>
> Make sure you start the server BEFORE the client!

---

## 🧠 Key Concepts

| Term | Meaning |
|:-----|:--------|
| **SYN** | Synchronize - Request to start connection |
| **ACK** | Acknowledge - Confirm receipt |
| **SYN-ACK** | Both flags - "I got yours, here's mine" |
| **Sequence Number** | Unique identifier for tracking packets |
| **Socket** | Endpoint for network communication |
| **Port** | Virtual door for network traffic |
| **Localhost** | Your own computer (127.0.0.1) |

---

## 📚 Learning Resources

| Resource | Link |
|:---------|:-----|
| 🐍 Python Socket Docs | [Link](https://docs.python.org/3/library/socket.html) |
| 🎥 TCP Explained - YouTube | [Search](https://www.youtube.com/results?search_query=tcp+three+way+handshake) |

---

## 🙏 Acknowledgments

Client/server code adapted from [@dawnl3ss](https://github.com/dawnl3ss). Thanks for sharing!

---

## 👤 Author

**Ian Richards** ([@KittyCartKing](https://github.com/KittyCartKing))

🛡️ Learning Security Engineering

---

## 🌟 Part of My Journey

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   🎯 Goal: Become a Security Engineer                          │
│                                                                 │
│   📚 Learning: 90+ Security Questions Framework                │
│                                                                 │
│   ✅ Question 1: What is a three-way handshake? [COMPLETED]    │
│                                                                 │
│   🚀 Next: How do cookies work?                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

<p align="center">
Making progress everyday.

</p>


