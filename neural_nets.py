# -*- coding: utf-8 -*-
"""TristanPaust_572_Assignment6.ipynb

Automatically generated by Colaboratory.

"""

!pip install Theano
import numpy
import theano

import numpy as np
np.random.seed(123)  # for reproducibility

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.utils import np_utils
from keras.datasets import mnist

# Load pre-shuffled MNIST data into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()
from matplotlib import pyplot as plt
#plt.imshow(X_train[0])

#X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
#X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

#print (y_train.shape)
#print (y_train[:10])
# Convert 1-dimensional class arrays to 10-dimensional class matrices
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)
#print (Y_train.shape)

#model = Sequential()
#model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(1,28,28), data_format='channels_first'))
#print (model.output_shape)
#model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(1,28,28), data_format='channels_first'))

#model.add(MaxPooling2D(pool_size=(2,2)))
#model.add(Dropout(0.25))

#model.add(Flatten())
#model.add(Dense(128, activation='relu'))
#model.add(Dropout(0.5))
#model.add(Dense(10, activation='softmax'))

#model.compile(loss='categorical_crossentropy',
#              optimizer='adam',
#              metrics=['accuracy'])

#model.fit(X_train, Y_train,
#          batch_size=32, nb_epoch=10, verbose=1)

#score = model.evaluate(X_test, Y_test, verbose=0)

# --*-- First Model --*--

model1 = Sequential(name="model1")
model1.add(Dense(16, activation='sigmoid',  input_shape=(1*28*28,)))
model1.add(Dense(10, activation='softmax'))


model1.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model1.fit(X_train, Y_train,
          batch_size=32, epochs=10, verbose=1)

score1_train = model1.evaluate(X_train, Y_train, verbose=0)
score1_test = model1.evaluate(X_test, Y_test, verbose=0)

# --*-- Second Model --*--

model2 = Sequential(name="model2")
model2.add(Dense(128, activation='sigmoid', input_shape=(784,)))
model2.add(Dense(10, activation='softmax'))

model2.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model2.fit(X_train, Y_train,
          batch_size=32, epochs=10, verbose=1)

score2_train = model2.evaluate(X_train, Y_train, verbose=0)
score2_test = model2.evaluate(X_test, Y_test, verbose=0)

# --*-- Third Model --*--

model3 = Sequential(name="model3")
model3.add(Dense(128, activation='relu', input_shape=(784,)))
model3.add(Dense(10, activation='softmax'))


model3.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model3.fit(X_train, Y_train,
          batch_size=32, epochs=10, verbose=1)

score3_train = model3.evaluate(X_train, Y_train, verbose=0)
score3_test = model3.evaluate(X_test, Y_test, verbose=0)

# --*-- Fourth Model --*--

model4 = Sequential(name="model4")
model4.add(Dense(128, activation='relu',  input_shape=(784,)))
model4.add(Dropout(0.5))
model4.add(Dense(10, activation='softmax'))


model4.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model4.fit(X_train, Y_train,
          batch_size=32, epochs=10, verbose=1)

score4_train = model4.evaluate(X_train, Y_train, verbose=0)
score4_test = model4.evaluate(X_test, Y_test, verbose=0)

# Reshaping the input data for Conv2D layers
X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)

# --*-- Fifth Model --*--

model5 = Sequential(name="model5")
model5.add(Conv2D(32, (3, 3), activation='relu', input_shape=(1,28,28), data_format='channels_first'))
model5.add(Flatten())
model5.add(Dense(128, activation='relu'))
model5.add(Dropout(0.5))
model5.add(Dense(10, activation='softmax'))


model5.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model5.fit(X_train, Y_train,
          batch_size=32, epochs=10, verbose=1)

model5.get_config()

score5_train = model5.evaluate(X_train, Y_train, verbose=0)
score5_test = model5.evaluate(X_test, Y_test, verbose=0)

# --*-- Sixth Model --*--

model6 = Sequential(name="model6")

