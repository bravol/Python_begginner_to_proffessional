alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(r'''
 _           _           _             
| |         | |         | |            
| |__   __ _| |__  _   _| | ___  _ __  
| '_ \ / _` | '_ \| | | | |/ _ \| '_ \ 
| |_) | (_| | |_) | |_| | | (_) | | | |
|_.__/ \__,_|_.__/ \__, |_|\___/|_| |_|
                    __/ |              
                   |___/               
''')

# ENCRYPT MESSAGE
def encrypt(original_text, shift_amount):
    cipher_text=""
    for letter in original_text:
       shifted_position = alphabet.index(letter) + shift_amount
       shifted_position %= len(alphabet)
       cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
# encrypt(original_text = text, shift_amount = shift)

# DECRYPT
def decrypt(original_text, shift_amount):
    decrypt_text=''
    for letter in original_text:
        shift_position=alphabet.index(letter) - shift_amount
        shift_position %= len(alphabet) # makes sure that we are in the range of alphabet 26
        decrypt_text += alphabet[shift_position]
    print(f" The original message was {decrypt_text} ")
# decrypt(original_text = text, shift_amount = shift)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:

        if letter not in alphabet:
            output_text+=letter
        else:
            if encode_or_decode =='decode':
                shift_position = alphabet.index(letter) - shift_amount
            else:
                shift_position = alphabet.index(letter) + shift_amount

            shift_position %= len(alphabet)
            output_text += alphabet[shift_position]
    print(f"The {encode_or_decode} result was {output_text} ")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again, Otherwise type 'no'.\n").lower()

    if restart == 'no':
        should_continue = False
        print("Good bye!")

