from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=1)

window.mainloop()