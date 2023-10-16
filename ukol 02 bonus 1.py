morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

text = input("Zadejte pozadovany text bez mezer a diakritiky: ")
text = text.lower() 

morse_preklad = [] # This line initializes an empty list to store the Morse code representations of the input text.
for char in text:
    if char in morse_code:
        morse_preklad.append(morse_code[char]) #If the character is found in the morse_code dictionary, its Morse code representation is appended to the morse_preklad list.
    else: 
        morse_preklad.append(" ")  # Adds a space for unknown characters

morse_text = " ".join(morse_preklad) # After processing all characters, this line joins the Morse code representations in the morse_preklad list into a single string, with each Morse character separated by a space.
print(morse_text)
