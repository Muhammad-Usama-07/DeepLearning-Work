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
window.geometry("500x600+300+50")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

lb1 = tkinter.Label(text="Cat and Dog Classification", bg="#DA902D", relief="solid",
      height=1, font="Times%New%Roman 18 bold italic", anchor=CENTER)
lb1.pack(side=TOP, fill=BOTH)

lb2 = tkinter.Label(text="Give me image", bg="#ED9850", font="Times%New%Roman 20 bold italic", anchor=CENTER)
lb2.place(relx=0.5, rely=0.2, anchor=CENTER)

predict_button = tkinter.Button(text="Predict", bg='#DA902D', width=7,
                        font=("Times%New%Roman", 15, "bold"),
                        relief="solid")
predict_button.place(relx=0.4, rely=0.8, anchor=CENTER)
clear_button = tkinter.Button(text='Upload', bg='#DA902D', width=7,
                      font=("Times%New%Roman", 15, "bold"),
                      relief="solid")
clear_button.place(relx=0.6, rely=0.8, anchor=CENTER)

window.mainloop()