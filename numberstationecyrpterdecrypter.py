import string

# Define the substitution cipher
alphabet = string.ascii_lowercase
cipher = {alphabet[i]: str(i) for i in range(26)}

def encrypt(message):
    """
    Encrypt a message by replacing each letter with its corresponding number.
    """
    encrypted_message = ""
    count = 0
    for letter in message:
        if letter in cipher:
            encrypted_message += cipher[letter]
            count += 1
            if count % 5 == 0:
                encrypted_message += " "
        else:
            encrypted_message += letter
    return encrypted_message.strip()

def decrypt(message):
    """
    Decrypt a message by replacing each number with its corresponding letter.
    """
    decrypted_message = ""
    i = 0
    while i < len(message):
        if message[i].isdigit():
            if i < len(message) - 1 and message[i+1].isdigit():
                num = int(message[i:i+2])
                if num < len(alphabet):
                    decrypted_message += alphabet[num]
                i += 2
            else:
                num = int(message[i])
                if num < len(alphabet):
                    decrypted_message += alphabet[num]
                i += 1
        else:
            if i == len(message) - 1:
                decrypted_message += message[i]
            else:
                i += 1
    return decrypted_message

# Prompt the user to enter a message
message = input("Enter a message to encrypt: ")

# Encrypt and decrypt the message
encrypted_message = encrypt(message)
decrypted_message = decrypt(encrypted_message)

# Print the results
print("Original message: ", message)
print("Encrypted message: ", encrypted_message)
print("Decrypted message: ", decrypted_message)
