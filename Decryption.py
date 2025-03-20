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



#FIRSTHELIVEDUPABOVEENTIRELYREA Plaintext
#Frequency analysis
# Create 6 groups of 5 letters taking every 6th letter for each group 
# Then count the frequency of each letter in each group
# For example in group 1 W(17) is the joint most frequent letter in the ciphertext
# there are 18 spaces between E and W. +1 to account for E and the caeser shift is 19 = S.
# For Group 2 the most common letter in the ciphertext is C(21) 
# there are 24 spaces between E and C. +1 to account for E amd the ceaser shift is 25 = Y
# So on and so forth 
# and the key is    
# Recover the Key
# Decipher the ciphertext
#SYPPTJ	key


#4

from collections import Counter

# Open the file in read mode
with open("lg565/cexercise4.txt", "r") as file:
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
key_length = 4

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
    
## 6 Letter Key ##
    
# For example in group 1 Y(13) is the joint most frequent letter in the ciphertext
# there are 20 spaces between E and Y. +1 to account for E and the caeser shift is 21 = U.

# For example in group 2 C(12) is the most frequent letter in the ciphertext
# there are 24 spaces between E and C. +1 to account for E and the caeser shift is 25 = Y.

# For example in group 3 Y(14) is the most frequent letter in the ciphertext
# there are 20 spaces between E and Y. +1 to account for E and the caeser shift is 21 = U.

# For example in group 4 S(14) is the  most frequent letter in the ciphertext
# there are 13 spaces between E and S. +1 to account for E and the caeser shift is 14 = N.

# For example in group 5 Y(14) is the most frequent letter in the ciphertext
# there are 20 spaces between E and Y. +1 to account for E and the caeser shift is 21 = U.
    
# For example in group 6 C(12) is the  most frequent letter in the ciphertext
# there are 20 spaces between E and C. +1 to account for E and the caeser shift is 21 = Y.

Key1 = 'UYUNUY'

## 5 Letter Key ##

# For example in group 1 C(18) is the most frequent letter in the ciphertext
# there are 24 spaces between E and C. +1 to account for E and the caeser shift is 25 = Y.

# For example in group 2 P(24) is the most frequent letter in the ciphertext
# there are 11 spaces between E and P. +1 to account for E and the caeser shift is 12 = L.

# For example in group 3 U(18) is the most frequent letter in the ciphertext
# there are 16 spaces between E and U. +1 to account for E and the caeser shift is 17 = Q.

# For example in group 4 P(24) is the most frequent letter in the ciphertext
# there are 11 spaces between E and P. +1 to account for E and the caeser shift is 12 = L.

# For example in group 5 S(26) is the joint most frequent letter in the ciphertext
# there are 14 spaces between E and Y. +1 to account for E and the caeser shift is 15 = O.

Key2 = 'YLQLO'


## 4 Letter Key ##

# For example in group 1 Y(22) is the most frequent letter in the ciphertext
# there are 20 spaces between E and Y. +1 to account for E and the caeser shift is 21 = U.

# For example in group 1 C(16) is the most frequent letter in the ciphertext
# there are 24 spaces between E and C. +1 to account for E and the caeser shift is 25 = Y.

# For example in group 1 Y(19) is the most frequent letter in the ciphertext
# there are 20 spaces between E and Y. +1 to account for E and the caeser shift is 21 = U.

# For example in group 4 P(18) is the most frequent letter in the ciphertext
# there are 11 spaces between E and P. +1 to account for E and the caeser shift is 12 = L.

Key3 = 'UYUL'


# Function to decode Vigenere cipher 
def decode_Vigenere_cipher(ciphertext, key):
    decoded_text = ""

    for i in range(len(ciphertext)):
        
        offset = ord('A')
            
        # Shift the character forward and wrap around the alphabet
        decoded_char = chr(((ord(ciphertext[i]) - ord(key[i]))) % 26 + offset)
        decoded_text += decoded_char

    return decoded_text



key = Key2

def generate_key(text, key):
    key = list(key)
    if len(key) < len(text):
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

