#!/usr/bin/env python3
import sys
import typing


def ancient_data(data: str) -> None:
    print(f"Accessing file '{data}'")
    try:
        f: typing.IO[str] = open(data, "r")
        content = f.read()
        print(f"---\n\n{content}\n\n---")
        print(f"File '{data}' closed.")
        print("Transform data:")
        new_content: list[str] = content.rstrip().split("\n")
        mod_content: list[str] = [line + "#" for line in new_content]
        merge_content = "\n".join(mod_content)
        f.close()
        print(f"---\n\n{merge_content}\n\n---")
        new_file: str = input("Enter new file name (or empty): ")
        if not new_file:
            print("Not saving data.")
        else:
            f2 = open(new_file, "w")
            f2.write(merge_content)
            print(f"Saving data to '{new_file}'")
            print(f"Data saved in file '{new_file}")
            f2.close()

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{data}':", e)


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) == 2:
        ancient_data(sys.argv[1])
    else:
        print("Usage: ft_ancient_text.py <file>")
