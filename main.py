def encrypt_text_file(input_file, output_file):
    """
    Encrypts the content of a text file using a predefined substitution cipher
    and writes the encrypted content to an output file.

    Args:
        input_file (str): The path to the input text file that needs to be encrypted.
        output_file (str): The path to the output text file where the encrypted content will be written.

    Returns:
        None
    """
    substitution = {
        "a": "s",
        "b": "b",
        "c": "d",
        "d": "f",
        "e": "k",
        "f": "h",
        "g": "x",
        "h": "c",
        "i": "e",
        "j": "y",
        "k": "t",
        "l": "v",
        "m": "w",
        "n": "l",
        "o": "u",
        "p": "q",
        "q": "p",
        "r": "r",
        "s": "j",
        "t": "i",
        "u": "o",
        "v": "m",
        "w": "n",
        "x": "a",
        "y": "z",
        "z": "g",
    }

    def encrypt_char(char):
        """
        Encrypts a single character using the substitution cipher.

        Args:
            char (str): The character to encrypt.

        Returns:
            str: The encrypted character.
        """
        if char.islower():
            return substitution.get(char, char)
        elif char.isupper():
            return substitution.get(char.lower(), char).upper()
        else:
            return char

    with open(input_file, "r") as file:
        text = file.read()

    encrypted_text = "".join(encrypt_char(c) for c in text)

    with open(output_file, "w") as file:
        file.write(encrypted_text)


input_file = "encrypted_book.txt"
output_file = "decrypted.txt"
encrypt_text_file(input_file, output_file)
