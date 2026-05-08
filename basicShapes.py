from tkinter import *

#window
window = Tk()
window.title("Basic Shapes Canvas")
window.geometry("600x500")

#canvas
canvas = Canvas(window, width=600, height=500, bg="white")
canvas.pack()

#rectangle
canvas.create_rectangle(50, 50, 200, 150, fill="blue")

#circle
canvas.create_oval(250, 50, 400, 200, fill="red")

#line
canvas.create_line(50, 250, 400, 250, fill="green")

#name
canvas.create_text(300, 450, text="Princess Lallane F. Gablanca", font=("Arial", 16, "bold"))

window.mainloop()