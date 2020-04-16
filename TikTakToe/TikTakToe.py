# SoS und SaS Projects Presents: TikTakToe
# Author: Jann Erhardt
# Version: 1.1
# Changes:
# ======================================
# 15.04.2020 --> Cross und Circle ohne abwechslung
# 16.04.2020 --> Spiel Logik angefangen

from tkinter import *


def getCount():
    global count
    count += 1
    return count


def OnButtonEnter(button):
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    _count = getCount()
    if button == "tl" and not tl:
        tl = True
        if _count % 2 == 1:
            canTopLeft.create_line(0, 0, 200, 200, fill=color, width=5)
            canTopLeft.create_line(200, 0, 0, 200, fill=color, width=5)
        else:
            canTopLeft.create_oval(10, 10, 190, 190, width=5)
    elif button == "tm" and not tm:
        tm = True
        if _count % 2 == 1:
            canTopMid.create_line(0, 0, 200, 200, fill=color, width=5)
            canTopMid.create_line(200, 0, 0, 200, fill=color, width=5)
        else:
            canTopMid.create_oval(10, 10, 190, 190, width=5)
    elif button == "tr" and not tr:
        tr = True
        if _count % 2 == 1:
            canTopRight.create_line(0, 0, 200, 200, fill=color, width=5)
            canTopRight.create_line(200, 0, 0, 200, fill=color, width=5)
        else:
            canTopRight.create_oval(10, 10, 190, 190, width=5)
    elif button == "ml" and not ml:
        ml = True
        if _count % 2 == 1:
            canMidLeft.create_line(0, 0, 200, 200, fill=color, width=5)
            canMidLeft.create_line(200, 0, 0, 200, fill=color, width=5)
        else:
            canMidLeft.create_oval(10, 10, 190, 190, width=5)
    elif button == "mm" and not mm:
        mm = True
        if _count % 2 == 1:
            canMidMid.create_line(0, 0, 200, 200, fill=color, width=5)
            canMidMid.create_line(200, 0, 0, 200, fill=color, width=5)
        else:
            canMidMid.create_oval(10, 10, 190, 190, width=5)
    elif button == "mr" and not mr:
        mr = True
        if _count % 2 == 1:
            canMidRight.create_line(0, 0, 200, 200, fill=color, width=5)
            canMidRight.create_line(200, 0, 0, 200, fill=color, width=5)
        else:
            canMidRight.create_oval(10, 10, 190, 190, width=5)
    elif button == "bl" and not bl:
        bl = True
        if _count % 2 == 1:
            canBotLeft.create_line(0, 0, 200, 200, fill=color, width=5)
            canBotLeft.create_line(200, 0, 0, 200, fill=color, width=5)
        else:
            canBotLeft.create_oval(10, 10, 190, 190, width=5)
    elif button == "bm" and not bm:
        bm = True
        if _count % 2 == 1:
            canBotMid.create_line(0, 0, 200, 200, fill=color, width=5)
            canBotMid.create_line(200, 0, 0, 200, fill=color, width=5)
        else:
            canBotMid.create_oval(10, 10, 190, 190, width=5)
    elif button == "br" and not br:
        br = True
        if _count % 2 == 1:
            canBotRight.create_line(0, 0, 200, 200, fill=color, width=5)
            canBotRight.create_line(200, 0, 0, 200, fill=color, width=5)
        else:
            canBotRight.create_oval(10, 10, 190, 190, width=5)


def InitialiseComponents():
    top.maxsize(600, 800)
    top.minsize(600, 800)
    B_topLeft = Button(top, height=height, width=width, bg=color, command=lambda: OnButtonEnter("tl"))
    B_topMid = Button(top, height=height, width=width, bg=color, command=lambda: OnButtonEnter("tm"))
    B_topRight = Button(top, height=height, width=width, bg=color, command=lambda: OnButtonEnter("tr"))
    B_midLeft = Button(top, height=height, width=width, bg=color, command=lambda: OnButtonEnter("ml"))
    B_midMid = Button(top, height=height, width=width, bg=color, command=lambda: OnButtonEnter("mm"))
    B_midRight = Button(top, height=height, width=width, bg=color, command=lambda: OnButtonEnter("mr"))
    B_botLeft = Button(top, height=height, width=width, bg=color, command=lambda: OnButtonEnter("bl"))
    B_botMid = Button(top, height=height, width=width, bg=color, command=lambda: OnButtonEnter("bm"))
    B_botRight = Button(top, height=height, width=width, bg=color, command=lambda: OnButtonEnter("br"))
    B_topLeft.place(x=200, y=625)
    B_topMid.place(x=250, y=625)
    B_topRight.place(x=300, y=625)
    B_midLeft.place(x=200, y=675)
    B_midMid.place(x=250, y=675)
    B_midRight.place(x=300, y=675)
    B_botLeft.place(x=200, y=725)
    B_botMid.place(x=250, y=725)
    B_botRight.place(x=300, y=725)
    top.mainloop()


top = Tk()
top.title('Tik Tak Toe')
count = 0
tl = False
tm = False
tr = False
ml = False
mm = False
mr = False
bl = False
bm = False
br = False
height = 2
width = 4
color = "black"
can_color = "orange"
can_size = 200
canTopLeft = Canvas(top, width=can_size, height=can_size, background=can_color)
canTopLeft.grid(row=0, column=0)
canTopMid = Canvas(top, width=can_size, height=can_size, background=can_color)
canTopMid.grid(row=0, column=1)
canTopRight = Canvas(top, width=can_size, height=can_size, background=can_color)
canTopRight.grid(row=0, column=2)
canMidLeft = Canvas(top, width=can_size, height=can_size, background=can_color)
canMidLeft.grid(row=1, column=0)
canMidMid = Canvas(top, width=can_size, height=can_size, background=can_color)
canMidMid.grid(row=1, column=1)
canMidRight = Canvas(top, width=can_size, height=can_size, background=can_color)
canMidRight.grid(row=1, column=2)
canBotLeft = Canvas(top, width=can_size, height=can_size, background=can_color)
canBotLeft.grid(row=2, column=0)
canBotMid = Canvas(top, width=can_size, height=can_size, background=can_color)
canBotMid.grid(row=2, column=1)
canBotRight = Canvas(top, width=can_size, height=can_size, background=can_color)
canBotRight.grid(row=2, column=2)
InitialiseComponents()
