import webbrowser
from tkinter import *
import tkinter.font as font
import json
import threading
from EditThread import *
from AddThread import *


class MainInterface(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.root = Tk()
        self.titleFont = font.Font(family='Helvetica', size=20, weight='bold')
        self.pwFont = font.Font(family='Helvetica', size=10)
        self.pwFrame = Frame(self.root)
        self.sb = Scrollbar(self.pwFrame, orient=VERTICAL)
        self.pwList = Listbox(self.pwFrame, width=60, height=20, selectbackground="black", fg="black", selectforeground="white", yscrollcommand=self.sb.set)
        self.pwFile = open("../../Data/Passwords.json", "r")
        self.pwData = json.load(self.pwFile)
        self.pwFile.close()
        self.pwCount = len(self.pwData)
        self.B_Add = Button(self.root, command=lambda: self.AddPw(), text="Add Passwort")
        self.B_Del = Button(self.root, command=lambda: self.DelPW(), text="Delete Passwort")
        self.B_Login = Button(self.root, command=lambda: self.login(), text="Login on Website")
        self.B_Edit = Button(self.root, command=lambda: self.details(), text="   Details   ")
        self.root.title("Password Safe")
        self.root.resizable(False, False)
        self.root.geometry("400x500")

        self.title = Label(self.root, text="My Passwords", bg="grey", padx=99, pady=20, fg="white")
        self.title['font'] = self.titleFont

        self.pwFrame.grid(row=2, column=0, columnspan=4)

        self.pwList.bind("<Key>", lambda e: "break")
        self.sb.config(command=self.pwList.yview)
        self.sb.pack(side=RIGHT, fill=Y)

        for each in self.pwData:
            self.pwList.insert(END, "       " + self.pwData[str(each)]["name"] + "-----" + self.pwData[str(each)]["Password"] + "       ")

        self.pwList.pack(padx=10, pady=10)

        self.title.grid(row=0, column=0, pady=5, padx=5, columnspan=4)

        self.B_Add.grid(row=1, column=0, pady=10)
        self.B_Del.grid(row=1, column=1, pady=10)
        self.B_Login.grid(row=1, column=2, pady=10)
        self.B_Edit.grid(row=1, column=3, pady=10)

    def login(self):
        if not len(self.getCurrentPassword()) == 0:
            pwFile = open("../../Data/Passwords.json", "r")
            pwData = json.load(pwFile)
            pwFile.close()

            website = pwData[str(str(self.pwList.get(ANCHOR)).split("-", 1)[0][7:])]["website"]
            webbrowser.open(str(website))

    def details(self):
        self.edit = Details(self.pwList)
        self.edit.run()

    def AddPw(self):
        self.add = AddPW(self.pwList)
        self.add.run()

    def getCurrentPassword(self):
        return str(self.pwList.curselection()).replace(",", "").replace("(", "").replace(")", "")

    def getEditedPwList(self):
        self.pwList = self.edit.pwList
        self.pwList.pack()

    def DelPW(self):
        if not len(self.pwList.curselection()) == 0:
            jsFile = open("../../Data/Passwords.json", "r")
            self.pwData = json.load(jsFile)
            jsFile.close()
            jsFile = open("../../Data/Passwords.json", "w")
            self.pwData.pop(str(str(self.pwList.get(ANCHOR)).split("-", 1)[0][7:]))
            json.dump(self.pwData, jsFile)
            jsFile.close()
            self.pwList.delete(ANCHOR)

    def run(self):
        self.root.mainloop()


main = MainInterface()
main.setName("MainIF")
main.run()

