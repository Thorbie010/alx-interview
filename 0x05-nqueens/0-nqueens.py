#!/usr/bin/python3
""" Script for N-queen. """
import sys


def n_queen(hor, ver, dia, x, y):
    """ Function that solves the N queens problem. """
    if (x > y):
        ver.append(hor[:])
        return ver

    for i in range(y + 1):
        if x == 0 or ([x - 1, i - 1] not in hor and
                      [x - 1, i + 1] not in hor and
                      i not in dia):
            if x > 1:
                src = 0
                for j in range(2, x + 1):
                    if ([x - j, i - j] in hor) or ([x - j, i + j] in hor):
                        src = 1
                        break
                if src:
                    continue
            hor.append([x, i])
            dia.append(i)
            n_queen(hor, ver, dia, x + 1, y)
            dia.pop()
            hor.pop()

    return ver


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        y = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)

    if not isinstance(y, int):
        print("N must be a number")
        exit(1)

    elif y < 4:
        print("N must be at least 4")
        exit(1)

    n_queen_ver = n_queen([], [], [], 0, y - 1)
    for x in n_queen_ver:
        print(x)
