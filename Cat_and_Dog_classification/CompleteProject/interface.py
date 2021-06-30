import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
import time
from tkinter import colorchooser, filedialog, messagebox
from tkinter.filedialog import asksaveasfilename
import PIL.ImageGrab as ImageGrab
import os


window = Tk()

window.title('Cat and Dog Classification')
window.configure(bg='#ED9850')
window.geometry("900x600+300+50")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

lb1 = tkinter.Label(text="Cat and Dog Classification", bg="#DA902D", relief="solid",
      height=2, font="Times%New%Roman 18 bold italic", anchor=CENTER)
lb1.pack(side=TOP, fill=BOTH)

window.mainloop()