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
window.configure(bg='#0C85DC')
window.geometry("900x600+300+50")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)



window.mainloop()