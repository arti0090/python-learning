# Use seaborn for pairplot.
# $ pip install -q seaborn

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

import dataset_provider

test_features, test_labels = dataset_provider.get_test_dataset()
train_features, train_labels = dataset_provider.get_train_dataset()
train_dataset = dataset_provider.get_full_train_dataset()

train_dataset.describe().transpose()[['mean', 'std']]

# Normalization - making data more reliable by eliminating some max-mins in the data
normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(np.array(train_features))

# calculated avg
# print()
# print(normalizer.mean.numpy())
# print()

first = np.array(train_features[:1])

with np.printoptions(precision=2, suppress=True):
    print('First example:', first)    
    print()
    print('Normalized:', normalizer(first).numpy())

# linear regression with one variable (predict MPG from horsepower only)

horsepower = np.array(train_features['Horsepower'])
# creating normalizer for data
horsepower_normalizer = layers.Normalization(input_shape=[1,], axis=None)
horsepower_normalizer.adapt(horsepower)

# using Sequential to represent step by step model
horsepower_model = tf.keras.Sequential([
    horsepower_normalizer,
    layers.Dense(units=1)
])

horsepower_model.summary()

# running untrained model by predicting value of MPG on 10 first horsepower values
# print(horsepower_model.predict(horsepower[:10]))

horsepower_model.compile(
    optimizer=tf.optimizers.Adam(learning_rate=0.1),
    loss='mean_absolute_error'
)

history = horsepower_model.fit(
    train_features['Horsepower'],
    train_labels,
    epochs=100,
    verbose=0,
    validation_split=0.2
)


hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
# print(hist.tail())

def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 10])
    plt.xlabel('Epoch')
    plt.ylabel('Error [MPG]')
    plt.legend()
    plt.grid(True)

# plot_loss(history)
# plt.show()

test_results = {}

test_results['horsepower_model'] = horsepower_model.evaluate(
    test_features['Horsepower'],
    test_labels,
    verbose=0
)

## view model prediction as function of input
# x = tf.linspace(0.0, 250, 251)
# y = horsepower_model.predict(x)

# def plot_horsepower(x, y):
#   plt.scatter(train_features['Horsepower'], train_labels, label='Data')
#   plt.plot(x, y, color='k', label='Predictions')
#   plt.xlabel('Horsepower')
#   plt.ylabel('MPG')
#   plt.legend()

# plot_horsepower(x, y)
# plt.show()
  
### linear model with all the inputs available ###
linear_model = tf.keras.Sequential([
    normalizer,
    layers.Dense(units=1)
])

## possible check of matrices that have shape (9, 1)
# linear_model.layers[1].kernel

linear_model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
    loss='mean_absolute_error'
)

history = linear_model.fit(
    train_features,
    train_labels,
    epochs=100,
    verbose=0,
    validation_split=0.2
)

test_results['linear_model'] = linear_model.evaluate(
    test_features, test_labels, verbose=0)

### Deep Neural Network with one input ###
def build_and_compile_dnn_model(norm):
    model = keras.Sequential([
        norm,
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    model.compile(
        loss='mean_absolute_error',
        optimizer=tf.keras.optimizers.Adam(0.001)
    )

    return model


dnn_horsepower_model = build_and_compile_dnn_model(horsepower_normalizer)
dnn_horsepower_model.summary()

history = dnn_horsepower_model.fit(
    train_features['Horsepower'],
    train_labels,
    validation_split=0.2,
    verbose=0,
    epochs=100
)

test_results['dnn_horsepower_model'] = dnn_horsepower_model.evaluate(
    test_features['Horsepower'],
    test_labels,
    verbose=0
)
### END Deep Neural Network with one input END ###

### Deep Neural Network with multiple input ###
dnn_model = build_and_compile_dnn_model(normalizer)
dnn_model.summary()

history = dnn_model.fit(
    train_features,
    train_labels,
    validation_split=0.2,
    verbose=0, 
    epochs=100
)

test_results['dnn_model'] = dnn_model.evaluate(test_features, test_labels, verbose=0)
### END Deep Neural Network with multiple input END ###

# Model Performance Review #
print(pd.DataFrame(test_results, index=['Mean absolute error [MPG]']).T)

test_predictions = dnn_model.predict(test_features).flatten()

# a = plt.axes(aspect='equal')
# plt.scatter(test_labels, test_predictions)
# plt.xlabel('True Values [MPG]')
# plt.ylabel('Predictions [MPG]')
# lims = [0, 50]
# plt.xlim(lims)
# plt.ylim(lims)
# _ = plt.plot(lims, lims)

# plt.show()

dnn_model.save('dnn_model.keras')

reloaded = tf.keras.models.load_model('dnn_model.keras')

test_results['reloaded'] = reloaded.evaluate(
    test_features, test_labels, verbose=0)

print(pd.DataFrame(test_results, index=['Mean absolute error [MPG]']).T)