from tkinter import *

FONT1 = ('Arial', 15, 'bold')

total = 0
morse_to_letter = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}

morse_to_letter_values = {str(value) for value in morse_to_letter.values()}


def convertion():
    your_output.delete("1.0", "end")
    text_value = your_input.get('1.0', 'end')
    if total % 2 == 0:
        for t in text_value.upper():
            for key, value in morse_to_letter.items():
                if t == key:
                    your_output.insert('1.0', value)
    else:
        text = ''
        for key, value in morse_to_letter.items():
            part = text_value[:len(value)]
            if value == part:
                text += key
                text_value = text_value[len(value):]
        your_output.insert('1.0', text)


def switch():
    your_output.delete("1.0", "end")
    global total
    if total == 10:
        total = 0
    if total % 2 == 0:
        text_label.config(text='Your code:')
        code_label.config(text='The text:')
    else:
        text_label.config(text='Your text:')
        code_label.config(text='The code:')
    total += 1
    print(total)
    return total


window = Tk()
window.title('Morse Code Converter')
window.minsize(width=800, height=800)

text_label = Label(text='Your text:', font=FONT1)
text_label.pack()
your_input = Text(width=50, height=20)
your_input.pack()
code_label = Label(text='The code:', font=FONT1)
code_label.pack()
your_output = Text(width=50, height=10)
your_output.pack()
convert_button = Button(text='Convert', font=FONT1, width=15, command=convertion)
convert_button.pack()
switch_button = Button(text='Switch', font=FONT1, width=15, command=switch)
switch_button.pack()

mainloop()
