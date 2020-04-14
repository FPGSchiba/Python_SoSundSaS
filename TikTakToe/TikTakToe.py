# SoS und SaS Projects Presents: TikTakToe

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("600x600")
top.title('Tik Tak Toe')
height = 13
width = 33
color = "black"


def TopLeft(event):
    msg = messagebox.showinfo("Top Left", "Top Left Pressed")


def TopMid(event):
    msg = messagebox.showinfo("Top Mid", "Top Mid Pressed")


def TopRight(event):
    msg = messagebox.showinfo("Top Right", "Top Right Pressed")


def MidLeft(event):
    msg = messagebox.showinfo("Mid Left", "Mid Left Pressed")


def MidMid(event):
    msg = messagebox.showinfo("Mid Mid", "Mid Mid Pressed")


def MidRigth(event):
    msg = messagebox.showinfo("Mid Right", "Mid Right Pressed")


def BotLeft(event):
    msg = messagebox.showinfo("Bot Left", "Bot Left Pressed")


def BotMid(event):
    msg = messagebox.showinfo("Bot Mid", "Bot Mid Pressed")


def BotRight(event):
    msg = messagebox.showinfo("Bot Right", "Bot Right Pressed")


top.maxsize(600, 600)
top.minsize(600, 600)
B_topLeft = Button(top, height=height, width=width, bg=color)
B_topMid = Button(top, height=height, width=width, bg=color)
B_topRight = Button(top, height=height, width=width, bg=color)
B_midLeft = Button(top, height=height, width=width, bg=color)
B_midMid = Button(top, height=height, width=width, bg=color)
B_midRight = Button(top, height=height, width=width, bg=color)
B_botLeft = Button(top, height=height, width=width, bg=color)
B_botMid = Button(top, height=height, width=width, bg=color)
B_botRight = Button(top, height=height, width=width, bg=color)
B_topLeft.place(x=0, y=0)
B_topMid.place(x=200, y=0)
B_topRight.place(x=400, y=0)
B_midLeft.place(x=0, y=200)
B_midMid.place(x=200, y=200)
B_midRight.place(x=400, y=200)
B_botLeft.place(x=0, y=400)
B_botMid.place(x=200, y=400)
B_botRight.place(x=400, y=400)
B_topLeft.bind('<Button-1>', TopLeft)
B_topMid.bind('<Button-1>', TopMid)
B_topRight.bind('<Button-1>', TopRight)
B_midLeft.bind('<Button-1>', MidLeft)
B_midMid.bind('<Button-1>', MidMid)
B_midRight.bind('<Button-1>', MidRigth)
B_botLeft.bind('<Button-1>', BotLeft)
B_botMid.bind('<Button-1>', BotMid)
B_botRight.bind('<Button-1>', BotRight)
top.mainloop()
