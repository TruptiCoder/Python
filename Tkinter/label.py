# label = an area widget that holds text and/or an image within a window

from tkinter import *
from PIL import ImageTk, Image

window = Tk()

# img = ImageTk.PhotoImage(Image.open("panda.jpg")) # normal image

# to resize the image
img = (Image.open('panda.jpg'))
resize_img = img.resize((200, 200))
new_img = ImageTk.PhotoImage(resize_img)

label = Label(window, 
              text="Hello World! :)", 
              font=('Arial', 40, 'bold'), 
              fg='purple', 
              bg='lavender',
              relief=RAISED, # RAISED, SUNKEN
              bd= 10,
              padx= 20,
              pady= 30,
              image=new_img,
              compound= 'bottom')
label.pack()
# label.place(x=50, y=50)

window.mainloop()