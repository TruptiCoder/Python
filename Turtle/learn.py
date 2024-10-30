import turtle;

t = turtle.Turtle()
penColor = "red"
fillColor = "yellow"

t.penup()
t.goto(0, 100)
t.pendown()
t.pencolor(penColor)
t.fillcolor(fillColor)
t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()

turtle.mainloop()  