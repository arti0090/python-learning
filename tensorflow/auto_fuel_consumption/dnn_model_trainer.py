import numpy as np
import pandas as pd
import dataset_provider
import matplotlib.pyplot as plt


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

np.set_printoptions(precision=3, suppress=True)

test_features, test_labels = dataset_provider.get_test_dataset()
train_features, train_labels = dataset_provider.get_train_dataset()
train_dataset = dataset_provider.get_full_train_dataset()

train_dataset.describe().transpose()[['mean', 'std']]

normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(np.array(train_features))

input_shape = train_features.shape[1:]
input_layer = layers.Input(shape=input_shape)

dnn_model = keras.Sequential([
        input_layer,
        normalizer,
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

dnn_model.compile(
    loss='mean_absolute_error',
    optimizer=tf.keras.optimizers.Adam(0.001)
)

normalizer.adapt(np.array(train_features))

dnn_model.summary()

dnn_model.fit(
    train_features,
    train_labels,
    validation_split=0.2,
    verbose=0, 
    epochs=100
)

test_results = {}
test_results['dnn_model'] = dnn_model.evaluate(test_features, test_labels, verbose=0)
pd.DataFrame(test_results, index=['Mean absolute error [MPG]']).T

test_predictions = dnn_model.predict(test_features).flatten()

dnn_model.save('dnn_model.keras')

reloaded = tf.keras.models.load_model('dnn_model.keras')

test_results['reloaded'] = reloaded.evaluate(
    test_features, test_labels, verbose=0)

print(pd.DataFrame(test_results, index=['Mean absolute error [MPG]']).T)