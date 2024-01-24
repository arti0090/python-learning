def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    
    plt.xlabel("{} {:2.0f}% ({})"
            .format(class_names[predicted_label],
                100 * np.max(predictions_array),
                class_names[true_label]
            ),
            color=color
    )

def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    this_plot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    this_plot[predicted_label].set_color('red')
    this_plot[true_label].set_color('blue')


# ---------------------------------

# https://www.tensorflow.org/tutorials/keras/classification?hl=pl
import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

# importing fashion MNIST datasets
fashion_mnist = tf.keras.datasets.fashion_mnist

# train_images - images on which model will train (28x28 grayscale images)
# train_labels - labels to be added to images (int from 0 to 9 which represents class of clothes)
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# shape (format) of the data
print(train_images.shape)
# (60000, 28, 28) -> 60000 images in 28 x 28 resolution
print(len(train_labels))
# 60000 labels, one per image each got value 0-9

print(test_images.shape)
# (10000, 28, 28) -> 10000 test images in 28 x 28 resolution

# show the 1st train image of dataset
# plt.figure()
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

# rescaling image pixels from range 0-255 to 0-1 thus making it more performant for model
train_images = train_images / 255.0
test_images = test_images / 255.0

# show first 25 images
# plt.figure(figsize=(10, 10))

# for i in range(25):
#     plt.subplot(5, 5, i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary)
#     plt.xlabel(class_names[train_labels[i]])

plt.show()

# 
# MODEL BUILDING
# 
# Layers configuration
model = tf.keras.Sequential([
    # Flatten -> convert 2D array of pixels into 1D array 28 x 28 -> 784px
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    # Dense Layer -> neuron layer, 128 nodes (neurons)
    # neurons could be small elements that are connected to each other and think about most accurate response
    tf.keras.layers.Dense(128, activation='relu'),
    # Output Dense Layer -> creates 10 neurons to which neuron from past is assigning 
    # the value of how accurate it thinks the answer is.
    # We can visualise it as 10 paper cards with an number from 0 to 9 and neuron from past is giving the note
    # to the card of what the input is closest by its thinking
    tf.keras.layers.Dense(10)
])

# model compilation
model.compile(
    # optimizer -> how model is updated according to data and its loss
    optimizer='adam',
    # loss function -> measure accuracy while learning, steer the model in correct direction of learning
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    # metrics -> used to monit the learning and testing
    metrics=['accuracy']
)

# training model -> fitting the data of images and labels with 10 epochs (try's)
model.fit(
    train_images,
    train_labels,
    epochs=10
)

# testing accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print("Test accuracy: ", test_acc)

# predicting the image label with model
probability_model = tf.keras.Sequential([
    model,
    # Softmax layer converts the logit output from model into probabilities readable by user
    tf.keras.layers.Softmax()
])

predictions = probability_model.predict(test_images)

# print all predictions for 1st image in a decimal digit
print(predictions[0])
# print prediction with highest probability
np.argmax(predictions[0])

# show label of 1st test image
print(class_names[np.argmax(predictions[0])])

# check forecasts
# num_rows = 5
# num_cols = 3
# num_images = num_rows*num_cols
# plt.figure(figsize=(2*2*num_cols, 2*num_rows))

# for i in range(num_images):
#   plt.subplot(num_rows, 2*num_cols, 2*i+1)
#   plot_image(i, predictions[i], test_labels, test_images)
#   plt.subplot(num_rows, 2*num_cols, 2*i+2)
#   plot_value_array(i, predictions[i], test_labels)

# plt.tight_layout()
# plt.show()

# 
# USING TRAINED MODEL
# 
img = test_images[1]

# keras models needs a batch of images hence:
img = (np.expand_dims(img, 0))

prediction_single = probability_model.predict(img)
print(prediction_single)

# plot_value_array(1, prediction_single[0], test_labels)
# _ = plt.xticks(range(10), class_names, rotation=45)
# plt.show()

plt.subplot(1, 2, 1)
plot_image(1, prediction_single, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(1, prediction_single[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()