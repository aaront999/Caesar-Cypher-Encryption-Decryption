# Caesar cipher Encryption/Decryption Project 

text = input("Type in a text to encrypt: ")
shiftByThree = 3

def CaesarCypher(input, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in input:
        if not char.isalpha(): # Append any non-letter character to the message
            result += char
        else:
            is_upper = char.isupper() # Determine if character is uppercase or lowercase
            index = alphabet.find(char.lower()) 
            new_index = (index + shift) % len(alphabet)
            encrypt_char = alphabet[new_index]
            if is_upper:
                encrypt_char = encrypt_char.upper()  # Preserve original case
            result += encrypt_char

    return result

# Defining encrypt/decrypt function for better readability
def encrypt(message):
    return CaesarCypher(message, shiftByThree)

def decrypt(message):
    return CaesarCypher(message, -shiftByThree)

# test cases
# output results for ENCRYPTION
print(f'\nDecrypted text: {text}')
print('_________________________')
encryption = encrypt(text)
print(f'encryption: {encryption}\n')

print('////////////////////////////')

# output results for DECRYPTION
print(f'\nEncrypted text: {encryption}')
decryption = decrypt(encryption)
print('_________________________')
print(f'decryption: {decryption}')
