import streamlit as st

# Function to encrypt using Caesar Cipher
def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetical characters are unchanged
    return encrypted_text

# Function to decrypt using Caesar Cipher
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabetical characters are unchanged
    return decrypted_text

# Streamlit app title
st.title("Caesar Cipher")

# Text input
input_text = st.text_area("Enter text")

# Slider to select shift
shift = st.slider("Shift (Key)", 1, 25, 3)

# Mode selection (Encrypt or Decrypt)
mode = "Encrypt"

# Button to trigger the operation
if st.button("Submit"):
    if mode == "Encrypt":
        # Call the encryption function
        result = caesar_encrypt(input_text, shift)
        st.write(f"Encrypted Text: {result}")
        decrypt_result = caesar_decrypt(result, shift)
        st.write(f"Decrypted Text: {decrypt_result}")
    else:
        # Call the decryption function
        result = caesar_decrypt(input_text, shift)
        st.write(f"Decrypted Text: {result}")
