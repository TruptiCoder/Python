from tkinter import *
from PIL import ImageTk, Image

# button = you click it, then it does stuff

count = 0
def click():
    global count
    print("You clicked the button", count)
    count += 1

window = Tk()

img = (Image.open('like.png'))
new = img.resize((50, 50))
photo = ImageTk.PhotoImage(new)

button = Button(window,
                text= 'click me!',
                command= click,
                font= ("Comic sans", 36),
                fg= 'crimson',
                bg= 'lavender',
                activeforeground= 'green',
                activebackground= 'lavender',
                state=ACTIVE, # DISABLED, ACTIVE
                image= photo,
                compound= 'bottom')
button.pack()


window.mainloop()