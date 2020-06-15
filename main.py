from tkinter import Tk, Button, Label
from time import time
from random import choices


class ColorGame:

    COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]

    def __init__(self):

        self.janela = Tk(screenName="Color Game")
        self.janela.title("Color Game")
        self.janela['bg'] = '#777777'
        self.janela.geometry("472x95+900+100")

        self.text = Label(self.janela, text="Press any button to start the game.",
                          width=40, height=3, font=("Courier", 10), bg="#777777")
        self.text.grid(row=1, column=0, columnspan=6)

        self.delay_text = Label(self.janela, text='', font=("Courier", 8), bg=self.janela['bg'])
        self.delay_text.grid(row=1, column=6, columnspan=2)

        self.acertos = int()
        self.ini = float()
        self.generate_buttons()
        self.run = False

        self.janela.mainloop()

    def random(self):
        text, color = choices(ColorGame.COLORS, k=2)
        self.text['text'], self.text['fg'] = text, color

    def new_game(self):
        self.run = True
        self.acertos = 0
        self.ini = time()
        self.text['font'] = ("Courier", 20)
        self.text['width'], self.text['height'] = 10, 2

    def end_game(self):
        delay = time() - self.ini
        self.delay_text['text'] = f"Response:\n{self.acertos/delay:.1f}/s"
        self.run = False
        self.text['text'] = "Press any button to start the game."
        self.text['font'] = ("Courier", 10)
        self.text['fg'] = 'black'
        self.text['width'], self.text['height'] = 40, 3

    def click(self, color):
        if not self.run:
            self.new_game()
            self.random()
        elif color == self.text['text']:
            self.acertos += 1
            self.random()
        else:
            self.end_game()

    def generate_buttons(self):
        def gen(col_id):
            color = ColorGame.COLORS[col_id]
            Button(bg=color, width=7, height=2, command=lambda: self.click(color)).grid(row=2, column=col_id)

        for i in range(8):
            gen(i)


ColorGame()
