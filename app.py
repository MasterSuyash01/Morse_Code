from flask import Flask, render_template, request

# Dictionary to map characters to their Morse code representation
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' ',  # For spaces in text to be translated
}

app = Flask(__name__)

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
    return ' '.join(morse_code)

def morse_to_text(morse_code):
    text = []
    morse_code_list = morse_code.split(' ')
    for code in morse_code_list:
        for char, morse in morse_code_dict.items():
            if morse == code:
                text.append(char)
                break
    return ' '.join(text)

@app.route("/", methods=["GET", "POST"])
def morse_code_translator():
    result = None

    if request.method == "POST":
        text = request.form.get("text")
        choice = request.form.get("choice")

        if choice == "to_morse":
            result = text_to_morse(text)
        elif choice == "to_text":
            result = morse_to_text(text)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
