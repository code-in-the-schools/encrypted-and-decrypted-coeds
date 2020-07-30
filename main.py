open_file(filename):
	f = open(filename, "r")
	sample = f.readlines()
	output = []
	for line in sample:
		line_words = []
		for word in line.split():
			line_words.append(word.lower())
		output.append(line_words)
	return (output)

#encrypt code

def encrypt_character(character, shift): 
  cipher = ord(character) + shift
  if cipher > ord("z"):
    cipher -= 26
  return(chr(cipher))

def encrypt_word(word, shift): 
  new_word = ""
  for character in word:
    new_word += encrypt_character(character, shift)
  return(new_word)
  
def encrypt_message(message, shift):
  new_message = []
  for line in message:
    new_line = []
    for word in line:
        new_line.append(encrypt_word(word, shift))
    new_message.append(new_line)
  return new_message
  
#decrypt code

def decrypt_character(character, shift): 
  cipher = ord(character) - shift
  if cipher < ord("a"):
    cipher += 26
  return(chr(cipher))

def decrypt_word(word, shift): 
  new_word = ""
  for character in word:
    new_word += decrypt_character(character, shift)
  return(new_word)
  
def decrypt_message(message, shift):
  new_message = []
  for line in message:
    new_line = []
    for word in line:
        new_line.append(decrypt_word(word, shift))
    new_message.append(new_line)
  return new_message

# program starts #
sample = open_file("sample.txt")
encrypted_message = encrypt_message(sample, 4)
print(encrypted_message)
print(decrypt_message(encrypted_message, 4))