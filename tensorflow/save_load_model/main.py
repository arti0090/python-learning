import os

import tensorflow as tf
from tensorflow import keras

# get dataset (example mnist data)
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# make dataset smaller for first 1000 elements
train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

# same for images and make their resolution smaller
# and change their rgb color from 255 format to 0-1 range
train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

# define simple sequential model
def create_model():
    model = tf.keras.Sequential([
        keras.layers.Dense(512, activation='relu', input_shape=(784,)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10)
    ])

    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=[tf.keras.metrics.SparseCategoricalAccuracy()]
    )

    return model

model = create_model()
model.summary()

# save checkpoints during training
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# create callback to save model weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    save_weights_only=True,
    verbose=1
)

# training model from callback
model.fit(
    train_images,
    train_labels,
    epochs=10,
    validation_data=(test_images, test_labels),
    callbacks=[cp_callback]
)

