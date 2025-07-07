import re
from playsound import playsound
import time
class MorseCodeConverter:
    def __init__(self):
        pass

    MORSE_CODE_DICT = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    ':': '---...',
    ';': '-.-.-.',
    "'": '.----.',
    '"': '.-..-.',
    '?': '..--..',
    '!': '-.-.--',
    '+': '.-.-.',
    '=': '-...-',
    '-': '-....-',
    ' ' : '    '
}
    
    def __play_dot(self):
        playsound('dot.wav')

    def __play_dash(self):
        playsound('dash.wav')

# TODO - Loop through user text and transform it to morse code
    def convert_to_morse(self,text):
        morse_code = []
        for char in text:
            value = self.MORSE_CODE_DICT.get(char)
            if value is not None:
                morse_code.append(f"{value}/")
            else:
                print("Invalid character - does not exist within library.")
        morse_word = ''.join(morse_code)
        for c in morse_word:
            if c == '.':
                self.__play_dot()
            elif c== "-":
                self.__play_dash()
        return morse_word

    def convert_to_text(self,morse_code):
        # morse = [chunk for chunk in morse_code.split('/') if len(chunk) !=2 and not chunk.isspace()]
        # morse = re.split(r'( {4})', morse_code)
        morse = [chunk for chunk in re.split(r'( {4})|/', morse_code) if chunk and (chunk == '    ' or not chunk.isspace())]
        text = []
        for part in morse:
            key = self.__get_key_by_value(part)
            text.append(key)
        return ''.join(text)

    def __get_key_by_value(self,target):
        for k,v in self.MORSE_CODE_DICT.items():
            if v == target:
                return k
        return None