model6.add(Conv2D(32, (3, 3), activation='relu', input_shape=(1,28,28), data_format='channels_first'))
model6.add(MaxPooling2D(pool_size=(2,2)))
model6.add(Dropout(0.25))
model6.add(Flatten())
model6.add(Dense(128, activation='relu'))
model6.add(Dropout(0.50))
model6.add(Dense(10, activation='softmax'))


model6.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model6.fit(X_train, Y_train,
          batch_size=32, epochs=10, verbose=1)

model6.get_config()

score6_train = model6.evaluate(X_train, Y_train, verbose=0)
score6_test = model6.evaluate(X_test, Y_test, verbose=0)

# --*-- Seventh Model --*--

model7 = Sequential(name="model7")

model7.add(Conv2D(32, (3, 3), activation='relu', input_shape=(1,28,28), data_format='channels_first'))
model7.add(Conv2D(32, (3, 3), activation='relu'))
model7.add(MaxPooling2D(pool_size=(2,2)))
model7.add(Dropout(0.25))
model7.add(Flatten())
model7.add(Dense(128, activation='relu'))
model7.add(Dropout(0.50))
model7.add(Dense(10, activation='softmax'))


model7.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model7.fit(X_train, Y_train,
          batch_size=32, epochs=10, verbose=1)

model7.get_config()

score7_train = model7.evaluate(X_train, Y_train, verbose=0)
score7_test = model7.evaluate(X_test, Y_test, verbose=0)

from keras.datasets import cifar10

# Load pre-shuffled Cifar10 data into train and test sets
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
from matplotlib import pyplot as plt

# 3 * 32 * 32 = 3072
x_train = x_train.reshape(-1, 3072)
x_test = x_test.reshape(-1, 3072)

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Convert 1-dimensional class arrays to 10-dimensional class matrices
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# --*-- Eigth Model --*--

model8 = Sequential(name="model8")
model8.add(Dense(128, activation='relu', input_shape=(3072,)))
model8.add(Dropout(0.5))
model8.add(Dense(10, activation='softmax'))


model8.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model8.fit(x_train, y_train,
          batch_size=32, epochs=10, verbose=1)

score8_train = model8.evaluate(x_train, y_train, verbose=0)
score8_test = model8.evaluate(x_test, y_test, verbose=0)

# Reshape input data for Conv2D
x_train = x_train.reshape(x_train.shape[0], 3, 32, 32)
x_test = x_test.reshape(x_test.shape[0], 3, 32, 32)

# --*-- Ninth Model --*--

model9 = Sequential(name="model9")

model9.add(Conv2D(32, (3, 3), activation='relu', input_shape=(3,32,32), data_format='channels_first'))
model9.add(Conv2D(32, (3, 3), activation='relu'))
model9.add(MaxPooling2D(pool_size=(2,2)))
model9.add(Dropout(0.25))
model9.add(Flatten())
model9.add(Dense(128, activation='relu'))
model9.add(Dropout(0.5))
model9.add(Dense(10, activation='softmax'))


model9.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model9.fit(x_train, y_train,
          batch_size=32, epochs=10, verbose=1)

model9.get_config()

score9_train = model9.evaluate(x_train, y_train, verbose=0)
score9_test = model9.evaluate(x_test, y_test, verbose=0)

print("Model 1, Train:", score1_train)
print("Model 1, Test:", score1_test)

# --*--

print("Model 2, Train:", score2_train)
print("Model 2, Test:", score2_test)

# --*--

print("Model 3, Train:", score3_train)
print("Model 3, Test:", score3_test)

# --*--

print("Model 4, Train:", score4_train)
print("Model 4, Test:", score4_test)

# --*--

print("Model 5, Train:", score5_train)
print("Model 5, Test:", score5_test)

# --*--

print("Model 6, Train:", score6_train)
print("Model 6, Test:", score6_test)

# --*--


print("Model 7, Train:", score7_train)
print("Model 7, Test:", score7_test)

# --*--


print("Model 8, Train:", score8_train)
print("Model 8, Test:", score8_test)

# --*--

print("Model 9, Train:", score9_train)
print("Model 9, Test:", score9_test)
