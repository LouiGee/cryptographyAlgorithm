#1


# Open the file in read mode
with open("lg565/cexercise1.txt", "r") as file:
    # Read the content of the file
    ciphertext = file.read()


# Function to decode a Caesar cipher
def decode_caesar_cipher(ciphertext, shift):
    decoded_text = ""

    for char in ciphertext:
        
        offset = ord('A')
            
        # Shift the character forward and wrap around the alphabet
        decoded_char = chr((ord(char) - offset + shift) % 26 + offset)
        decoded_text += decoded_char

    return decoded_text


plainTexts = {}

for i in range(0, 27):
    plainTexts[f"Shift_{i}"] = decode_caesar_cipher(ciphertext,i)


#2


# Open the file in read mode
with open("lg565/cexercise2.txt", "r") as file:
    # Read the content of the file
    ciphertext = file.read()


# Function to decode Vigenere cipher 
def decode_Vigenere_cipher(ciphertext, key):
    decoded_text = ""

    for i in range(len(ciphertext)):
        
        offset = ord('A')
            
        # Shift the character forward and wrap around the alphabet
        decoded_char = chr(((ord(ciphertext[i]) - ord(key[i]))) % 26 + offset)
        decoded_text += decoded_char

    return decoded_text



key = 'TESSOFTHEDURBERVILLES'

def generate_key(text, key):
    key = list(key)
    if len(key) < len(text):
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

generated_key = generate_key(ciphertext, key)


plain_text = decode_Vigenere_cipher(ciphertext,generated_key)


#3

    






    



