# Simple Port Scanner

A beginner Python project that scans a target system across a range of ports to check which ones are open. This is a basic technique used in cybersecurity to understand what services are exposed on a network.

## What It Does

A "port" is like a numbered door on a computer through which services (web servers, SSH, FTP, etc.) communicate. This tool checks a range of ports on a target machine and reports which ones are OPEN (actively listening) versus CLOSED.

## Built With

- Python 3
- socket (Python's built-in library for network connections)
- datetime (for tracking scan duration)

## How to Run

1. Clone or download this repository
2. Run the script:
3. Enter the target IP (use 127.0.0.1 to safely scan your own machine)
4. Enter a start port and end port (e.g. 1 to 1024)
5. View the results - open ports will be listed with their likely service name

## Note

This tool should only be used on systems you own or have permission to scan. Scanning systems without permission can be illegal.

## What I Learned

- How TCP connections and ports work
- Using Python's socket library to interact with networks
- Basics of security reconnaissance - checking what is exposed on a system
- Working with Linux terminal (Kali Linux) and Git/GitHub

## Sample Output
