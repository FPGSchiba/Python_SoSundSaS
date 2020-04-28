# SoS und SaS Projects Presents: TikTakToe
# Author: Jann Erhardt
# Version: 1.2
# Changes:
# ======================================================================================
#
# 15.04.2020 --> Cross und Circle ohne abwechslung
# 16.04.2020 --> Spiel Logik angefangen
# 16.04.2020 --> Gewinn Mechanismus impementiert (Worm.exe ebenfalls implementiert xD)
# 17.04.2020 --> Fix GitHub fail
# 28.04.2020 --> Win eingebaut
#
# ======================================================================================
# initate worm.explode(dest=all, 10)
from tkinter import *
from YouWon import *


def getCount():
    global count
    count += 1
    return count


def OnButtonEnter(button):
    # wert hat was gesetzt
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    global tlset
    global tmset
    global trset
    global mlset
    global mmset
    global mrset
    global blset
    global bmset
    global brset

    crosspoint = 100
    scirclepoint = 95
    ecirclepoint = 5
    zahl = getCount()
    if button == "tl" and not tl:
        tl = True
        if zahl % 2 == 1:
            tlset = 'Kreuz'
            canTopLeft.create_line(0, 0, crosspoint, crosspoint, fill=color, width=5)
            canTopLeft.create_line(crosspoint, 0, 0, crosspoint, fill=color, width=5)
        else:
            tlset = 'Kreis'
            canTopLeft.create_oval(ecirclepoint, ecirclepoint, scirclepoint, scirclepoint, width=5)
    elif button == "tm" and not tm:
        tm = True

        if zahl % 2 == 1:
            tmset = 'Kreuz'
            canTopMid.create_line(0, 0, crosspoint, crosspoint, fill=color, width=5)
            canTopMid.create_line(crosspoint, 0, 0, crosspoint, fill=color, width=5)
        else:
            tmset = 'Kreis'
            canTopMid.create_oval(ecirclepoint, ecirclepoint, scirclepoint, scirclepoint, width=5)
    elif button == "tr" and not tr:
        tr = True

        if zahl % 2 == 1:
            trset = 'Kreuz'
            canTopRight.create_line(0, 0, crosspoint, crosspoint, fill=color, width=5)
            canTopRight.create_line(crosspoint, 0, 0, crosspoint, fill=color, width=5)
        else:
            trset = 'Kreis'
            canTopRight.create_oval(ecirclepoint, ecirclepoint, scirclepoint, scirclepoint, width=5)
    elif button == "ml" and not ml:
        ml = True

        if zahl % 2 == 1:
            mlset = 'Kreuz'
            canMidLeft.create_line(0, 0, crosspoint, crosspoint, fill=color, width=5)
            canMidLeft.create_line(crosspoint, 0, 0, crosspoint, fill=color, width=5)
        else:
            mlset = 'Kreis'
            canMidLeft.create_oval(ecirclepoint, ecirclepoint, scirclepoint, scirclepoint, width=5)
    elif button == "mm" and not mm:
        mm = True

        if zahl % 2 == 1:
            mmset = 'Kreuz'
            canMidMid.create_line(0, 0, crosspoint, crosspoint, fill=color, width=5)
            canMidMid.create_line(crosspoint, 0, 0, crosspoint, fill=color, width=5)
        else:
            mmset = 'Kreis'
            canMidMid.create_oval(ecirclepoint, ecirclepoint, scirclepoint, scirclepoint, width=5)
    elif button == "mr" and not mr:
        mr = True

        if zahl % 2 == 1:
            mrset = 'Kreuz'
            canMidRight.create_line(0, 0, crosspoint, crosspoint, fill=color, width=5)
            canMidRight.create_line(crosspoint, 0, 0, crosspoint, fill=color, width=5)
        else:
            mrset = 'Kreis'
            canMidRight.create_oval(ecirclepoint, ecirclepoint, scirclepoint, scirclepoint, width=5)
    elif button == "bl" and not bl:
        bl = True

        if zahl % 2 == 1:
            blset = 'Kreuz'
            canBotLeft.create_line(0, 0, crosspoint, crosspoint, fill=color, width=5)
            canBotLeft.create_line(crosspoint, 0, 0, crosspoint, fill=color, width=5)
        else:
            blset = 'Kreis'
            canBotLeft.create_oval(ecirclepoint, ecirclepoint, scirclepoint, scirclepoint, width=5)
    elif button == "bm" and not bm:
        bm = True

        if zahl % 2 == 1:
            bmset = 'Kreuz'
            canBotMid.create_line(0, 0, crosspoint, crosspoint, fill=color, width=5)
            canBotMid.create_line(crosspoint, 0, 0, crosspoint, fill=color, width=5)
        else:
            bmset = 'Kreis'
            canBotMid.create_oval(ecirclepoint, ecirclepoint, scirclepoint, scirclepoint, width=5)
    elif button == "br" and not br:
        br = True

        if zahl % 2 == 1:
            brset = 'Kreuz'
            canBotRight.create_line(0, 0, crosspoint, crosspoint, fill=color, width=5)
            canBotRight.create_line(crosspoint, 0, 0, crosspoint, fill=color, width=5)
        else:
            brset = 'Kreis'
            canBotRight.create_oval(ecirclepoint, ecirclepoint, scirclepoint, scirclepoint, width=5)

    if tl and tm and tr:
        if tlset == 'Kreuz' and tmset == 'Kreuz' and trset == 'Kreuz':
            YouWon("Kreuz")

        elif tlset == 'Kreis' and tmset == 'Kreis' and trset == 'Kreis':
            YouWon("Kreis")

    if ml and mm and mr:
        if mlset == 'Kreuz' and mmset == 'Kreuz' and mrset == 'Kreuz':
            YouWon("Kreuz")

        elif mlset == 'Kreis' and mmset == 'Kreis' and mrset == 'Kreis':
            YouWon("Kreis")

    if bl and bm and br:
        if blset == 'Kreuz' and bmset == 'Kreuz' and brset == 'Kreuz':
            YouWon("Kreuz")

        elif blset == 'Kreis' and bmset == 'Kreis' and brset == 'Kreis':
            YouWon("Kreis")

    if tr and mr and br:
        if trset == 'Kreuz' and mrset == 'Kreuz' and brset == 'Kreuz':
            YouWon("Kreuz")

        elif trset == 'Kreis' and mrset == 'Kreis' and brset == 'Kreis':
            YouWon("Kreis")

    if tm and mm and bm:
        if tmset == 'Kreuz' and mmset == 'Kreuz' and bmset == 'Kreuz':
            YouWon("Kreuz")

        elif tmset == 'Kreis' and mmset == 'Kreis' and bmset == 'Kreis':
            YouWon("Kreis")

    if tl and ml and bl:
        if tlset == 'Kreuz' and mlset == 'Kreuz' and blset == 'Kreuz':
            YouWon("Kreuz")

        elif tlset == 'Kreis' and mlset == 'Kreis' and blset == 'Kreis':
            YouWon("Kreis")

    if tr and mm and bl:
        if trset == 'Kreuz' and mmset == 'Kreuz' and blset == 'Kreuz':
            YouWon("Kreuz")

        elif trset == 'Kreis' and mmset == 'Kreis' and blset == 'Kreis':
            YouWon("Kreis")
    if tl and mm and br:
        if tlset == 'Kreuz' and mmset == 'Kreuz' and brset == 'Kreuz':
            YouWon("Kreuz")

        elif tlset == 'Kreis' and mmset == 'Kreis' and brset == 'Kreis':
            YouWon("Kreis")


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
    B_topLeft.place(x=200, y=425)
    B_topMid.place(x=250, y=425)
    B_topRight.place(x=300, y=425)
    B_midLeft.place(x=200, y=475)
    B_midMid.place(x=250, y=475)
    B_midRight.place(x=300, y=475)
    B_botLeft.place(x=200, y=525)
    B_botMid.place(x=250, y=525)
    B_botRight.place(x=300, y=525)
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

tlset = ''
tmset = ''
trset = ''
mlset = ''
mmset = ''
mrset = ''
blset = ''
bmset = ''
brset = ''
height = 2
width = 4
color = "black"
can_color = "orange"
can_size = 100
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
