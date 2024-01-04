import pyperclip

def encrypt(message, key):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(message, key):
    return encrypt(message, -key)

def main():
    action = input("Do you want to (e) encrypt or (d) decrypt? > ").lower()

    if action not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' or 'd'.")
        return

    key = int(input("Please enter the key (0 to 25) to use. > "))
    if not 0 <= key <= 25:
        print("Invalid key. Please enter a key between 0 and 25.")
        return

    message = input("Enter the message. > ")

    if action == 'e':
        result = encrypt(message, key)
        print(f"Encrypted text: {result}")
    else:
        result = decrypt(message, key)
        print(f"Decrypted text: {result}")

    pyperclip.copy(result)
    print("Full text copied to clipboard.")

if __name__ == "__main__":
    main()
