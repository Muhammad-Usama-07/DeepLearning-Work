from tkinter import *
from tkinter import colorchooser, filedialog, messagebox
from tkinter.filedialog import asksaveasfilename
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import PIL.ImageGrab as ImageGrab

window = Tk()


def draw(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill='white', outline='white', width=pen_size)


def clear():
    canvas.delete("all")


def predict():
    filename = 'image.png'
    x = window.winfo_rootx() + canvas.winfo_x()
    y = window.winfo_rooty() + canvas.winfo_y()

    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    # Image taken
    image = ImageGrab.grab().crop((x, y, x1, y1))
    new_image = image.resize((28, 28))
    new_image.save(filename)

    # converting image to array
    img = load_img(str(filename), color_mode="grayscale", target_size=(28, 28))
    img = img_to_array(img)

    img = img.reshape(1, 784)  # reshaping image as model trained.
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    # Loading Trained Model
    model = models.load_model('TrainedModel.h5')
    # Predicting image
    result = model.predict_classes(img)
    
window.title('Paint')
window.configure(bg='#0C85DC')
window.geometry("900x600+300+50")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
menubar = Menu(window)

Label(window, text=" Handwritten Digit Recognition ", bg="#0065AE", relief="solid",
      height=2, font="Times%New%Roman 18 bold italic", anchor=CENTER).pack(side=TOP, fill=BOTH)

canvas = Canvas(window, width=300, height=300, background='black')
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

canvas.bind('<B1-Motion>', draw)

pen_size = 20

predict_button = Button(window, text="Predict", bg='#0065AE', width=8,
                        font=("Times%New%Roman", 15, "bold"),
                        relief="ridge", command = predict)
predict_button.place(relx=0.4, rely=0.8, anchor=CENTER)
clear_button = Button(window, text='Clear', bg='#0065AE', width=8,
                      font=("Times%New%Roman", 15, "bold"),
                      relief="ridge", command=clear)
clear_button.place(relx=0.6, rely=0.8, anchor=CENTER)

window.mainloop()
