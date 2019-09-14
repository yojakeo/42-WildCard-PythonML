import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import tkinter as tk
from PIL import Image
from PIL import ImageTk

data = input_data.read_data_sets("MNIST_data", one_hot=True)  # y labels are oh-encoded

n_train = data.train.num_examples  # 55,000
n_validation = data.validation.num_examples  # 5000
n_test = data.test.num_examples  # 10,000

n_input = 784  # 784 = 28 x 28 pixels from the input image converted to CSV.
n_hidden1 = 512  # Argibtrary 1st Hidden Node Count
n_hidden2 = 256  # Argibtrary 2nd Hidden Node Count
n_hidden3 = 128  # Argibtrary 3rd Hidden Node Count
n_hidden4 = 64   # Argibtrary 4th Hidden Node Count
n_hidden5 = 32   # Argibtrary 5th Hidden Node Count
n_output = 10  # Output Node Count (0-9 digits) 10 + (A-Z) 26
learning_rate = 1e-4 # Rate of learning given in SN
n_iterations = 1000
batch_size = 512
dropout = 0.5

X = tf.placeholder("float", [None, n_input])
Y = tf.placeholder("float", [None, n_output])
keep_prob = tf.placeholder(tf.float32)
# Weights with a deviation of .1 from 0.
weights = {
    'w1': tf.Variable(tf.truncated_normal([n_input, n_hidden1], stddev=0.1)),
    'w2': tf.Variable(tf.truncated_normal([n_hidden1, n_hidden2], stddev=0.1)),
    'w3': tf.Variable(tf.truncated_normal([n_hidden2, n_hidden3], stddev=0.1)),
    'w4': tf.Variable(tf.truncated_normal([n_hidden3, n_hidden4], stddev=0.1)),
    'w5': tf.Variable(tf.truncated_normal([n_hidden4, n_hidden5], stddev=0.1)),
    'out': tf.Variable(tf.truncated_normal([n_hidden5, n_output], stddev=0.1)),
}
# Constant bias values for each layer.
biases = {
    'b1': tf.Variable(tf.constant(0.1, shape=[n_hidden1])),
    'b2': tf.Variable(tf.constant(0.1, shape=[n_hidden2])),
    'b3': tf.Variable(tf.constant(0.1, shape=[n_hidden3])),
    'b4': tf.Variable(tf.constant(0.1, shape=[n_hidden4])),
    'b5': tf.Variable(tf.constant(0.1, shape=[n_hidden5])),
    'out': tf.Variable(tf.constant(0.1, shape=[n_output]))
}

layer_1 = tf.add(tf.matmul(X, weights['w1']), biases['b1'])
layer_2 = tf.add(tf.matmul(layer_1, weights['w2']), biases['b2'])
layer_3 = tf.add(tf.matmul(layer_2, weights['w3']), biases['b3'])
layer_4 = tf.add(tf.matmul(layer_3, weights['w4']), biases['b4'])
layer_5 = tf.add(tf.matmul(layer_4, weights['w5']), biases['b5'])
layer_drop = tf.nn.dropout(layer_5, keep_prob)
output_layer = tf.matmul(layer_5, weights['out']) + biases['out']

cross_entropy = tf.reduce_mean( # Computes the mean from element dimentions in a Tensor
    tf.nn.softmax_cross_entropy_with_logits( # Computes softmax between logits and labels
        labels=Y, logits=output_layer
        ))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

correct_pred = tf.equal(tf.argmax(output_layer, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# train on mini batches
for i in range(n_iterations):
    batch_x, batch_y = data.train.next_batch(batch_size)
    sess.run(train_step, feed_dict={
        X: batch_x, Y: batch_y, keep_prob: dropout
        })

    # print loss and accuracy (per minibatch)
    if i % 100 == 0:
        minibatch_loss, minibatch_accuracy = sess.run(
            [cross_entropy, accuracy],
            feed_dict={X: batch_x, Y: batch_y, keep_prob: 1.0}
            )
        print(
            "Iteration",
            str(i),
            "\t| Loss =",
            str(minibatch_loss),
            "\t| Accuracy =",
            str(minibatch_accuracy)
            )

test_accuracy = sess.run(accuracy, feed_dict={X: data.test.images, Y: data.test.labels, keep_prob: 1.0})
print("\nAccuracy on test set:", test_accuracy)

# Window

# Colour Config
fg = '#839496'
bg = '#242428'

gui = tk.Tk()

gui.title("Wildcard 42 ML")

gui.geometry('450x300')
gui.configure(background=bg)

# Number Image
img_frame = tk.Frame(bd=5, relief='sunken', bg=bg, height=210, width=210)
img_frame.place(x=5, y=5)


def Open_num_image():
    try:
        e1_out = e1_input.get()
        width = 200
        height = 200
        img = Image.open(e1_out)
        img = img.resize((width, height))
        photo_img = ImageTk.PhotoImage(img)
        num_image = tk.Label(img_frame, image=photo_img)
        num_image.image = photo_img
        num_image.grid(row=0, column=0)
        gui.update_idletasks()
    except(FileNotFoundError, AttributeError):
        print("Invalid File Path.")

# Input
input_frame = tk.Frame(bd=5, bg=bg, height=120, width=210) # Frame
input_frame.place(x=230, y=5)
l1 = tk.Label(input_frame, text='Select Image Location', fg=fg, bg=bg) # Label
l1.place(x=20, y=0)
e1_input = tk.StringVar()
e1 = tk.Entry(input_frame, textvariable=e1_input)
e1.place(x=0, y=30)
tk.Button(input_frame, text='open', command=Open_num_image, fg=fg).place(x=75, y=70) # Open Command

# Output

def Predict_num():
    try:
        e1_out = e1_input.get()
        img = np.invert(Image.open(e1_out).convert('L')).ravel()
        num_res = sess.run(tf.argmax(output_layer, 1), feed_dict={X: [img]})
        np.squeeze(num_res)
        tk.Label(output_frame, text=str(num_res), bg=bg, fg=fg).place(x=135, y=40)
        gui.update_idletasks()
    except (FileNotFoundError, AttributeError):
        print("Invalid File Path.")


output_frame = tk.Frame(bg=bg, height=70, width=350) # Frame
output_frame.place(x=0, y=220)
tk.Button(output_frame, text='Predict', command=Predict_num, bg=bg, fg=fg).place(x=85, y=5)
tk.Label(output_frame, text='Predicted Number:', bg=bg, fg=fg).place(x=5, y=40)

gui.mainloop()