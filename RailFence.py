import streamlit as st

# Rail Fence Cipher Encryption
def rail_fence_encrypt(plaintext, num_rails):
    if num_rails == 1:
        return plaintext
    
    rails = [''] * num_rails
    direction_down = False
    row = 0

    # Build the zigzag pattern
    for char in plaintext:
        rails[row] += char
        if row == 0 or row == num_rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    
    # Concatenate all rows to form the ciphertext
    return ''.join(rails)

# Rail Fence Cipher Decryption
def rail_fence_decrypt(ciphertext, num_rails):
    if num_rails == 1:
        return ciphertext
    
    # Create an empty zigzag pattern to find positions of characters
    zigzag = [['\n' for _ in range(len(ciphertext))] for _ in range(num_rails)]
    direction_down = False
    row, col = 0, 0

    # Mark the places where characters will go
    for i in range(len(ciphertext)):
        zigzag[row][col] = '*'
        if row == 0 or row == num_rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
        col += 1

    # Place the ciphertext characters into the zigzag pattern
    index = 0
    for i in range(num_rails):
        for j in range(len(ciphertext)):
            if zigzag[i][j] == '*' and index < len(ciphertext):
                zigzag[i][j] = ciphertext[index]
                index += 1

    # Read off the characters in zigzag order
    result = []
    row, col = 0, 0
    direction_down = False
    for i in range(len(ciphertext)):
        result.append(zigzag[row][col])
        if row == 0 or row == num_rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
        col += 1

    return ''.join(result)

# Streamlit app title
st.title("Rail Fence Cipher Encryption/Decryption")

# Text input
input_text = st.text_area("Enter text")

# Slider to select number of rails
num_rails = st.slider("Number of Rails", 1, 10, 3)

# Mode selection (Encrypt or Decrypt)
mode = "Encrypt"

# Button to trigger the operation
if st.button("Submit"):
    if mode == "Encrypt":
        # Call the encryption function
        result = rail_fence_encrypt(input_text, num_rails)
        st.write(f"Encrypted Text: {result}")
        dec = rail_fence_decrypt(result, num_rails)
        st.write(f"Decrypted Text: {dec}")
    else:
        # Call the decryption function
        result = rail_fence_decrypt(input_text, num_rails)
        st.write(f"Decrypted Text: {result}")
