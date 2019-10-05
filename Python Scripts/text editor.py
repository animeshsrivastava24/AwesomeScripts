from tkinter import *
from tkinter import ttk
#import tkfilebrowser




class main:
    def __init__(self, master):
        self.master = master

        self.text = Text(self.master)
        self.text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        button = ttk.Button(self.master, text='Save', command = self.saveas)
        button.grid(row=0, column=2, sticky='sw')

        self.font = Menubutton(self.master, text = 'Font', pady=10)
        self.font.grid(row=0, column=0, sticky='sw')
        self.font.menu = Menu(self.font, tearoff = 0)
        self.font["menu"] = self.font.menu
        self.helvetica = IntVar()
        self.courier = IntVar()
        self.impact = IntVar()
        self.roman = IntVar()
        self.georgia = IntVar()
        self.font.menu.add_checkbutton(label="Courier", variable=self.courier, command=self.FontCourier)
        self.font.menu.add_checkbutton(label="Helvetica", variable=self.helvetica, command=self.FontHelvetica)
        self.font.menu.add_checkbutton(label="Impact", variable=self.impact, command=self.FontImpact)
        self.font.menu.add_checkbutton(label="Roman", variable=self.roman, command=self.FontRoman)
        self.font.menu.add_checkbutton(label="Georgia", variable=self.georgia, command=self.FontGeorgia)

        self.font_size = Menubutton(self.master, text = 'Font Size', pady=10)
        self.font_size.grid(row=0, column=1, sticky='sw')
        self.font_size.menu = Menu(self.font_size, tearoff = 0)
        self.font_size["menu"] = self.font_size.menu
        self.Twelve = IntVar()
        self.Twentytwo = IntVar()
        self.Twentysix = IntVar()
        self.Thirty = IntVar()
        self.Thirtyfour = IntVar()
        self.font_size.menu.add_checkbutton(label = '12', variable = self.Twelve, command = self.Font_twelve)
        self.font_size.menu.add_checkbutton(label = '22', variable = self.Twentytwo, command = self.Font_twentytwo)
        self.font_size.menu.add_checkbutton(label='26', variable=self.Twentysix, command=self.Font_twentysix)
        self.font_size.menu.add_checkbutton(label='30', variable=self.Thirty, command=self.Font_thirty)
        self.font_size.menu.add_checkbutton(label='34', variable=self.Thirtyfour, command=self.Font_thirtyfour)

        button2 = ttk.Button(self.master, command = self.closewindow, text='Exit').grid(row=2, column=0, columnspan=3)

    def closewindow(self):
        root.destroy()


    def saveas(self):
        t = self.text.get("1.0", "end-1c")
        savelocation = tkfilebrowser.asksaveasfilename()
        file1 = open(savelocation, "w+")
        file1.write(t)
        file1.close()

    def FontHelvetica(self):
        self.text.config(font=("Helvetica"))

    def FontCourier(self):
        self.text.config(font=("Courier"))

    def FontImpact(self):
        self.text.config(font=("Impact"))

    def FontRoman(self):
        self.text.config(font=("Roman"))

    def FontGeorgia(self):
        self.text.config(font=("Georgia"))

    def Font_twelve(self):
        self.text.config(font = ('arial', 12))

    def Font_twentytwo(self):
        self.text.config(font = ('arial', 22))

    def Font_twentysix(self):
        self.text.config(font = ('arial', 26))

    def Font_thirty(self):
        self.text.config(font = ('arial', 30))

    def Font_thirtyfour(self):
        self.text.config(font = ('arial', 34))




root = Tk()
root.title('Text Editor')
main(root)
root.mainloop()

