import threading
from tkinter import *
import tkinter.font as font
import json
import tkinter
from tkinter import messagebox


class AddPW(threading.Thread):
    def __init__(self, pwList):
        threading.Thread.__init__(self)
        self.pwList = pwList
        self.root = Tk()

        jsFile = open("../../Data/Passwords.json", "r")
        self.pwData = json.load(jsFile)
        jsFile.close()

        self.defName = ""
        self.defPw = ""
        self.defWebsite = ""
        self.defDescription = ""

        self.newPosition = "400x500+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y())

        self.newWindow = Toplevel(self.root)
        self.newWindow.title("New Password")
        self.newWindow.geometry(self.newPosition)
        self.newWindow.resizable(False, False)

        self.root.withdraw()
        self.newWindow.focus_force()

        self.options = LabelFrame(self.newWindow)
        self.titleFont = font.Font(family='Helvetica', size=20, weight='bold')
        self.Title = tkinter.Label(self.newWindow, text="Add Password", bg="grey", fg="white", padx=99, pady=20)
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

            Data = {str(updatedName): {
                "name": str(updatedName),
                "website": str(updatedPw),
                "Password": str(updatedWebsite),
                "Description": str(updatedDescription)
                }
            }
            self.pwData.update(Data)

            jsFile = open("../../Data/Passwords.json", "w")
            json.dump(self.pwData, jsFile)
            jsFile.close()

            self.pwList.insert(END, "       " + str(updatedName) + "-----" + str(updatedPw) + "       ")
            self.root.destroy()
        else:
            messagebox.showerror("Name Exists", "The name already exists for another Password.")

    def NameExists(self):
        name = str(self.root.n.get())
        for i in self.pwData:
            if name == i:
                return True
        return False

    def run(self):
        self.root.mainloop()
