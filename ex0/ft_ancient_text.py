#!/usr/bin/env python3
import sys
import typing


def ancient_data(_) -> None:
    try:
        f = open(sys.argv[1], "r")
    except FileNotFoundError or PermissionError as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        ancient_data(sys.argv[1])
    else:
        print("Usage: ft_ancient_text.py <file>")
