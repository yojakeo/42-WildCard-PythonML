import tkinter as tk
from PIL import Image
from PIL import ImageTk

# Colour Config
fg = '#839496'
bg = '#242428'

gui = tk.Tk()

gui.title("Wildcard 42 ML")

gui.geometry('450x600')
gui.configure(background=bg)

# def Predict_num(path):
#     img = np.invert(Image.open(path).convert('L')).ravel()
#     num_res = sess.run(tf.argmax(output_layer, 1), feed_dict={X: [img]})
#     np.squeeze(num_res)
#     tk.Label(output_frame, text=str(num_res))

def Open_num_image():
    string = e1.get()
    width = 200
    height = 200
    img = Image.open(string)
    img = img.resize((width, height))
    photo_img = ImageTk.PhotoImage(img)
    num_image = tk.Label(img_frame, image=photo_img)
    num_image.grid(row=0, column=0)
    gui.update_idletasks()

# Number Image
img_frame = tk.Frame(bd=5, relief='sunken', bg=bg, height=210, width=210)
img_frame.place(x=5, y=5)

# Input
input_frame = tk.Frame(bd=5, bg=bg, height=90, width=210) # Frame
input_frame.place(x=230, y=5)
l1 = tk.Label(input_frame, text='Select Image Location', fg=fg, bg=bg) # Label
l1.place(x=20, y=5)
canvas1 = tk.Canvas(input_frame, width=100, height=100)
canvas1.place(x=0, y=30)
e1 = tk.Entry(gui)
canvas1.create_window(200, 140, window=e1)
tk.Button(input_frame, text='open', command=Open_num_image()).place(x=75, y=60) # Open Command

# Output
output_frame = tk.Frame(bg=bg, height=70, width=350) # Frame
output_frame.place(x=0, y=220)
tk.Button(output_frame, text='Predict', bg=bg, fg=fg).place(x=85, y=5)
tk.Label(output_frame, text='Predicted Number:', bg=bg, fg=fg).place(x=5, y=40)

gui.mainloop()
