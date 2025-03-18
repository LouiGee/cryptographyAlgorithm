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
        decoded_char = chr((ord(char) - offset - shift) % 26 + offset)
        decoded_text += decoded_char

    return decoded_text


plainTexts = {}

for i in range(0, 27):
    plainTexts[f"Shift_{i}"] = decode_caesar_cipher(ciphertext,i)
    
plainText1 = plainTexts["Shift_14"][:30]

if plainText1 in text:
    print("The extract exists in the text.")
else:
    print("The extract does not exist in the text.")


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


plainText2 = decode_Vigenere_cipher(ciphertext,generated_key)

plainText2 = plainText2[:30]

if plainText2 in text:
    print("The extract exists in the text.")
else:
    print("The extract does not exist in the text.")


#3



from collections import Counter

# Open the file in read mode
with open("lg565/cexercise3.txt", "r") as file:
    # Read the content of the file
    ciphertext = file.read()


# Function to divide ciphertext into groups based on key length
def divide_ciphertext(ciphertext, key_length=6):
    groups = [''] * key_length  # Create a list for each group

    for i, letter in enumerate(ciphertext):
        groups[i % key_length] += letter  # Assign letters to groups cyclically

    return groups

# Function to perform frequency analysis on each group
def frequency_analysis(groups):
    analysis = []
    for i, group in enumerate(groups):
        freq_count = Counter(group)  # Count letter occurrences
        sorted_freq = sorted(freq_count.items(), key=lambda x: x[1], reverse=True)  # Sort by frequency
        analysis.append((i + 1, sorted_freq))  # Store group number and frequencies
    return analysis

# Example ciphertext
key_length = 6

# Step 1: Divide ciphertext into groups
groups = divide_ciphertext(ciphertext, key_length)

# Step 2: Perform frequency analysis on each group
freq_results = frequency_analysis(groups)

# Print frequency analysis results
for group_num, freqs in freq_results:
    print(f"Group {group_num} frequency analysis:")
    for letter, freq in freqs:
        print(f"  {letter}: {freq}")
    print("\n")


from collections import Counter


def divide_ciphertext(ciphertext, key_length=6):
    groups = [''] * key_length  # Create a list for each group

    for i, letter in enumerate(ciphertext):
        groups[i % key_length] += letter  # Assign letters to groups cyclically

    return groups

# Example usage
groups = divide_ciphertext(ciphertext)

# Print each group
for i, group in enumerate(groups):
    print(f"Group {i+1}: {group}")
    
divide_ciphertext(ciphertext)
    
    

def caesar_shift(text, shift):
    result = ""
    for char in text:
            shift_base = ord('A')
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
    return result

#Create groups

Groups = dict(group1=["X","W","M","W","A"],
               group2=["G","J","N","C","W"], 
               group3=["G","X","P","C","J"],
               group4=["H","K","Q","I","N"],
               group5=["M","X","H","B","G"],
               group6=["Q","M","E","A","X"],)

#SYPPTJ	key
#FIRSTHELIVEDUPABOVEENTIRELYREA Plaintext
#Frequency analysis
# For example in group 1 W is the most frequent letter in the ciphertext
# there are 18 spaces between E and W. +1 to account for E and the caeser shift is 19 = S.
# For Group 2 the most common letter in the ciphertext is C 
# there are 24 spaces between E and C. +1 to account for E amd the ceaser shift is 25 = Y
# So on and so forth 
# and the key is    
# Recover the Key
# Decipher the ciphertext



#4





    



