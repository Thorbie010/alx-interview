#!/usr/bin/python3

import sys

def print_metrics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")

def process_line(line, total_size, status_counts):
    try:
        parts = line.split()
        if len(parts) >= 7 and parts[5] == '"GET' and parts[6].startswith("/projects/"):
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

        return total_size, status_counts
    except (ValueError, IndexError):
        # Skip lines with incorrect format
        return total_size, status_counts

def main():
    total_size = 0
    status_counts = {}
    line_counter = 0

    try:
        for line in sys.stdin:
            total_size, status_counts = process_line(line.strip(), total_size, status_counts)
            line_counter += 1

            if line_counter == 10:
                print_metrics(total_size, status_counts)
                line_counter = 0

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
