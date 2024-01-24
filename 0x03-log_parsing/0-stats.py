#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics. """

from sys import stdin


status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
        }
size = 0


def compute_metric():
    """ Function that reads and computes stdin. """

    print("File size: {}".format(size))
    for key, val in sorted(status_codes.items()):
        if val > 0:
            print("{}: {}".format(key, val))


if __name__ == '__main__':
    try:
        for i, line in enumerate(stdin, 1):
            try:
                my_data = line.split()
                size += int(my_data[-1])
                if my_data[-2] in status_codes.keys():
                    status_codes[my_data[-2]] += 1
            except Exception:
                pass
            if not i % 10:
                compute_metric()

    except KeyboardInterrupt:
        compute_metric()
        raise
    compute_metric()
