#!/usr/bin/env python3
import sys
import typing


def ancient_data(data:str) -> None:
    try:
        f = open(data, "r")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{data}':", e)


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 2:
        ancient_data(sys.argv[1])
    else:
        print("Usage: ft_ancient_text.py <file>")
