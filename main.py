import Tkinter as tk
import random
import numpy

class ConnectFour(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=490, height=490, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")

        self.cellwidth = 70
        self.cellheight = 70
        self.columnRanges = [(0, 70), (70, 140), (140, 210), (210, 280), (280, 350), (350, 420), (420, 490)]
        self.filledCircles = None

        self.startingColor = random.randint(0,1)
        self.numTurns = 0
        self.numWinsRed = 0
        self.numWinsYellow = 0
        self.gameFinished = False

        self.mapped = None
        self.rect = {}
        self.oval = {}

        self.bind("<Button-1>", self.on_click)

        self.initialize_board()

    def initialize_board(self):
        self.filledCircles = [6, 6, 6, 6, 6, 6, 6]
        self.mapped = [["g" for x in range(7)] for y in range(7)]
        self.numTurns = 0
        for col in range(7):
            for row in range(7):
                x1 = col * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row, col] = self.canvas.create_rectangle(x1, y1, x2, y2, fill = "blue", tags = "rect", outline = "")
                self.oval[row, col] = self.canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill = "seashell3", tags = "oval")

    def get_column(self, xIndex):
        i = 0
        for start, end in self.columnRanges:
            if xIndex in range(start, end):
                break
            i += 1
        return i

    def display_winner(self, color):
        self.gameFinished = True
        self.canvas.delete("all")
        self.canvas.configure(bg="seashell3")
        color = "yellow" if color == "y" else "red"
        self.canvas.create_text(245, 163, text = color + " wins!", font = "Herculanum 60 bold")
        self.canvas.create_text(245, 200, text = "Score", font = "Herculanum 30 bold")
        self.canvas.create_text(245, 230, text = "Red: " + str(self.numWinsRed), font = "Herculanum 30 bold")
        self.canvas.create_text(245, 260, text = "Yellow: " + str(self.numWinsYellow), font = "Herculanum 30 bold")

    def check_sequence(self, col, row):
        color = self.mapped[row][col]
        print("Color: {}".format(color))
        NE = E = SE = S = SW = W = NW = 0

        # NE
        r = row; c = col;
        while (c < 6 and r > 0) and (self.mapped[r - 1][c + 1] == color):
            NE += 1
            r -= 1; c += 1;

        # E
        r = row; c = col;
        while (c < 6) and (self.mapped[r][c + 1] == color):
            E += 1
            c += 1

        # SE
        r = row; c = col;
        while (r < 6 and c < 6) and (self.mapped[r + 1][c + 1] == color):
            SE += 1
            r += 1; c += 1;

        # S
        r = row; c = col;
        while (r < 6) and (self.mapped[r + 1][c] == color):
            S += 1
            r += 1

        # SW
        r = row; c = col;
        while (c > 0 and r < 6) and (self.mapped[r + 1][c - 1] == color):
            SW += 1
            r += 1; c -= 1

        # W
        r = row; c = col;
        while (c > 0) and (self.mapped[r][c - 1] == color):
            W += 1
            c -= 1

        # NW
        r = row; c = col;
        while (c > 0 and r > 0) and (self.mapped[r - 1][c - 1] == color):
            NW += 1
            r -= 1; c -= 1;

        if (S + 1 >= 4) or (W + 1 + E >= 4) or (NE + 1 + SW >= 4) or (NW + 1 + SE >= 4):
            if color == "y":
                self.numWinsYellow += 1
            else:
                self.numWinsRed += 1
            self.display_winner(color)

    def draw(self):
        self.gameFinished = True
        self.canvas.delete("all")
        self.canvas.configure(bg="seashell3")
        self.canvas.create_text(245, 163, text = "DRAW", font = "Herculanum 60 bold")
        self.canvas.create_text(245, 200, text = "Score", font = "Herculanum 30 bold")
        self.canvas.create_text(245, 230, text = "Red: " + str(self.numWinsRed), font = "Herculanum 30 bold")
        self.canvas.create_text(245, 260, text = "Yellow: " + str(self.numWinsYellow), font = "Herculanum 30 bold")
        print("Draw")

    def on_click(self, event):
        if self.gameFinished:
            self.gameFinished = False
            self.canvas.delete("all")
            self.initialize_board()

        else:
            index = self.get_column(event.x)
            if self.filledCircles[index] > -1:
                self.numTurns += 1
                if self.numTurns >= 49:
                    self.draw()
                col = index
                row = self.filledCircles[index]
                centerX = col * self.cellwidth + 35
                centerY = row * self.cellheight + 35
                print("Clicked col: {}, row: {}".format(col, row))
                item = self.canvas.find_closest(centerX, centerY)
                if "oval" in self.canvas.itemcget(item, "tags"):
                    color = "yellow2" if self.startingColor else "red"
                    self.startingColor = 1 - self.startingColor
                    self.mapped[row][col] = "y" if color == "yellow2" else "r"
                    self.canvas.itemconfig(item, fill = color)
                self.filledCircles[index] -= 1
                print(numpy.matrix(self.mapped))
                if self.numTurns >= 7:
                    self.check_sequence(col, row)

if __name__ == "__main__":
    game = ConnectFour()
    game.title("Connect4")
    game.mainloop()
