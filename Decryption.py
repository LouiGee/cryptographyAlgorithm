# Open the file in read mode
with open("tess26.txt", "r") as file:
    # Read the content of the file
    text = file.read()


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


if plain_text in text:
    print("The extract exists in the text.")
else:
    print("The extract does not exist in the text.")




#3

# Open the file in read mode
with open("lg565/cexercise3.txt", "r") as file:
    # Read the content of the file
    ciphertext = file.read()


from collections import Counter

def caesar_shift(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

def frequency_analysis(segment):
    frequencies = Counter(segment)
    most_common_char = max(frequencies, key=frequencies.get)
    # Assuming 'E' is the most common letter in plaintext (English)
    shift = (ord(most_common_char) - ord('E')) % 26
    return shift

def divide_text(text, key_length):
    segments = [''] * key_length
    for i, char in enumerate(text):
        if char.isalpha():
            segments[i % key_length] += char
    return segments

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_shifts = [(ord(k) - ord('A')) for k in key.upper()]
    key_len = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = key_shifts[i % key_len]
            shift_base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            plaintext += char
    return plaintext


# Key length is known to be 6
key_length = 6
segments = divide_text(ciphertext, key_length)

# Determine key using frequency analysis
key = ""

for segment in segments:
    shift = frequency_analysis(segment)
    key += chr((ord('A') + shift) % 26)

print(f"Identified Key: {key}")

# Decrypt the ciphertext using the identified key
plaintext = vigenere_decrypt(ciphertext, key)
print(f"Decrypted Text: {plaintext}")
    




if plaintext in text:
    print("The extract exists in the text.")
else:
    print("The extract does not exist in the text.")





    



