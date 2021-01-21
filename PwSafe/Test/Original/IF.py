# --------------
# Autor: Lukas Meier
# ---------------
from tkinter import *
import tkinter.font as font
import json
import tkinter
import webbrowser
from tkinter import messagebox


def add_pw(root):
    mwpos = "400x500+" + str(root.winfo_x()) + "+" + str(root.winfo_y())

    add_pw.newWindow = Toplevel(root)
    add_pw.newWindow.title("New Password")
    add_pw.newWindow.geometry(mwpos)
    add_pw.newWindow.resizable(False, False)

    root.withdraw()
    add_pw.newWindow.focus_force()

    options = LabelFrame(add_pw.newWindow)
    titlefont = font.Font(family='Helvetica', size=20, weight='bold')
    addpwtitle = tkinter.Label(add_pw.newWindow, text="Add Password", bg="grey", fg="white", padx=99, pady=20)
    addpwtitle["font"] = titlefont
    addpwtitle.grid(row=0, column=0, pady=5, padx=5)
    button_pressed = StringVar()
    button_pressed.set(None)

    Label(options, text="Type a title for your Password").grid(row=0, column=0, padx=10, pady=30)
    title = Entry(options, width=32)
    title.grid(row=0, column=1, pady=30)

    Label(options, text="Type the Password").grid(row=1, column=0, padx=10, pady=30)
    passw = Entry(options, width=32)
    passw.grid(row=1, column=1, pady=30)

    Label(options, text="Optional Website").grid(row=2, column=0, padx=10, pady=30)
    web = Entry(options, width=32)
    web.grid(row=2, column=1, pady=30)

    Label(options, text="Description").grid(row=3, column=0, padx=10, pady=30)
    descript = Entry(options, width=32)
    descript.grid(row=3, column=1, pady=30)

    goahead = Button(options, text="Save", state=tkinter.DISABLED,
                     command=lambda: safepw(str(title.get()), str(web.get()), str(passw.get()), str(descript.get())))
    goahead.grid(row=4, column=1, pady=20)

    options.grid(row=1, column=0)

    repeater = True
    while repeater == True:

        safebt = Button(options, text="Validate Name", command=lambda: button_pressed.set("button pressed"))
        safebt.grid(row=4, column=0, pady=20)
        safebt.wait_variable(button_pressed)

        jsfile = open("../../Data/Passwords.json", "r")
        jsdatar = json.load(jsfile)
        jsfile.close()

        if str(title.get()) == "":
            messagebox.showerror("Name Error", "Name cant be empty")
            button_pressed.set(None)
            goahead.config(state=tkinter.DISABLED)
        else:
            goahead.config(state=tkinter.NORMAL)

        for i in jsdatar:
            if i == str(title.get()):
                messagebox.showerror("Name Error", "Name is already used")
                button_pressed.set(None)
                goahead.config(state=tkinter.DISABLED)
            else:
                goahead.config(state=tkinter.NORMAL)

    add_pw.newWindow.mainloop()


def safepw(name, webs, pw, desc):
    root.deiconify()
    root.geometry("400x500+" + str(add_pw.newWindow.winfo_x()) + "+" + str(add_pw.newWindow.winfo_y()))
    add_pw.newWindow.destroy()

    app_data = {str(name): {
        "name": str(name),
        "website": str(webs),
        "Password": str(pw),
        "Description": str(desc)
    }
    }

    jsdatar.update(app_data)
    jsfile = open("../../Data/Passwords.json", "w")
    json.dump(jsdatar, jsfile)
    jsfile.close()
    pwlist.insert(END, "       " + str(name) + "-----" + str(pw) + "       ")


def edit_pw(root):
    edit_pw.curpw = str(pwlist.curselection()).replace(",", "").replace("(", "").replace(")", "")
    if len(edit_pw.curpw) == 0:
        return

    listitem = pwlist.get(ANCHOR)
    listitem = str(listitem).split("-", 1)
    edit_pw.curpwname = listitem[0]
    edit_pw.curpwname = edit_pw.curpwname[7:]

    jsfile = open("../../Data/Passwords.json", "r")
    jsdatar = json.load(jsfile)
    jsfile.close()

    defname = jsdatar[edit_pw.curpwname]["name"]
    defpw = jsdatar[edit_pw.curpwname]["Password"]
    defweb = jsdatar[edit_pw.curpwname]["website"]
    defdesc = jsdatar[edit_pw.curpwname]["Description"]

    mwpos = "400x500+" + str(root.winfo_x()) + "+" + str(root.winfo_y())

    newWindow = Toplevel(root)
    newWindow.title("New Password")
    newWindow.geometry(mwpos)
    newWindow.resizable(False, False)

    root.withdraw()
    newWindow.focus_force()

    options = LabelFrame(newWindow)
    titlefont = font.Font(family='Helvetica', size=20, weight='bold')
    edpwtitle = tkinter.Label(newWindow, text="Edit Password", bg="grey", fg="white", padx=99, pady=20)
    edpwtitle["font"] = titlefont
    edpwtitle.grid(row=0, column=0, pady=5, padx=5)

    Label(options, text="Type a title for your Password").grid(row=0, column=0, padx=10, pady=30)
    edit_pw.n = Entry(options, width=32)
    edit_pw.n.insert(END, defname)
    edit_pw.n.grid(row=0, column=1, pady=30)

    Label(options, text="Type the Password").grid(row=1, column=0, padx=10, pady=30)
    edit_pw.p = Entry(options, width=32)
    edit_pw.p.insert(END, defpw)
    edit_pw.p.grid(row=1, column=1, pady=30)

    Label(options, text="Optional Website").grid(row=2, column=0, padx=10, pady=30)
    edit_pw.w = Entry(options, width=32)
    edit_pw.w.insert(END, defweb)
    edit_pw.w.grid(row=2, column=1, pady=30)

    Label(options, text="Description").grid(row=3, column=0, padx=10, pady=30)
    edit_pw.d = Entry(options, width=32)
    edit_pw.d.insert(END, defdesc)
    edit_pw.d.grid(row=3, column=1, pady=30)

    Button(options, text="Save", command=lambda: [root.deiconify(), updpw(), root.geometry("400x500+" + str(newWindow.winfo_x()) + "+" + str(newWindow.winfo_y())), newWindow.destroy()]).grid(row=4, column=0, pady=20), options.grid(row=1, column=0)


