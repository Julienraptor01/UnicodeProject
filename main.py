def main():
    """
    Writes Unicode characters and their corresponding codes to a file.

    This function iterates over the range of valid Unicode characters, and for each character,
    it writes a line to the file in the format: "| U+{code} - {character} |".

    If the character is not valid, it writes "N/A" instead of the character.
    """
    with open("unicode_characters.txt", "w", encoding="utf-8-sig", newline="\n") as file:
        for i in range(0x10FFFF + 1):
            try:
                file.write(f"| U+{i:06X} - {chr(i)} |\n")
            except UnicodeEncodeError:
                file.write(f"| U+{i:06X} - N/A |\n")


if __name__ == '__main__':
    main()
