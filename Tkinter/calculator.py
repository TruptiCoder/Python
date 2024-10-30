from tkinter import *

# --------- Fucntions -----------
def get_digit(digit):
    current = result_label['text']
    if current == 'Error':
        current = ''
    new = current + str(digit)
    result_label['text'] = new

def clr_screen():
    result_label['text'] = ''

def operation(opr):
    curr = result_label['text']
    if curr == 'Error':
        curr = ''
    if curr == '':
        return
    if curr[-1] == '+' or curr[-1] == '-' or curr[-1] == '*' or curr[-1] == '/':
        curr = curr[:-1]
    if curr[-1] != opr:
        new = curr + opr
    result_label['text'] = new

def get_result():
    equation = result_label['text']
    if equation == 'Error':
        equation = ''
    try:
        result = round(eval(equation), 2)
        result_label['text'] = str(result)
    except:
        result_label['text'] = 'Error'


root = Tk()

bg_color = '#111'
fg_color = 'white'
btn_color = 'royalblue'

root.title('Calculator')
root.geometry('280x380')
root.resizable(0, 0)
root.config(background=bg_color)

# --------- result screen -----------
result_label = Label(root, text='', bg=bg_color, fg=fg_color, width=9, anchor='e')
result_label.grid(row=0, column=0, columnspan=4, pady=(50, 25), sticky='w')
result_label.config(font=('verdana', 30, 'bold'))

# ---------- row 1 -------------
btn7 = Button(root, text='7', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: get_digit(7))
btn7.grid(row=1, column=0)

btn8 = Button(root, text='8', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: get_digit(8))
btn8.grid(row=1, column=1)

btn9 = Button(root, text='9', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: get_digit(9))
btn9.grid(row=1, column=2)

btn_add = Button(root, text='+', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: operation('+'))
btn_add.grid(row=1, column=3)

# ----------- row 2 -------------
btn4 = Button(root, text='4', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: get_digit(4))
btn4.grid(row=2, column=0)

btn5 = Button(root, text='5', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: get_digit(5))
btn5.grid(row=2, column=1)

btn6 = Button(root, text='6', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: get_digit(6))
btn6.grid(row=2, column=2)

btn_sub = Button(root, text='-', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: operation('-'))
btn_sub.grid(row=2, column=3)

# --------- row 3 ------------
btn1 = Button(root, text='1', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: get_digit(1))
btn1.grid(row=3, column=0)

btn2 = Button(root, text='2', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: get_digit(2))
btn2.grid(row=3, column=1)

btn3 = Button(root, text='3', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: get_digit(3))
btn3.grid(row=3, column=2)

btn_mul = Button(root, text='*', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: operation('*'))
btn_mul.grid(row=3, column=3)

# -------- row 4 ------------ 
btn0 = Button(root, text='0', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: get_digit(0))
btn0.grid(row=4, column=0)

btn_clr = Button(root, text='C', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command=clr_screen)
btn_clr.grid(row=4, column=1)

btn_eq = Button(root, text='=', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command=get_result)
btn_eq.grid(row=4, column=2)

btn_div = Button(root, text='/', bg=btn_color, fg=fg_color, width=5, height=2, font=('verdana', 14), command= lambda: operation('/'))
btn_div.grid(row=4, column=3)

root.mainloop()