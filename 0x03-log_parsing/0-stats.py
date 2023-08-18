#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics
"""
import sys
import signal


def signal_handler(signal, frame):
    """Defines a signal handler to catch CTRL + C """
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                 403: 0, 404: 0, 405: 0, 500: 0}


def print_metrics():
    """Define a helper function  to print the metrics"""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


line_count = 0
for line in sys.stdin:
    try:
        ip, _, date, request, status, size = line.split(" ")
        method, path, protocol = request.split(" ")
        size = int(size)
        status = int(status)
    except ValueError:
        continue

    total_size += size
    if status in status_counts:
        status_counts[status] += 1

    line_count += 1
    if line_count % 10 == 0:
        print_metrics()
