import numpy as np
import mnist
import matplotlib.pyplot as plt
from pylab import cm
import random
import math

# Set the input shape, number of images, and number of classes
input_shape = (28, 28, 1)
num_images = 60000
num_classes = 10

# Set the batch size and create an empty list for the batch
batch_size = 101
batch_x = []
batch_y = []

# Store the total cross-entropy error

total_error = 0

# Load the MNIST dataset
X = mnist.download_and_parse_mnist_file("train-images-idx3-ubyte.gz")
Y = mnist.download_and_parse_mnist_file("train-labels-idx1-ubyte.gz")

# Normalize the images
X = X / 255.0

# Convert the labels to one-hot encoded vectors
Y = np.eye(num_classes)[Y]

# Flatten the images
X = X.reshape(X.shape[0], 28, 28, 1)

# Generate a list of random indices for the batch:
indices = random.sample(range(num_images), batch_size)

# Extract the images and labels for the batch from the indices:
for i in indices:
    batch_x.append(X[i])
    batch_y.append(Y[i])

# Convert the batch to a numpy array:
batch_x = np.array(batch_x)
batch_y = np.array(batch_y)

# Get the batch of images from the MNIST test data
x = batch_x[0]

# The number of nodes in the intermediate layer that can be set by the user
M = 100

# Initialize the weights and biases with random numbers from a normal distribution
W1 = np.random.normal(0, 1/M, (M, input_shape[0]*input_shape[1]))
W2 = np.random.normal(0, 1/M, (num_classes, M))
B1 = np.random.normal(0, 1/M, M)
B2 = np.random.normal(0, 1/M, num_classes)

# # Flatten the input image
# x = x.flatten()

# # Perform the forward pass through the neural network
# z1 = np.dot(W1, x) + B1
# a1 = 1 / (1 + np.exp(-z1))
# z2 = np.dot(W2, a1) + B2
# alpha = np.max(z2)
# a2 = np.exp(z2 - alpha) / np.sum(np.exp(z2 - alpha))

# Compute the cross-entropy error for each image in the batch and add it to the total error
for i in range(batch_size):
    x = batch_x[i]
    y = batch_y[i]
    x = x.flatten()
    z1 = np.dot(W1, x) + B1
    a1 = 1 / (1 + np.exp(-z1))
    z2 = np.dot(W2, a1) + B2
    alpha = np.max(z2)
    a2 = np.exp(z2 - alpha) / np.sum(np.exp(z2 - alpha))
    error = -np.sum(y * np.log(a2))
    total_error += error

# Compute the average error
average_error = total_error / batch_size

# Get the index of the class with the highest probability
output = np.argmax(a2)

# Print the output to standard output
print(a2)
print(output)

# Print the average error to standard output
print("Average cross-entropy error: {}".format(average_error))


# Display the image and label
idx = indices[0]
plt.imshow(X[idx], cmap=cm.gray)
plt.show()
print(Y[idx])
