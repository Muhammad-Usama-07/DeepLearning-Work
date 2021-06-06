from tkinter import *


window = Tk()

def draw(event):
    x1,y1 = (event.x-2), (event.y-2)
    x2,y2 = (event.x+2), (event.y+2)
    canvas.create_oval(x1,y1,x2,y2, fill='white', outline = 'white', width = pen_size)

def clear():
    canvas.delete("all")


window.title('Paint')
window.configure( bg = '#0C85DC' )
window.geometry( "900x600+300+50" )
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
menubar = Menu(window)

canvas = Canvas(window, width=300,height=300, background='black')
canvas.place(relx=0.2, rely=0.4,anchor=CENTER)

canvas.bind('<B1-Motion>', draw)

pen_size = 20

predict_button = Button(window, text = "Predict" , bg = '#09436D' , width = 8,
                               font = ("Times%New%Roman" , 15 , "bold") ,
                               relief = "ridge" )
predict_button.place(relx=0.1, rely=0.7,anchor=CENTER)
clear_button = Button(window, text='Clear', bg = '#09436D' , width = 8,
                               font = ("Times%New%Roman" , 15 , "bold") ,
                               relief = "ridge", command= clear)
clear_button.place(relx=0.3, rely=0.7,anchor=CENTER)

window.mainloop()
