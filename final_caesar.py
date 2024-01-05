#Caesar Cipher

caesar_cipher = True
while caesar_cipher:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message ...\n").lower()
    shift_number = int(input("Type the shift number ...\n"))


    def caesar(mode_direction, text, shift):
        target_text = ""
        if mode_direction == "decode":
            shift *= -1
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = (position + shift) % 26
                target_text += alphabet[new_position]
            else:
                target_text += char
        print(f"Here is the {mode}d result: {target_text} ")

    caesar(mode_direction=mode, text=message, shift=shift_number)
    conti = input("Type 'Yes' if you want to go again. Otherwise type 'No'...\n").lower()
    if conti == "no":
        caesar_cipher = False
        print("Goodbye Fella.")