import tensorflow as tf
import matplotlib.pyplot as plt
%matplotlib inline

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow import keras

from keras.callbacks import EarlyStopping #For saving epochs
from keras.layers import BatchNormalization

