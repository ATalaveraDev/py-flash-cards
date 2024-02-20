from tkinter import *
from pandas import read_csv, DataFrame
from random import choice
from functools import partial

BACKGROUND_COLOR = "#B1DDC6"

current_language = 'French'
word = {}

def generate_random_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = choice(data)
    canvas.itemconfig(word_language, text="French")
    canvas.itemconfig(word_text, text=word["French"])
    canvas.itemconfig(card_image, image=card_front_image)
    flip_timer = window.after(3000, flip)

def flip():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(word_language, text="English")
    canvas.itemconfig(word_text, text=word["English"])

def is_known():
    data.remove(word)
    new_data = DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    generate_random_word()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
word_language = canvas.create_text(400, 150, text="French", font=("Comic sans", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Comic sans", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_random_word)
wrong_button.grid(row=1, column=1)

try:
    data = read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = read_csv("data/french_words.csv").to_dict(orient="records")

flip_timer = window.after(3000, flip)
generate_random_word()

window.mainloop()
