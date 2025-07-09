# Morse Code Converter 🔤➡️📻

A Python application that converts text to Morse code and vice versa, with audio playback functionality for an authentic Morse code experience.

## Features ✨

- **Text to Morse Code Conversion**: Convert any text string to Morse code
- **Morse Code to Text Conversion**: Decode Morse code back to readable text
- **Audio Playback**: Hear the actual Morse code sounds with dot and dash audio files
- **Interactive CLI**: User-friendly command-line interface
- **Comprehensive Character Support**: Supports letters (a-z), numbers (0-9), and common punctuation marks

## Supported Characters 📝

The converter supports the following characters:
- **Letters**: A-Z (case insensitive)
- **Numbers**: 0-9
- **Punctuation**: `.`, `,`, `:`, `;`, `'`, `"`, `?`, `!`, `+`, `=`, `-`
- **Spaces**: Converted to appropriate spacing in Morse code

## Installation 🚀

1. **Clone or download** this repository to your local machine
2. **Install required dependencies**:
   ```bash
   pip install playsound
   ```
3. **Ensure audio files are present**: Make sure `dot.wav` and `dash.wav` are in the same directory as the Python files

## Usage 💻

### Running the Application

```bash
python main.py
```

### Interactive Menu Options

When you run the application, you'll see:
```
====================================
Welcome to the Morse Code Converter!
====================================

Do you want to encrypt, decrypt or exit:
```

Choose from the following options:
- **encrypt**: Convert text to Morse code
- **decrypt**: Convert Morse code to text
- **exit**: Close the application

### Example Usage

#### Encrypting Text to Morse Code
```
Do you want to encrypt, decrypt or exit: encrypt
Enter the text you want to encrypt: hello world
Transformed to morse code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

#### Decrypting Morse Code to Text
```
Do you want to encrypt, decrypt or exit: decrypt
Enter the morse code you want to decrypt: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Transformed to plaintext: hello world
```

## File Structure 📁

```
String_2_Morse/
├── main.py              # Main application entry point
├── MorseClass.py        # Morse code converter class
├── dot.wav              # Audio file for dot sound
├── dash.wav             # Audio file for dash sound
└── .gitignore           # Git ignore file
```

## How It Works 🔧

### MorseCodeConverter Class

The `MorseCodeConverter` class in `MorseClass.py` provides:

1. **Morse Code Dictionary**: A comprehensive mapping of characters to their Morse code equivalents
2. **Audio Playback**: Private methods to play dot and dash sounds
3. **Conversion Methods**:
   - `convert_to_morse(text)`: Converts text to Morse code with audio playback
   - `convert_to_text(morse_code)`: Converts Morse code back to text

### Audio Features 🔊

- **Dot Sound**: Plays `dot.wav` for each dot (.) in the Morse code
- **Dash Sound**: Plays `dash.wav` for each dash (-) in the Morse code
- **Real-time Playback**: Audio plays as the conversion happens

## Technical Details 🛠️

### Dependencies
- **playsound**: For audio playback functionality
- **re**: For regular expression operations (built-in)
- **time**: For timing operations (built-in)

### Character Encoding
- Morse code characters are separated by a single space (` `).
- Spaces between words are represented by a slash (`/`).

## Error Handling 🚨

- **Invalid Characters**: Characters not in the Morse code dictionary are skipped with a warning message
- **Audio File Issues**: Ensure `dot.wav` and `dash.wav` files are present for audio functionality
- **Input Validation**: The application handles empty inputs and invalid menu choices

## Future Enhancements 🔮

Potential improvements for this project:
- Add support for more special characters
- Implement adjustable audio playback speed
- Add file input/output functionality
- Create a GUI version
- Add timing accuracy for proper Morse code spacing

## Contributing 🤝

Feel free to fork this project and submit pull requests for any improvements or bug fixes.

## License 📄

This project is open source and available under the MIT License.

---

**Enjoy converting text to Morse code and back! 📻✨**
