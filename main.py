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
        # 7 0 1
        # 6 c 2
        # 5 4 3

        # Case 0
        if row > 0:
            pass

        # Case 1
        if col < 6 and row > 0:
            pass

        # Case 2
        if col < 6:
            pass

        # Case 3
        if row < 6 and col < 6:
            pass

        # Case 4
        if row < 6:
            pass

        # Case 5
        if col > 0 and row < 6:
            pass

        # Case 6
        if col > 0:
            pass

        # Case 7
        if col > 0 and row > 0:
            pass

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
            if self.numTurns >= 7:
                self.check_sequence(col, row, -1, 0)

        #self.clicked = True
        print(numpy.matrix(self.mapped))


if __name__ == "__main__":
    game = ConnectFour()
    game.mainloop()
