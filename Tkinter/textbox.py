from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print("Hello", username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1 ,END)

window = Tk()

entry = Entry(window,
              font= ("Comic sans", 30),
              fg= 'white',
              bg= 'royalblue',
              show='*' # for passwords
              )
entry.insert(0, 'spongebob')
entry.pack(side=LEFT)

submit_btn = Button(window,
                    text= 'Submit',
                    font= ("Comic sans", 20),
                    command=submit)
submit_btn.pack(side=RIGHT)

del_btn = Button(window,
                    text= 'Delete',
                    font= ("Comic sans", 20),
                    command=delete)
del_btn.pack(side=RIGHT)

bks_btn = Button(window,
                    text= 'Backspace',
                    font= ("Comic sans", 20),
                    command=backspace)
bks_btn.pack(side=RIGHT)

window.mainloop()