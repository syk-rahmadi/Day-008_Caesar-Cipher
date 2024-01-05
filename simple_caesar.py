#Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message ...\n").lower()
shift_number = int(input("Type the shift number ...\n"))

def caesar(mode_direction, text, shift):
    target_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if mode_direction == "encode":
            new_position = (position + shift) % 26
        elif mode_direction == "decode":
            new_position = (position - shift) % 26
        target_text += alphabet[new_position]
    print(f"Here is the {mode}d result: {target_text} ")

caesar(mode_direction=mode, text=message, shift=shift_number)

