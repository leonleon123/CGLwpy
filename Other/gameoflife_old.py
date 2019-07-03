import tkinter as tk
import time

n = 50
tileSize = 20
w = n*tileSize
h = w
run_check = False
main_color = "grey28"
square_color = "white"

arr = [[0 for y in range(n+2)] for x in range(n+2)]
arrCpy = [[0 for y in range(n+2)] for x in range(n+2)]

def checkSquares(x,y, arr):
    num = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not (i==x and j==y):
                num = num + arr[i][j]
    return num 
    
def Run():
    global arr
    global arrCpy
    global run_check
    speed = slider.get()
    canvas.delete("temp")
    for i in range(n):
        for j in range(n):
            num = checkSquares(i,j, arr)
            if arr[i][j]==1 and (num<2 or num >= 4): 
                arrCpy[i][j] = 0
                canvas.create_rectangle(i*tileSize, j*tileSize, i*tileSize+tileSize, j*tileSize+tileSize, 
                                    fill=main_color, width=0, tags="temp")
            elif arr[i][j]==1: 
                arrCpy[i][j] = 1
                canvas.create_rectangle(i*tileSize, j*tileSize, i*tileSize+tileSize, j*tileSize+tileSize, 
                                    fill=square_color, width=0, tags="temp")
            elif arr[i][j]==0 and num==3: 
                arrCpy[i][j] = 1
                canvas.create_rectangle(i*tileSize, j*tileSize, i*tileSize+tileSize, j*tileSize+tileSize, 
                                    fill=square_color, width=0, tags="temp")
    arr = arrCpy.copy()
    arrCpy = [[0 for y in range(n+2)] for x in range(n+2)]
    if run_check:
        run_check = False
        return
    canvas.after(speed, Run)

def Clear():
    global arr
    global arrCpy
    global run_check
    canvas.delete("all")
    arr = [[0 for y in range(n+2)] for x in range(n+2)]
    arrCpy = [[0 for y in range(n+2)] for x in range(n+2)]
    drawSquares(arrCpy)
    run_check = True

def Stop():
    global run_check
    run_check = True

def drawSquares(arr_in):
    for i in range(n):
        for j in range(n):
            color = square_color if arr_in[i][j] else main_color
            canvas.create_rectangle(i*tileSize, j*tileSize, i*tileSize+tileSize, j*tileSize+tileSize, 
                                    fill=color, width=0)

def drawSingleSquare(event):
    x = int(event.x/tileSize)
    y = int(event.y/tileSize)
    if arr[x][y] == 0:
        arr[x][y] = 1
        color = square_color
    else:
        arr[x][y] = 0
        color = main_color
    xsize = x * tileSize
    ysize = y * tileSize
    canvas.create_rectangle(xsize, ysize, xsize+tileSize, ysize+tileSize, fill=color, width=0, tags="temp")

master = tk.Tk(className="Game of life")
master.configure(background=main_color)

canvas = tk.Canvas(master,width=w, height=h)
canvas.pack(fill="both", expand=True)


button_run = tk.Button(master, text="Run", command=Run, relief="flat",
                            background=main_color, foreground="white")
button_run.pack()

button_restart = tk.Button(master, text="Restart", command=Clear, relief="flat",
                            background=main_color, foreground="white")
button_restart.pack()

button_restart = tk.Button(master, text="Stop", command=Stop, relief="flat",
                            background=main_color, foreground="white")
button_restart.pack()

slider = tk.Scale(master, from_=1000, to=1, variable=30, orient="horizontal",
                            background=main_color, foreground="white")
slider.pack()

canvas.bind("<Button-1>", drawSingleSquare)
drawSquares(arr)
       
canvas.mainloop()