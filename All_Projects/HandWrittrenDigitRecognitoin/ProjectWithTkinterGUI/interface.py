import time
from tkinter import *
from tkinter import colorchooser, filedialog, messagebox
from tkinter.filedialog import asksaveasfilename
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from functools import partial
import PIL.ImageGrab as ImageGrab
import os

window = Tk()


def draw(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill='white', outline='white', width=pen_size)


def clear(strr):
    canvas.delete("all")
    display_result.config(text=strr)

def predict(strr):
    filename = 'image.png'
    x = window.winfo_rootx() + canvas.winfo_x()
    y = window.winfo_rooty() + canvas.winfo_y()

    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    # Image taken
    image = ImageGrab.grab().crop((x, y, x1, y1))
    new_image = image.resize((28, 28))
    new_image.save(filename)


    img = load_img(str(filename), color_mode="grayscale", target_size=(28, 28)) # Loading Image
    img = img_to_array(img) # converting image to array
    img = img.reshape(1, 784)  # reshaping image as model trained.
    img = img.astype('float32')
    img = img / 255.0    # prepare pixel data
    model = models.load_model('TrainedModel.h5')# Load Trained Model
    result = model.predict_classes(img)         # Predicting image
    time.sleep(2)                               # Some time to predict
    display_result.config(text=strr + str(result[0])) # Display result
    os.remove(filename)                         #removing image after prediction

window.title('Handwritten Digit Recognition')
window.configure(bg='#0C85DC')
window.geometry("900x600+300+50")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
photo = PhotoImage(file = "MyLogo.png")
window.iconphoto(False, photo)

Label(window, text=" Handwritten Digit Recognition ", bg="#0065AE", relief="solid",
      height=2, font="Times%New%Roman 18 bold italic", anchor=CENTER).pack(side=TOP, fill=BOTH)

Label(window, text="Draw Digit", bg="#0C85DC",
      height=2, font="Times%New%Roman 18 bold italic", anchor=CENTER).place(relx=0.5, rely=0.2, anchor=CENTER)

canvas = Canvas(window, width=300, height=300, background='black')
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

canvas.bind('<B1-Motion>', draw)

pen_size = 20


result_value = ''
display_result = Label(window, text='the number is: '+result_value, bg="#0065AE", relief="solid",width = 15,
          height=2, font="Times%New%Roman 18 bold italic", anchor=CENTER)
display_result.pack(side=BOTTOM)

predict_button = Button(window, text="Predict", bg='#0065AE', width=8,
                        font=("Times%New%Roman", 15, "bold"),
                        relief="ridge", command=lambda:predict('the number is: '))
predict_button.place(relx=0.4, rely=0.8, anchor=CENTER)
clear_button = Button(window, text='Clear', bg='#0065AE', width=8,
                      font=("Times%New%Roman", 15, "bold"),
                      relief="ridge", command=lambda:clear('the number is: '))
clear_button.place(relx=0.6, rely=0.8, anchor=CENTER)


window.mainloop()
