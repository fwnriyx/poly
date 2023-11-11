morseCodeTranslate = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..'
}


def toMorse(text):
    morse_code = ""
    for i in text:
        if i == ' ':
            morse_code += ','
        for j in i:
            if j.upper() in morseCodeTranslate:
                morse_code += morseCodeTranslate[j.upper()].rstrip(',') + " ,"
            elif j == '\n':
                morse_code += '\n,'
    return morse_code

def fromMorse(morse_code):
    decoded_text = ''
    for char in morse_code.split(','):
        if char == '\n':
            decoded_text += '\n'
        for key, value in morseCodeTranslate.items():
            if char == value.rstrip(','):
                decoded_text += str(key)
        if char == '':
            decoded_text += ' '
    return decoded_text


morse = open("morse.txt", "r")
morse_code = morse.read()
print(toMorse(morse_code))

text = open("text.txt", "r")
text_code = text.read()
print(fromMorse(text_code)) 
