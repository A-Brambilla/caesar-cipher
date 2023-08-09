alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  encrypted_text = []
  for letter in text:
    start_letter = alphabet.index(letter)
    result_letter = start_letter + shift
    if result_letter < 26:
      encrypted_text += alphabet[result_letter]
    elif result_letter >= 26:
      result_letter = result_letter - 26
      encrypted_text += alphabet[result_letter]
  print("The encrypted text is:", ''.join(encrypted_text))

def decrypt(text, shift):
  decrypted_text = []
  for letter in text:
    start_letter = alphabet.index(letter)
    result_letter = start_letter - shift
    if result_letter > 0:
      decrypted_text += alphabet[result_letter]
    elif result_letter <= 0:
      decrypted_text += alphabet[result_letter + 26]
  print("The decrypted text is:", ''.join(decrypted_text))

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
else:
  print("Invalid input")
