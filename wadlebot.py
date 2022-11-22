from customtkinter import *
from tkinter import *
from tkinter import scrolledtext as st
from PIL import Image, ImageTk
class app:
    def __init__(self):
        self.croot = CTk()
        self.croot.set_appearance_mode("dark")
        self.croot.title("Wadle Bot")
        self.croot.geometry("360x500")
        self.croot.resizable(False, False)
        self.croot.iconbitmap("wadle.ico")
        with Image.open("wadle.png") as self.ti:
            self.titleimage = ImageTk.PhotoImage(self.ti)
            self.title = Label(self.croot, image=self.titleimage, bg="black").place(x=118, y=20, width=130, height=70)
    def inletters(self):
        self.lin = CTkButton(self.croot, text="Have Letters:")
        self.lin.place(x=40, y=190)
        self.tin = CTkEntry(self.croot)
        self.tin.place(x=190, y=190)
    def noletters(self):
        self.lno = CTkButton(self.croot, text="Without Letters:")
        self.lno.place(x=40, y=230)
        self.tno = CTkEntry(self.croot)
        self.tno.place(x=190, y=230)
    def instructions(self):
        self.iwin = CTkToplevel(self.croot)
        self.iwin.title("Instructions")
        self.iwin.geometry("300x150")
        self.guide = CTkLabel(self.iwin, text='''Type the letter corresponding to it's position in \nthe word into each box.\n\nType each letter seperated by a comma \nthat is not in the word \ninto the "Without Letters" box, \nsame applies to the "Have Letters" box.''')
        self.guide.pack()
    def instructionsbutton(self):
        self.instructionbuttn = CTkButton(self.croot, text="?", height=10, width=10, command=self.instructions)
        self.instructionbuttn.place(x=335, y=0)
    def onletters(self):
        self.fr = Entry(self.croot, font=("Helvetica", 45))
        self.fr.place(x=40, y=100, width=50, height=50)
        self.se = Entry(self.croot, font=("Helvetica", 45))
        self.se.place(x=100, y=100, width=50, height=50)
        self.th = Entry(self.croot, font=("Helvetica", 45))
        self.th.place(x=160, y=100, width=50, height=50)
        self.fo = Entry(self.croot, font=("Helvetica", 45))
        self.fo.place(x=220, y=100, width=50, height=50)
        self.fi = Entry(self.croot, font=("Helvetica", 45))
        self.fi.place(x=280, y=100, width=50, height=50)
    def generate(self):
        try:
            self.results.configure(state="normal")
            self.results.delete("1.0", END)
            self.results.configure(state="disable")
        except:
            pass
        self.charpos = [self.fr.get(), self.se.get(), self.th.get(), self.fo.get(), self.fi.get()]
        self.charposlen = 0
        self.charposhave = 0
        self.badlist = False
        self.badword = False
        self.noletterslist = self.tno.get().split(",")
        self.inletterslist = self.tin.get().split(",")
        if len(self.fr.get()) > 1 or len(self.se.get()) > 1 or len(self.th.get()) > 1 or len(self.fo.get()) > 1 or len(self.fi.get()) > 1:
            self.badlist = True
        elif not len(self.noletterslist) < 22 or len(self.inletterslist) > 5:
            self.badlist = True
        for nl in self.noletterslist:
            if nl in self.charpos and nl != '' or nl in self.inletterslist and nl != '':
                self.badlist = True

        if self.badlist == False:
            for char in self.charpos:
                if char != "":
                    self.charposlen += 1
            with open("words.txt", "r") as self.openfile:
                self.allwords = self.openfile.read()
                self.allwords = self.allwords.split('\n')
                for words in self.allwords:
                    self.badword = False
                    self.charposhave = 0
                    for nol in self.noletterslist:
                        if nol in words and nol != '':
                            self.badword = True
                    for inl in self.inletterslist:
                        if inl not in words and inl != '':
                            print(inl, words)
                            self.badword = True
                    for ind in range(5):
                        if self.charpos[ind] != words[ind] and self.charpos[ind] != '':
                            self.badword = True
                        else:
                            self.charposhave += 1
                    if self.charposhave < self.charposlen:
                        self.badword = True
                    if self.badword == False:
                        self.results.config(state="normal")
                        self.results.insert(INSERT, f"[+]Possible Word: {words}\n")
                        self.results.config(state="disable")
                self.openfile.close()


    def generatewidgets(self):
        self.results = st.ScrolledText(self.croot, height=5, width=34, state="disable")
        self.results.place(x=40, y=370)
        self.genbutton = CTkButton(self.croot, text="Generate", height=70, width=290, command=self.generate).place(x=40, y=280)
    def start(self):
        self.inletters()
        self.onletters()
        self.noletters()
        self.generatewidgets()
        self.instructionsbutton()
        self.croot.mainloop()
mn = app()
mn.start()