import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
import time
from tkinter import colorchooser, filedialog, messagebox
from tkinter import filedialog as fd
import PIL.ImageGrab as ImageGrab
import os
#after
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img

window = Tk()
image_path = 'aaa'


def upload(strr):
    display_result.config(text=strr)
    global image_path
    filename = fd.askopenfilename()
    image_path = filename
    # Getting image
    my_pic = Image.open(image_path)
    # Resizing Image
    global resized
    resized = my_pic.resize((150, 150), Image.ANTIALIAS)
    # Displaying image
    new_pic = ImageTk.PhotoImage(resized)
    img_label = tkinter.Label(image=new_pic, bg='black')
    img_label.image = new_pic
    img_label.place(relx=0.5, rely=0.4, anchor=CENTER)


def predict(pat,strr):
    print(resized)
    #After
    img = load_img(str(resized), color_mode="grayscale", target_size=(150, 150))  # Loading Image
    img = img.astype('float32')
    img = img / 255.0  # prepare pixel data
    model = models.load_model('cats_and_dogs_small_1.h5')  # Load Trained Model
    result = model.predict_classes(img)  # Predicting image
    time.sleep(2)
    display_result.config(text=strr + str(result[0]))



window.title('Cat and Dog Classification')
window.configure(bg='#ED9850')
window.geometry("500x500+500+100")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

lb1 = tkinter.Label(text="Cat and Dog Classification", bg="#DA902D", relief="solid",
                    height=1, font="Times%New%Roman 18 bold italic", anchor=CENTER)
lb1.pack(side=TOP, fill=BOTH)

lb2 = tkinter.Label(text="Give me image", bg="#ED9850", font="Times%New%Roman 20 bold italic", anchor=CENTER)
lb2.place(relx=0.5, rely=0.2, anchor=CENTER)

result_value = ''
display_result = tkinter.Label(text="Prediction here: "+result_value, bg="#DA902D", relief="solid"  ,
          height=2, font="Times%New%Roman 18 bold italic", anchor=CENTER)
display_result.pack(side=BOTTOM,fill=X)

predict_button = tkinter.Button(text="Predict", bg='#DA902D', width=7,
                                font=("Times%New%Roman", 15, "bold"),
                                relief="solid", command=lambda: predict(image_path,"it's a: "))
predict_button.place(relx=0.4, rely=0.6, anchor=CENTER)
upload_button = tkinter.Button(text='Upload', bg='#DA902D', width=7,
                               font=("Times%New%Roman", 15, "bold"),
                               relief="solid", command=lambda:upload("Prediction here: "))
upload_button.place(relx=0.6, rely=0.6, anchor=CENTER)

window.mainloop()
