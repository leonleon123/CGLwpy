import tkinter as tk
import time

class App:
    def __init__(self):
        self.n = 50
        self.tileSize = 15
        self.w = self.n*self.tileSize
        self.h = self.w
        self.run_check = False
        self.main_color = "grey28"
        self.square_color = "white"
        self.arr = [[0 for y in range(self.n+2)] for x in range(self.n+2)]
        self.arrCpy = [[0 for y in range(self.n+2)] for x in range(self.n+2)]

        self.master = tk.Tk(className="Game of life")
        self.master.configure(background=self.main_color)

        self.canvas = tk.Canvas(self.master,width=self.w, height=self.h)
        self.canvas.pack(fill="both", expand=True)
        
        self.drawSquares(self.arr)

        self.button_run = tk.Button(self.master, text="Run", command=self.Run, relief="flat",
                                    background=self.main_color, foreground="white")
        self.button_run.pack()

        self.button_restart = tk.Button(self.master, text="Restart", command=self.Clear, relief="flat",
                                    background=self.main_color, foreground="white")
        self.button_restart.pack()

        self.button_restart = tk.Button(self.master, text="Stop", command=self.Stop, relief="flat",
                                    background=self.main_color, foreground="white")
        self.button_restart.pack()

        self.slider = tk.Scale(self.master, from_=1000, to=1, variable=30, orient="horizontal",
                                    background=self.main_color, foreground="white")
        self.slider.pack()
        
        self.canvas.bind("<Button-1>", self.drawSingleSquare)
        
        self.canvas.mainloop()

    def checkSquares(self, x,y, arr):
        num = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if not (i==x and j==y):
                    num = num + arr[i][j]
        return num 
        
    def Run(self):
        speed = self.slider.get()
        self.canvas.delete("temp")
        for i in range(self.n):
            for j in range(self.n):
                num = self.checkSquares(i,j, self.arr)
                if self.arr[i][j]==1 and (num<2 or num >= 4): 
                    self.arrCpy[i][j] = 0
                    self.canvas.create_rectangle(i*self.tileSize, j*self.tileSize, i*self.tileSize+self.tileSize, j*self.tileSize+self.tileSize, 
                                        fill=self.main_color, width=0, tags="temp")
                elif self.arr[i][j]==1: 
                    self.arrCpy[i][j] = 1
                    self.canvas.create_rectangle(i*self.tileSize, j*self.tileSize, i*self.tileSize+self.tileSize, j*self.tileSize+self.tileSize, 
                                        fill=self.square_color, width=0, tags="temp")
                elif self.arr[i][j]==0 and num==3: 
                    self.arrCpy[i][j] = 1
                    self.canvas.create_rectangle(i*self.tileSize, j*self.tileSize, i*self.tileSize+self.tileSize, j*self.tileSize+self.tileSize, 
                                        fill=self.square_color, width=0, tags="temp")
        self.arr = self.arrCpy.copy()
        self.arrCpy = [[0 for y in range(self.n+2)] for x in range(self.n+2)]
        if self.run_check:
            self.run_check = False
            return
        self.canvas.after(speed, self.Run)

    def Clear(self):
        self.canvas.delete("all")
        self.arr = [[0 for y in range(self.n+2)] for x in range(self.n+2)]
        self.arrCpy = [[0 for y in range(self.n+2)] for x in range(self.n+2)]
        self.drawSquares(self.arrCpy)
        self.run_check = True

    def Stop(self):
        self.run_check = True

    def drawSquares(self, arr_in):
        for i in range(self.n):
            for j in range(self.n):
                color = self.square_color if arr_in[i][j] else self.main_color
                self.canvas.create_rectangle(i*self.tileSize, j*self.tileSize, i*self.tileSize+self.tileSize, j*self.tileSize+self.tileSize, 
                                        fill=color, width=0)

    def drawSingleSquare(self, event):
        x = int(event.x/self.tileSize)
        y = int(event.y/self.tileSize)
        if self.arr[x][y] == 0:
            self.arr[x][y] = 1
            color = self.square_color
        else:
            self.arr[x][y] = 0
            color = self.main_color
        xsize = x * self.tileSize
        ysize = y * self.tileSize
        self.canvas.create_rectangle(xsize, ysize, xsize+self.tileSize, ysize+self.tileSize, fill=color, width=0, tags="temp")

app = App()
