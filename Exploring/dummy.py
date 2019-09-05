import tkinter

window = tkinter.Tk()
window.title("Guessing Game")

canvas1 = tkinter.Canvas(window, width=400, height=300)
canvas1.pack()

entry1 = tkinter.Entry(window)
canvas1.create_window(200, 140, window=entry1)


def getSquareRoot():
    x1 = entry1.get()

    label1 = tkinter.Label(window, text=float(x1) ** 0.5)
    canvas1.create_window(200, 230, window=label1)


button1 = tkinter.Button(text='Get the Square Root', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

window.mainloop()

if __name__ == "__main__":
    getSquareRoot()
