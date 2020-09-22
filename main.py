import Tkinter as tk

class ConnectFour(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=490, height=490, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.cellwidth = 70
        self.cellheight = 70
        self.clicked = False
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

    def on_hover(self, event):
        if not self.clicked:
            print(event.x, event.y)

    def on_click(self, event):
        x = event.x
        y = event.y
        item = self.canvas.find_closest(x, y)
        #type = self.canvas.type(item)
        tag = self.canvas.itemcget(item, "tags")
        if "oval" in tag:
            print("Found oval")
            self.canvas.itemconfig(item, fill = "yellow")
        self.clicked = True
        print("Clicked: {},{}".format(event.x, event.y))
        #print(event.x, event.y)

if __name__ == "__main__":
    game = ConnectFour()
    game.mainloop()
