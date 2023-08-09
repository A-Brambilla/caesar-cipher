alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):
  output_text = ""
  for letter in text:
    position = alphabet.index(letter)
    if direction == "encode":
      new_position = position + shift
      if new_position < 26:
        output_text += alphabet[new_position]
      elif result_letter >= 26:
        output_text += alphabet[new_position - 26]
    elif direction == "decode":
      new_position = position - shift
      output_text += alphabet[new_position]
    else:
      print("invalid input")
      break
  print(f"The {direction}d text is {output_text}")
    
caesar(direction, text, shift)
