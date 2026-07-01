#!/usr/bin/env python3
"""
SIMPLE PORT SCANNER
====================
A beginner cybersecurity project.

WHAT THIS DOES:
A "port" is like a numbered door on a computer that a service (web server,
SSH, FTP, etc.) can listen on. This tool tries to connect to a range of
ports on a target machine and tells you which ones are OPEN (something is
listening) and which are CLOSED.

LEGAL WARNING:
Only scan computers you own or have explicit permission to scan
(e.g. your own laptop using 127.0.0.1, or a machine you control).
Scanning systems you don't own without permission can be illegal.
"""

import socket
from datetime import datetime


def scan_port(target_ip, port, timeout=0.5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((target_ip, port))
    sock.close()
    return result == 0


def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "unknown"


def run_scan(target_ip, start_port, end_port):
    print("=" * 50)
    print(f"Starting scan on target: {target_ip}")
    print(f"Scanning ports {start_port} to {end_port}")
    print(f"Time started: {datetime.now()}")
    print("=" * 50)

    open_ports = []
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            service = get_service_name(port)
            print(f"[OPEN]   Port {port:<6} -> {service}")
            open_ports.append(port)

    end_time = datetime.now()
    duration = end_time - start_time

    print("=" * 50)
    print("Scan complete.")
    print(f"Time taken: {duration}")
    if open_ports:
        print(f"Open ports found: {open_ports}")
    else:
        print("No open ports found in this range.")
    print("=" * 50)


if __name__ == "__main__":
    print("SIMPLE PORT SCANNER - For educational use on systems you own only.\n")

    target = input("Enter target IP address (e.g. 127.0.0.1 for your own machine): ").strip()
    start = input("Enter start port (e.g. 1): ").strip()
    end = input("Enter end port (e.g. 1024): ").strip()

    try:
        start_port = int(start)
        end_port = int(end)
    except ValueError:
        print("Ports must be numbers. Exiting.")
        exit(1)

    try:
        socket.gethostbyname(target)
    except socket.gaierror:
        print("Could not resolve that target. Check the IP/hostname and try again.")
        exit(1)

    run_scan(target, start_port, end_port)
