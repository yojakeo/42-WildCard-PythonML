import tkinter as tk
from PIL import Image
from PIL import ImageTk

fg = '#839496'
bg = '#242428'
gui = tk.Tk()

gui.title("Wildcard 42 ML")

gui.geometry('600x600')
gui.configure(background=bg)

# def Open_num_image(img_path):


l1 = tk.Label(gui, text='Select Image Location', fg=fg, bg=bg)
l1.grid(row=0, column=0)
e1 = tk.Entry(gui,text='')
e1.grid(row=0, column=1)

tk.Button(gui,text='open').grid(row=0, column=2)

box1 = tk.Listbox(gui,selectmode='multiple', fg=fg, bg=bg)
box1.grid(row=10, column=0)
tk.Button(gui, text='Clear All').grid(row=12,column=0)

box2 = tk.Listbox(gui, fg=fg, bg=bg)
box2.grid(row=10, column=1)
tk.Button(gui, text='Select X', fg=fg, bg=bg).grid(row=12,column=1)

T = tk.Text(gui, height=2, width=30, fg=fg, bg=bg)
T.grid(row=3, column=5)
T.insert(tk.END, "Just a text Widget\nin two lines\n")
width = 200
height = 200
img = Image.open("test_img.png")
img = img.resize((width,height))
photoImg =  ImageTk.PhotoImage(img)
num_image = tk.Label(gui, image=photoImg)
num_image.grid(row=8, column=0)
tk.Button(gui, text='Select y').grid(row=12,column=2)

tk.Button(gui, text='Solution').grid(row=20, column=1)

gui.mainloop()
