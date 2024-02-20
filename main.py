from tkinter import *
from pandas import read_csv
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

french_words = []
english_words = []

def generate_random_word():
    word = choice(data)
    canvas.itemconfig(word_text, text=word['French'])

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="French", font=("Comic sans", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Comic sans", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=generate_random_word)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_random_word)
wrong_button.grid(row=1, column=1)

with open("data/french_words.csv", "r") as data_file:
    data = read_csv(data_file).to_dict(orient="records")

generate_random_word()

window.mainloop()