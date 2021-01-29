#Caesar cipher game where the user can input the letters and
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to Caesar Cipher!")



#function to encrypt
def encrypt(plain_text, shift_amount):
    cipher_text = ''
    new_letter = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter += alphabet[new_position]
        cipher_text = new_letter
    print(cipher_text)

#function to decrypt
def decrypt(plain_text, shift_amount):
    decipher_text = ''
    new_letter = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter += alphabet[new_position]
        decipher_text = new_letter
    print(decipher_text)

#function to do both
def caesar(direction, plain_text, shift_amount):
    text = ''
    new_letter = ''
    if direction == 'decode':
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter += alphabet[new_position]
            text = new_letter
        else:
            new_letter += char
            text = char
    print(f"Here's the {direction}d result: {text}")

print(logo)

should_continue = False

while not should_continue:
    direction = input("If you want to encrypt write encode or if you want to decrypt write decrypt? ")
    letters = input("What letters do you want to input? ")
    shift = int(input("How many do you want to shift? "))


#encrypt(letters, shift)
#decrypt(letters, shift)
    caesar(direction, letters, shift)

    shift = shift % 26

    start_over = input("Do you want to start over? Yes or No? ").lower()
    if start_over == 'no':
        should_continue = True
        print("Thank you, Goodbye")
