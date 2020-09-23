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
        self.clicked = False
        self.columnRanges = [(0, 70), (70, 140), (140, 210), (210, 280), (280, 350), (350, 420), (420, 490)]
        self.filledCircles = [6, 6, 6, 6, 6, 6, 6]
        self.startingColor = random.randint(0,1)
        self.numTurns = 0
        #self.previousCol = [-1, -1, -1]
        self.bind("<Motion>", self.on_hover)
        self.bind("<Button-1>", self.on_click)

        self.mapped = [["g" for x in range(7)] for y in range(7)]

        self.rect = {}
        self.oval = {}
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

    def on_hover(self, event):
        pass
        #print("Hovering: {},{}".format(event.x, event.y))
        """
        x = event.x
        index = self.get_column(x)
        if self.filledCircles[index] > -1:
            centerX = index * self.cellwidth + 35
            centerY = self.filledCircles[index] * self.cellheight + 35
            item = self.canvas.find_closest(centerX, centerY)
            if "oval" in self.canvas.itemcget(item, "tags") and index != previousCol[0]:
                if previousCol[0] != -1:
                    prevX = previousCol[0] * self.cellwidth + 35
                    prevY = self.filledCircles[previousCol[0]] * self.cellheight + 35
                    prevItem = self.canvas.find_closest(prevX, prevY)
                    self.canvas.itemconfig(prevItem, fill = "seashell3")
                color = "yellow" if self.startingColor else "red"
                self.canvas.itemconfig(item, fill = color)
            self.filledCircles[index] -= 1
            """

    def check_sequence(self, col, row, dir, len):
        color = self.mapped[row][col]
        print("Color: {}".format(color))
        NE = E = SE = S = SW = W = NW = 0
        # nw n ne
        #  w c e
        # sw s se

        # NE
        r = row; c = col;
        while (c < 6 and r > 0) and (self.mapped[r - 1][c + 1] == color):
            NE += 1
            #print("NE: {}".format(NE))
            r -= 1; c += 1;

        # E
        r = row; c = col;
        while (c < 6) and (self.mapped[r][c + 1] == color):
            E += 1
            c += 1
            #print("E")

        # SE
        r = row; c = col;
        while (r < 6 and c < 6) and (self.mapped[r + 1][c + 1] == color):
            #print("SE")
            SE += 1
            r += 1; c += 1;

        # S
        r = row; c = col;
        while (r < 6) and (self.mapped[r + 1][c] == color):
            S += 1
            r += 1
            #print("S")

        # SW
        r = row; c = col;
        while (c > 0 and r < 6) and (self.mapped[r + 1][c - 1] == color):
            SW += 1
            r += 1; c -= 1
            #print("SW")

        # W
        r = row; c = col;
        if (c > 0) and (self.mapped[r][c - 1] == color):
            W += 1
            c -= 1
            #print ("W")

        # NW
        r = row; c = col;
        if (c > 0 and r > 0) and (self.mapped[r - 1][c - 1] == color):
            NW += 1
            r -= 1; c -= 1;
            #print("NW")

        if S + 1 >= 4:
            print("WINNER")
        elif W + 1 + E >= 4:
            print("WINNER")
        elif NE + 1 + SW >= 4:
            print("WINNER")
        elif NW + 1 + SE >= 4:
            print("WINNER")

    def on_click(self, event):
        # For now increment counter. We are assuming clicking is means you played your turn
        self.numTurns += 1
        index = self.get_column(event.x)

        # Only do something if there are empty slots in given column
        if self.filledCircles[index] > -1:
            col = index
            row = self.filledCircles[index]
            centerX = col * self.cellwidth + 35
            centerY = row * self.cellheight + 35
            print("Clicked col: {}, row: {}".format(col, row))
            item = self.canvas.find_closest(centerX, centerY)
            if "oval" in self.canvas.itemcget(item, "tags"):
                color = "yellow" if self.startingColor else "red"
                self.startingColor = 1 - self.startingColor
                self.mapped[row][col] = "y" if color == "yellow" else "r"
                self.canvas.itemconfig(item, fill = color)
            self.filledCircles[index] -= 1
            #if self.numTurns >= 7:
            self.check_sequence(col, row, -1, 0)

        #self.clicked = True
        print(numpy.matrix(self.mapped))


if __name__ == "__main__":
    game = ConnectFour()
    game.title("Connect4")
    game.mainloop()
