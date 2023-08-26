#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics
"""

import sys
import signal

# Initialize variables to store metrics
total_size = 0
status_count = {}


def signal_handler(sig, frame):
    """Handler function for keyboard interruption (CTRL + C) """
    print_statistics()
    sys.exit(0)


def print_statistics():
    """Printe the metrics and reset variable """
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_count.keys()):
        print(f"{status_code}: {status_count[status_code]}")
    print()


signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        if len(parts) >= 7:
            ip, date, request, status_code, file_size = \
                    parts[0], parts[3], parts[5], parts[6], parts[7]

            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in (200, 301, 400, 401, 403, 404, 405, 500):
                    if status_code not in status_count:
                        status_count[status_code] = 0
                    status_count[status_code] += 1

            if file_size.isdigit():
                total_size += int(file_size)

            line_count += 1

            if line_count == 10:
                print_statistics()
                line_count = 0

except KeyboardInterrupt:
    print("\nKeyboardInterrupt received. Printing current statistics:")
    print_statistics()
