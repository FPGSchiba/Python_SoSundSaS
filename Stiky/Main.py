# Version 1.0# Author: Jann Erhardt# Changes:==============================## Init: 03.06.2020## ======================================## Notes:================================## Notes here## ======================================import osfrom tkinter import *from ReadWrite import *def killme():    root.quit()    root.destroy()def test():    write("der Test \n")    killme()def Start():    print(read())Start()root = Tk()root.geometry('10x10+0+0')lb = Text(root, width=16, height=5)yscrollbar = Scrollbar(root, orient=VERTICAL, command=lb.yview)yscrollbar.pack(side=RIGHT, fill=Y)lb["yscrollcommand"] = yscrollbar.setlb.pack(side=LEFT, fill=BOTH, expand=YES)root.geometry('400x400+0+0')root.protocol("WM_DELETE_WINDOW", test)root.mainloop()