message = "Goeiemiddag!"
import string
import random

def rot_rand(message):
  alphabet = list(string.ascii_lowercase)
  x = [i for i in message]
  encoded_message = ""
  encoder = []
  for i in range(len(x)):
    orig_char = x[i]

    random_number = random.randint(1,100)
    encoder.append(random_number)
    if (x[i].lower()) in alphabet:
      encoded_char = alphabet[(int(alphabet.index(x[i].lower()))+random_number)%26]
      if orig_char.isupper():
        encoded_char = encoded_char.upper()
    else:
      encoded_char = x[i]
    encoded_message += encoded_char
  return encoded_message, encoder

encoded_message, encoder = rot_rand(message)

print(encoded_message)
print(encoder)

def decoder(encoded_message, encoder):
  alphabet = list(string.ascii_lowercase)
  x = [i for i in encoded_message]
  decoded_message = ""
  
  for i in range(len(x)):
    orig_char = x[i]

    if (x[i].lower()) in alphabet:
      encoded_char = alphabet[(int(alphabet.index(x[i].lower()))-encoder[i])%26]
      if orig_char.isupper():
        encoded_char = encoded_char.upper()
    else:
      encoded_char = x[i]
    decoded_message += encoded_char

  return decoded_message

print(decoder(encoded_message, encoder))
