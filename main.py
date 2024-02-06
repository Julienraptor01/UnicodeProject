def add_front_spacer(file):
    """
    Adds a front spacer to the file.

    This function writes a line of 50 hyphens to the file, followed by a newline character.
    """
    file.write("| ")


def add_spacer(file):
    """
    Adds a spacer to the file.

    This function writes a line of 50 hyphens to the file, followed by a newline character.
    """
    file.write(" - ")


def add_back_spacer(file):
    """
    Adds a back spacer to the file.

    This function writes a line of 50 hyphens to the file, followed by a newline character.
    """
    file.write(" |")


def end_line(file):
    """
    Ends the line in the file.

    This function writes a newline character to the file.
    """
    file.write("\n")


def main(as_is=True):
    """
    Writes Unicode characters and their corresponding codes to a file.

    This function iterates over the range of valid Unicode characters, and for each character,
    it writes a line to the file in the format: "| U+{code} - {character} |".

    If the character is not valid, it writes "N/A" instead of the character.

    :param as_is: A boolean value indicating whether EOL characters should be written as-is or as "CR" and "LF".
    """
    with open("unicode_characters.txt", "w", encoding="utf-8-sig", newline="\n") as file:
        with open("unicode_characters.txt", "ab") as file_binary:
            file.close()
            file = open("unicode_characters.txt", "a", encoding="utf-8-sig", newline="\n")
            for i in range(0x10FFFF + 1):
                add_front_spacer(file)
                file.write(f"U+{i:06X}")
                add_spacer(file)
                try:
                    if i == 0x0D and not as_is:
                        file.write("CR")
                    elif i == 0x0A and not as_is:
                        file.write("LF")
                    else:
                        file.write(f"{chr(i)}")
                except UnicodeEncodeError:
                    file.flush()
                    file_binary.write(chr(i).encode("utf-8", "surrogatepass"))
                    file_binary.flush()
                add_back_spacer(file)
                end_line(file)


if __name__ == '__main__':
    main(input("Write EOL characters as-is ? (Y/n) ").lower() == "y")