generated_key = generate_key(ciphertext, key)


plainText4 = decode_Vigenere_cipher(ciphertext,generated_key)

plainText4 = plainText4[:30]

if plainText4 in text:
    print("The extract exists in the text.")
else:
    print("The extract does not exist in the text.")
    
    
##5##

import pandas as pd

# Open the file in read mode
with open("lg565/cexercise5.txt", "r") as file:
    # Read the content of the file
    ciphertext = file.read()
    
def split_text_into_columns4(text, num_columns=4):
    # Calculate the length of each column
    # column_length = len(text) // num_columns
    
    # Split the text into columns
    # columns = [text[i:i+column_length] for i in range(0, len(text), column_length)]
    
    # Create a DataFrame where each row is a segment of the text
    
    df1 = pd.DataFrame([list(text)[:210]])
    df2 = pd.DataFrame([list(text)[210:420]])
    df3 = pd.DataFrame([list(text)[420:630]])
    df4 = pd.DataFrame([list(text)[630:840]])
    
    
    return df1,df2,df3,df4



df1,df2,df3,df4 = split_text_into_columns4(ciphertext)

transpose_df1 = df1.transpose()
transpose_df2 = df2.transpose()
transpose_df3 = df3.transpose()
transpose_df4 = df4.transpose()

transpose_df1 = transpose_df1.rename(columns={0: 'df1'})
transpose_df2 = transpose_df2.rename(columns={0: 'df2'})
transpose_df3 = transpose_df3.rename(columns={0: 'df3'})
transpose_df4 = transpose_df4.rename(columns={0: 'df4'})

dataframe = transpose_df1.merge(transpose_df2, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df3, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df4, left_index=True, right_index=True, how='left')


def split_text_into_columns5(text, num_columns=5):
    # Calculate the length of each column
    # column_length = len(text) // num_columns
    
    # Split the text into columns
    # columns = [text[i:i+column_length] for i in range(0, len(text), column_length)]
    
    # Create a DataFrame where each row is a segment of the text
    
    df1 = pd.DataFrame([list(text)[:168]])
    df2 = pd.DataFrame([list(text)[168:336]])
    df3 = pd.DataFrame([list(text)[336:504]])
    df4 = pd.DataFrame([list(text)[504:672]])
    df5 = pd.DataFrame([list(text)[672:840]])
    
    return df1,df2,df3,df4,df5



df1,df2,df3,df4,df5 = split_text_into_columns5(ciphertext)

transpose_df1 = df1.transpose()
transpose_df2 = df2.transpose()
transpose_df3 = df3.transpose()
transpose_df4 = df4.transpose()
transpose_df5 = df4.transpose()

transpose_df1 = transpose_df1.rename(columns={0: 'df1'})
transpose_df2 = transpose_df2.rename(columns={0: 'df2'})
transpose_df3 = transpose_df3.rename(columns={0: 'df3'})
transpose_df4 = transpose_df4.rename(columns={0: 'df4'})
transpose_df5 = transpose_df5.rename(columns={0: 'df5'})

dataframe = transpose_df1.merge(transpose_df2, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df3, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df4, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df5, left_index=True, right_index=True, how='left')


def split_text_into_columns6(text, num_columns=6):
    # Calculate the length of each column
    # column_length = len(text) // num_columns
    
    # Split the text into columns
    # columns = [text[i:i+column_length] for i in range(0, len(text), column_length)]
    
    # Create a DataFrame where each row is a segment of the text
    
    df1 = pd.DataFrame([list(text)[:140]])
    df2 = pd.DataFrame([list(text)[140:280]])
    df3 = pd.DataFrame([list(text)[280:420]])
    df4 = pd.DataFrame([list(text)[420:560]])
    df5 = pd.DataFrame([list(text)[560:700]])
    df6 = pd.DataFrame([list(text)[700:840]])
    
    
    return df1,df2,df3,df4,df5,df6


df1,df2,df3,df4,df5,df6 = split_text_into_columns6(ciphertext)