def updpw():
    jsfile = open("../../Data/Passwords.json", "r")
    jsdatar = json.load(jsfile)
    jsfile.close()

    updname = edit_pw.n.get()
    updpass = edit_pw.p.get()
    updweb = edit_pw.w.get()
    upddes = edit_pw.d.get()

    jsdatar[updname] = jsdatar.pop(edit_pw.curpwname)

    jsdatar[updname]["name"] = str(updname)
    jsdatar[updname]["Password"] = str(updpass)
    jsdatar[updname]["website"] = str(updweb)
    jsdatar[updname]["Description"] = str(upddes)

    jsfile = open("../../Data/Passwords.json", "w")
    json.dump(jsdatar, jsfile)
    jsfile.close()

    pwlist.delete(ANCHOR)
    pwlist.insert(edit_pw.curpw, "       " + str(updname) + "-----" + str(updpass + "       "))


def del_pw(list):
    curpw = (pwlist.curselection())
    if len(curpw) == 0:
        return

    listitem = pwlist.get(ANCHOR)
    listitem = str(listitem).split("-", 1)
    curpwname = listitem[0]
    curpwname = curpwname[7:]

    list.delete(ANCHOR)

    jsfile = open("../../Data/Passwords.json", "r")
    jsdatar = json.load(jsfile)
    jsfile.close()

    jsfile = open("../../Data/Passwords.json", "w")
    jsdatar.pop(curpwname)
    json.dump(jsdatar, jsfile)
    jsfile.close()


def login():
    edit_pw.curpw = str(pwlist.curselection()).replace(",", "").replace("(", "").replace(")", "")
    if len(edit_pw.curpw) == 0:
        return

    jsfile = open("../../Data/Passwords.json", "r")
    jsdatar = json.load(jsfile)
    jsfile.close()

    listitem = pwlist.get(ANCHOR)
    listitem = str(listitem).split("-", 1)
    listitem = listitem[0]
    listitem = listitem[7:]
    print(listitem)
    website = jsdatar[str(listitem)]["website"]
    webbrowser.open(str(website))


# -------------Main Interface--------

root = Tk()
root.title("Password Safe")
root.resizable(False, False)
root.geometry("400x500")

titlefont = font.Font(family='Helvetica', size=20, weight='bold')
pwfont = font.Font(family='Helvetica', size=10)

title = Label(root, text="My Passwords", bg="grey", padx=99, pady=20, fg="white")
title['font'] = titlefont

pwframe = Frame(root)
pwframe.grid(row=2, column=0, columnspan=4)

sb = Scrollbar(pwframe, orient=VERTICAL)

pwlist = Listbox(pwframe, width=60, height=20, selectbackground="black", fg="black", selectforeground="white",
                 yscrollcommand=sb.set)
pwlist.bind("<Key>", lambda e: "break")
sb.config(command=pwlist.yview)
sb.pack(side=RIGHT, fill=Y)

jsfile = open("../../Data/Passwords.json", "r")
jsdatar = json.load(jsfile)
jsfile.close()

pwcount = len(jsdatar)
for each in jsdatar:
    pwlist.insert(END, "       " + jsdatar[str(each)]["name"] + "-----" + jsdatar[str(each)]["Password"] + "       ")

pwlist.pack(padx=10, pady=10)

add_btu = Button(root, command=lambda: add_pw(root), text="Add Passwort")
del_btu = Button(root, command=lambda: del_pw(pwlist), text="Delete Passwort")
logn_btu = Button(root, command=lambda: login(), text="Login on Website")
edt_btu = Button(root, command=lambda: edit_pw(root), text="   Details   ")

title.grid(row=0, column=0, pady=5, padx=5, columnspan=4)

add_btu.grid(row=1, column=0, pady=10)
del_btu.grid(row=1, column=1, pady=10)
logn_btu.grid(row=1, column=2, pady=10)
edt_btu.grid(row=1, column=3, pady=10)

jsfile = open("../../Data/Passwords.json", "a")
jsfile.close()
root.mainloop()
