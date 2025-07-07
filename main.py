import importlib
import MorseClass
# TODO - Implement MorseClass
importlib.reload(MorseClass)
from MorseClass import MorseCodeConverter

# TODO - Create MorseClass model/converter
converter = MorseCodeConverter()



print("====================================")
print("Welcome to the Morse Code Converter!")
print("====================================\n")

# TODO - Prompt user if they want to encrypt or decrypt a message
option = ''
while (option != 'exit'):
    option = input("Do you want to encrypt, decrypt or exit: ").lower()
    
    if option != 'exit':
        # TODO - Receive the user input
        

        # TODO - Convert to morse code
        if option == 'encrypt':
            text = input("Enter the text you want to encrypt: ").lower()
            print(f"Transformed to morse code: {converter.convert_to_morse(text)}\n")
            

        # TODO - Convert to plain text
        elif option == 'decrypt':
            text = input("Enter the morse code you want to decrypt: ").lower()
            print(f"Transformed to plaintext: {converter.convert_to_text(text)}\n")

        else:
            print("Invalid option.\n")
    else:
        print("\nGoodbye!\n")




# TODO - Transform the message

# TODO - Print the transformed message

# TODO - Reprompt


