import threading
from tkinter import *
import tkinter.font as font
import json
import tkinter
from tkinter import messagebox


class Details(threading.Thread):
    def __init__(self, pwList):
        threading.Thread.__init__(self)
        self.pwList = pwList
        self.root = Tk()
        self.currentPW = self.getCurrentPassword()
        if not len(self.currentPW) == 0:
            self.currentPwName = str(self.pwList.get(ANCHOR)).split("-", 1)[0][7:]

            jsFile = open("../../Data/Passwords.json", "r")
            self.pwData = json.load(jsFile)
            jsFile.close()

            self.defName = self.pwData[self.currentPwName]["name"]
            self.defPw = self.pwData[self.currentPwName]["Password"]
            self.defWebsite = self.pwData[self.currentPwName]["website"]
            self.defDescription = self.pwData[self.currentPwName]["Description"]

            self.newPosition = "400x500+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y())

            self.newWindow = Toplevel(self.root)
            self.newWindow.title("New Password")
            self.newWindow.geometry(self.newPosition)
            self.newWindow.resizable(False, False)

            self.root.withdraw()
            self.newWindow.focus_force()

            self.options = LabelFrame(self.newWindow)
            self.titleFont = font.Font(family='Helvetica', size=20, weight='bold')
            self.Title = tkinter.Label(self.newWindow, text="Edit Password", bg="grey", fg="white", padx=99, pady=20)
            self.Title["font"] = self.titleFont
            self.Title.grid(row=0, column=0, pady=5, padx=5)

            Label(self.options, text="Type a title for your Password").grid(row=0, column=0, padx=10, pady=30)
            self.root.n = Entry(self.options, width=32)
            self.root.n.insert(END, self.defName)
            self.root.n.grid(row=0, column=1, pady=30)

            Label(self.options, text="Type the Password").grid(row=1, column=0, padx=10, pady=30)
            self.root.p = Entry(self.options, width=32)
            self.root.p.insert(END, self.defPw)
            self.root.p.grid(row=1, column=1, pady=30)

            Label(self.options, text="Optional Website").grid(row=2, column=0, padx=10, pady=30)
            self.root.w = Entry(self.options, width=32)
            self.root.w.insert(END, self.defWebsite)
            self.root.w.grid(row=2, column=1, pady=30)

            Label(self.options, text="Description").grid(row=3, column=0, padx=10, pady=30)
            self.root.d = Entry(self.options, width=32)
            self.root.d.insert(END, self.defDescription)
            self.root.d.grid(row=3, column=1, pady=30)

            Button(self.options, text="Save", command=lambda: self.updPw()).grid(row=4, column=0, pady=20), self.options.grid(row=1, column=0)

    def updPw(self):
        if not self.NameExists():
            updatedName = self.root.n.get()
            updatedPw = self.root.p.get()
            updatedWebsite = self.root.w.get()
            updatedDescription = self.root.d.get()

            self.pwData[updatedName] = self.pwData.pop(self.currentPwName)

            self.pwData[updatedName]["name"] = str(updatedName)
            self.pwData[updatedName]["Password"] = str(updatedPw)
            self.pwData[updatedName]["website"] = str(updatedWebsite)
            self.pwData[updatedName]["Description"] = str(updatedDescription)

            jsFile = open("../../Data/Passwords.json", "w")
            json.dump(self.pwData, jsFile)
            jsFile.close()

            self.pwList.delete(ANCHOR)
            self.pwList.insert(self.currentPW, "       " + str(updatedName) + "-----" + str(updatedPw + "       "))
            self.root.destroy()
        else:
            messagebox.showerror("Name Exists", "The name already exists for another Password.")

    def run(self):
        if not len(self.currentPW) == 0:
            self.root.mainloop()

    def NameExists(self):
        name = str(self.root.n.get())
        for i in self.pwData:
            if name == i:
                return True
        return False

    def getCurrentPassword(self):
        return str(self.pwList.curselection()).replace(",", "").replace("(", "").replace(")", "")