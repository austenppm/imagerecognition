import numpy as np
import mnist
import matplotlib.pyplot as plt
from pylab import cm
#IN THIS FILE, THERE IS NO NORMALIZATION OF THE IMAGES
# Set the input shape, number of images, and number of classes
input_shape = (28, 28, 1)
num_images = 10000
num_classes = 10

# Load the MNIST dataset
X = mnist.download_and_parse_mnist_file("train-images-idx3-ubyte.gz")
Y = mnist.download_and_parse_mnist_file("train-labels-idx1-ubyte.gz")

# Convert the labels to one-hot encoded vectors
Y = np.eye(num_classes)[Y]

# Flatten the images
X = X.reshape(X.shape[0], 28, 28, 1)

# Get input i from the user
i = int(input("Enter an integer from 0 to 9999: "))

# Get the i-th image from the MNIST test data
x = X[i]

# Get the number of nodes in the intermediate layer from the user
M = int(input("Enter the number of nodes in the intermediate layer: "))

# Initialize the weights and biases with random numbers from a normal distribution
W1 = np.random.normal(0, 1/M, (M, input_shape[0]*input_shape[1]))
W2 = np.random.normal(0, 1/M, (num_classes, M))
B1 = np.random.normal(0, 1/M, M)
B2 = np.random.normal(0, 1/M, num_classes)

# Flatten the input image
x = x.flatten()

# Perform the forward pass through the neural network
z1 = np.dot(W1, x) + B1
a1 = 1 / (1 + np.exp(-z1))
z2 = np.dot(W2, a1) + B2
a2 = 1 / (1 + np.exp(-z2))

# Get the index of the class with the highest probability
output = np.argmax(a2)

# Print the output to standard output
print(output)

# Display the image and label
idx = i
plt.imshow(X[idx], cmap=cm.gray)
plt.show()
print(Y[idx])
