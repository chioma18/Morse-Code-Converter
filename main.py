morse_code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-', 'g': '--.', 'h': '....', 'i': '..',
              'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
              'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-.--', 'y': '-.--',
              'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

text = input("Type in your message: \n").lower()
sentence = []


# Create a function
def morse(plain_text):
    # The text that would be encoded to morse code
    morse_text = ""
    # To encode, the text would need to be looped over
    for letter in text:
        # Add the morse code version of each letter of the plain text to the sentence
        sentence.append(morse_code[letter])
        # To join the letters into a proper word without the list brackets, I use .join()
        # morse_text += ''.join(sentence)
    print(f"The morse code for {text} is {sentence}")


morse(plain_text=text)
