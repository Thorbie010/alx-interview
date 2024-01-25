#!/usr/bin/python3
"""Comment"""
import sys


if __name__ == "__main__":
    size = 0
    code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    for index, line in enumerate(sys.stdin, start=1):
        line_size = len(line.encode("utf-8"))
        size += line_size
        items = line.strip().split()
        key = int(items[7])
        code[key] += 1
        if index % 10 == 0:
            print("File size: {}".format(size))
            for k, v in code.items():
                if v > 0:
                    print("{}: {}".format(k, v))
