#Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message ...\n").lower()
shift_number = int(input("Type the shift number ...\n"))

def encrypt(text, shift):
    cypherText =""
    for letter in text:
        position = alphabet.index(letter)
        new_position = (position + shift) % 26
        cypherText += alphabet[new_position]
    print(f"Here is the encoded result: {cypherText} ")

def decrypt(cypher_text, shift):
    decryptText =""
    for letter in cypher_text:
        position = alphabet.index(letter)
        new_position = (position - shift) % 26
        decryptText += alphabet[new_position]
    print(f"Here is the encoded result: {decryptText} ")


if mode == "encode":
    encrypt(text=message, shift=shift_number)
elif mode == "decode":
    decrypt(cypher_text=message, shift=shift_number)

#input("Type 'yes' if you want to start again. Otherwise 'no' ")
