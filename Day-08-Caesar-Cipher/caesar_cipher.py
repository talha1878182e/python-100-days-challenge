import time

alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r',
            's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']

print("""
 _____                                                  _____ 
( ___ )------------------------------------------------( ___ )
 |   |                                                  |   | 
 |   |  ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗  |   | 
 |   | ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗ |   | 
 |   | ██║     ███████║█████╗  ███████╗███████║██████╔╝ |   | 
 |   | ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗ |   | 
 |   | ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║ |   | 
 |   |  ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ |   | 
 |   |                                                  |   | 
 |   |  ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗       |   | 
 |   | ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗      |   | 
 |   | ██║     ██║██████╔╝███████║█████╗  ██████╔╝      |   | 
 |   | ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗      |   | 
 |   | ╚██████╗██║██║     ██║  ██║███████╗██║  ██║      |   | 
 |   |  ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      |   | 
 |___|                                                  |___| 
(_____)------------------------------------------------(_____)    
""")

time.sleep(1)
direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()
text = input("Type your message:\n ").lower()
shift = int(input("Type the shift number:\n "))


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for char in original_text:
        if char in alphabet:
            shifted_position = (alphabet.index(char) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += char

    print(f"Here is the {encode_or_decode}d result: {output_text}")


if direction in ['encode', 'decode']:
    print("is being translated...")
    time.sleep(1)
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
else:
    print("Invalid option selected.")