transpose_df1 = df1.transpose()
transpose_df2 = df2.transpose()
transpose_df3 = df3.transpose()
transpose_df4 = df4.transpose()
transpose_df5 = df5.transpose()
transpose_df6 = df6.transpose()

transpose_df1 = transpose_df1.rename(columns={0: 'df1'})
transpose_df2 = transpose_df2.rename(columns={0: 'df2'})
transpose_df3 = transpose_df3.rename(columns={0: 'df3'})
transpose_df4 = transpose_df4.rename(columns={0: 'df4'})
transpose_df5 = transpose_df5.rename(columns={0: 'df5'})
transpose_df6 = transpose_df6.rename(columns={0: 'df6'})

dataframe = transpose_df1.merge(transpose_df2, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df3, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df4, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df5, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df6, left_index=True, right_index=True, how='left')


##6##

import pandas as pd

with open("lg565/cexercise6.txt", "r") as file:
    # Read the content of the file
    ciphertext = file.read()

def split_text_into_columns6(text, num_columns=6):
    # Calculate the length of each column
    # column_length = len(text) // num_columns
    
    # Split the text into columns
    # columns = [text[i:i+column_length] for i in range(0, len(text), column_length)]
    
    # Create a DataFrame where each row is a segment of the text
    
    df1 = pd.DataFrame([list(text)[:140]])
    df2 = pd.DataFrame([list(text)[140:280]])
    df3 = pd.DataFrame([list(text)[280:420]])
    df4 = pd.DataFrame([list(text)[420:560]])
    df5 = pd.DataFrame([list(text)[560:700]])
    df6 = pd.DataFrame([list(text)[700:840]])
    
    
    return df1,df2,df3,df4,df5,df6


df1,df2,df3,df4,df5,df6 = split_text_into_columns6(ciphertext)

transpose_df1 = df1.transpose()
transpose_df2 = df2.transpose()
transpose_df3 = df3.transpose()
transpose_df4 = df4.transpose()
transpose_df5 = df5.transpose()
transpose_df6 = df6.transpose()

transpose_df1 = transpose_df1.rename(columns={0: 'df1'})
transpose_df2 = transpose_df2.rename(columns={0: 'df2'})
transpose_df3 = transpose_df3.rename(columns={0: 'df3'})
transpose_df4 = transpose_df4.rename(columns={0: 'df4'})
transpose_df5 = transpose_df5.rename(columns={0: 'df5'})
transpose_df6 = transpose_df6.rename(columns={0: 'df6'})

dataframe = transpose_df1.merge(transpose_df2, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df3, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df4, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df5, left_index=True, right_index=True, how='left')
dataframe = dataframe.merge(transpose_df6, left_index=True, right_index=True, how='left')

dfi = dataframe[['df2','df1','df6','df3','df5','df4']]


##7##

from collections import Counter

# Open the file in read mode
with open("lg565/cexercise7.txt", "r") as file:
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
key_length = 1

# Step 1: Divide ciphertext into groups
groups = divide_ciphertext(ciphertext, key_length)

# Step 2: Perform frequency analysis on each group
freq_results = frequency_analysis(groups)

# Print frequency analysis results
for group_num, freqs in freq_results:
    print(f"Group {group_num} frequency analysis:")
    for letter, freq in freqs:
        print(f" {letter}: {freq}")
    print("\n")
    

ciphertext = ciphertext[:30] 
plainText = ciphertext.replace('|', 'A')   
plainText = plainText.replace('L', '|')

plainText = plainText.replace('H', 'T')
plainText = plainText.replace('T', 'H')
plainText = plainText.replace('K', 'E')

plainText = 'HUV|TUFE|GW|APPGXWT|GJ|THE|IGT'


plainText = plainText.replace('P', 'C')
plainText = plainText.replace('G', 'O')
plainText = plainText.replace('X', 'U')
plainText = plainText.replace('W', 'N')

plainText = plainText.replace('J', 'F')



plainText = plainText.replace('U', 'O')
plainText = plainText.replace('E', 'W')
plainText = plainText.replace('K', 'H')


