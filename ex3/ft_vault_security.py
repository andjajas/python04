#!/usr/bin/env python3
def secure_archive(
    file_name: str,
    action: str = "r",
    content: str = ""
     ) -> tuple[bool, str]:
    try:
        if action != "r" and action != "w":
            raise ValueError("action needs to be \"r\" or \"w\"")
        with open(file_name, action) as file:
            if action == "r":
                read_file = file.read()
                return (True, read_file)
            elif action == "w":
                file.write(content)
                return (True, "Content successfully written to file")
            else:
                return (False, "Unknown error")
    except (ValueError, FileNotFoundError, PermissionError) as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("foo.txt", "r"))
    print("using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("nopermission.txt", "r"))
    print("using 'secure_archive' to read from a regular file:")
    previous_tuple = secure_archive("ancient_fragment.txt", "r")
    print(previous_tuple)
    print("using 'secure_archive' to write previous content to a new file:")
    previous_bool, previous_str = previous_tuple
    write_return = secure_archive("new_file.txt", "w", previous_str)
    print(write_return)
