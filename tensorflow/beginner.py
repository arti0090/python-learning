# https://www.tensorflow.org/tutorials/quickstart/beginner?hl=pl
import tensorflow as tf
print("Tensorflow version:", tf.__version__)

mnist = tf.keras.datasets.mnist

# Load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# convert from int to float
x_train = x_train / 255.0
x_test = x_test / 255.0

# build ML model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

# return vector of results 'logit' or 'log-odds'
# https://developers.google.com/machine-learning/glossary?hl=pl#logits
# https://developers.google.com/machine-learning/glossary?hl=pl#log-odds
predictions = model(x_train[:1]).numpy()
print(predictions)

# convert logits to predictions of classes
tf.nn.softmax(predictions).numpy()

# loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# untrained model like this should give low probability (1/10th)
loss_fn(y_train[:1], predictions).numpy()

# compile model
model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

# model training
model.fit(x_train, y_train, epochs=5)

# model evaluation checks model performance on test sets
model.evaluate(x_test, y_test, verbose=2)

# Properties of Softmax Function
# The calculated probabilities will be in the range of 0 to 1.
# The sum of all the probabilities is equals to 1.
# Softmax Function Usage
# Used in multiple classification logistic regression model.
# In building neural networks softmax functions used in different layer level.
probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])

probability_model(x_test[:5])
