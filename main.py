import Tkinter as tk
import random

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
        self.bind("<Motion>", self.on_hover)
        self.bind("<Button-1>", self.on_click)

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
        if not self.clicked:
            print(event.x, event.y)

    def on_click(self, event):
        x = event.x
        y = event.y
        index = self.get_column(x)
        print("Index: {}".format(index))
        if self.filledCircles[index] > -1:
            centerX = index * self.cellwidth + 35
            centerY = self.filledCircles[index] * self.cellheight + 35
            item = self.canvas.find_closest(centerX, centerY)
            if "oval" in self.canvas.itemcget(item, "tags"):
                color = "yellow" if self.startingColor else "red"
                self.startingColor = 1 - self.startingColor
                self.canvas.itemconfig(item, fill = color)
            self.filledCircles[index] -= 1
        self.clicked = True
        print("Clicked: {},{}".format(event.x, event.y))

if __name__ == "__main__":
    game = ConnectFour()
    game.mainloop()
