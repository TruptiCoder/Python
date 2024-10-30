from tkinter import *
from PIL import ImageTk, Image

# widgets = GUI elements: buttons, textboxes, lables, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("420x420") # size of window (widthxheight)
window.title("Trupti's first window")

icon = ImageTk.PhotoImage(Image.open("panda.jpg")) 
window.iconphoto(True, icon)

# To change the background color
window.config(background="#967bb6")

window.mainloop() # place a window on computer screen, listen for events