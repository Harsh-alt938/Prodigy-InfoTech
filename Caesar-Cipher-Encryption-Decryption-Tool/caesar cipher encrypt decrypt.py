def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if direction == "encrypt":
                new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            elif direction == "decrypt":
                new_char = chr(((ord(char.lower()) - 97 - shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

# User input
text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
direction = input("Choose 'encrypt' or 'decrypt': ").lower()

# Perform encryption/decryption
if direction in ["encrypt", "decrypt"]:
    processed_text = caesar_cipher(text, shift, direction)
    print(f"The {direction}ed text is: {processed_text}")
else:
    print("Invalid operation. Please choose 'encrypt' or 'decrypt'.")
