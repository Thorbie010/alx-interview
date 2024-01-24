#!/usr/bin/python3
import sys

total_size = 0
status_counts = {}
line_counter = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) >= 7 and parts[5] == '"GET' and parts[6].startswith("/projects/"):
                file_size = int(parts[-1])
                status_code = int(parts[-2])

                total_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

                line_counter += 1

                if line_counter == 10:
                    print(f"File size: {total_size}")
                    for code in sorted(status_counts):
                        print(f"{code}: {status_counts[code]}")
                    print()
                    line_counter = 0

        except (ValueError, IndexError):
            # Skip lines with incorrect format
            pass

except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")
    sys.exit(0)
