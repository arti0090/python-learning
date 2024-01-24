import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses

# import dataset from IMDB database
url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

dataset = tf.keras.utils.get_file("aclImdb_v1", url,
                                    untar=True, cache_dir='.',
                                    cache_subdir=''
                                  )

dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')

print("Dataset dir: ", os.listdir(dataset_dir))

train_dir = os.path.join(dataset_dir, 'train')
print("Train dir: ", os.listdir(train_dir))

sample_file = os.path.join(train_dir, 'pos/1181_9.txt')
with open(sample_file) as f:
    print("File pos/1181_9.txt: ")
    print(f.read())

# folder structure preparation
remove_dir = os.path.join(train_dir, 'unsup')
shutil.rmtree(remove_dir)

# dividing data to train, verify and test datasets
batch_size = 32
seed = 42

raw_train_ds = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed
)

# Found 25000 files belonging to 2 classes.
# Using 20000 files for training.

# iterate through data and print some examples
for text_batch, label_batch in raw_train_ds.take(1):
    for i in range(3):
        print("Review", text_batch.numpy()[i])
        print("Label", label_batch.numpy()[i])

# label class names (probably coming from dir names)
print("Label 0 corresponds to", raw_train_ds.class_names[0])
print("Label 1 corresponds to", raw_train_ds.class_names[1])
# Label 0 corresponds to neg
# Label 1 corresponds to pos

# creating validation dataset
raw_val_ds = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=seed
)

# creating test dataset
raw_test_ds = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/test',
    batch_size=batch_size
)

# standardization of text (removing html tags and punctuation)
# tokenization (split strings into 'tokens' f.e. on spaces)
# vectorization (convert tokens into numbers that can be pop-ed into model)
# can be done with tf.keras.layers.TextVectorization

# creating custom standardization 
def custom_standardization(input_data):
    lowercase = tf.strings.lower(input_data)
    stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
    return tf.strings.regex_replace(
        stripped_html,
        '[%s]' % re.escape(string.punctuation),
        ''
    )

# text vectorization with custom standardization and output as integer
max_features = 10000
sequence_length = 250

vectorize_layer = layers.TextVectorization(
    standardize=custom_standardization,
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=sequence_length
)

# adapting layer state to dataset (builds index of strings to ints)
# make a text only dataset without labels first
train_text = raw_train_ds.map(lambda x, y: x)
vectorize_layer.adapt(train_text)

# function to see the preliminary combined data
def vectorize_text(text, label):
    text = tf.expand_dims(text, -1)
    return vectorize_layer(text), label

# retrieve a batch (of 32 reviews and labels) from the dataset
text_batch, label_batch = next(iter(raw_train_ds))
first_review, first_label = text_batch[0], label_batch[0]
print("Review", first_review)
print("Label", raw_train_ds.class_names[first_label])
print("Vectorized review", vectorize_text(first_review, first_label))

# mapping datasets to vectorized format
train_ds = raw_train_ds.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
test_ds = raw_test_ds.map(vectorize_text)

# performance dataset configuration
# function cache() and prefetch() are needed so data is more performant and data won't be blocked
# more at https://www.tensorflow.org/guide/data_performance?hl=pl
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)

# CREATING MODEL AND NEURAL NETWORK
embedding_dim = 16

# sequential model
model = tf.keras.Sequential([
    # getting coded in ints index of strings
    layers.Embedding(max_features + 1, embedding_dim),
    layers.Dropout(0.2),
    # return averaged sequence dimension, it lets model use input data with different length
    layers.GlobalAveragePooling1D(),
    layers.Dropout(0.2),
    # dense connection with 1 output node
    layers.Dense(1)
])

print(model.summary())

# loss i optimizer function
model.compile(
    loss=losses.BinaryCrossentropy(from_logits=True),
    optimizer='adam',
    metrics=tf.metrics.BinaryAccuracy(threshold=0.0)
)

# model training
epochs = 10
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)

# evaluate model accuracy
loss, accuracy = model.evaluate(test_ds)

print("Loss: ", loss)
print("Accuracy: ", accuracy)

# creating accuracy chart
history_dict = history.history
print(history_dict.keys())

acc = history_dict['binary_accuracy']
val_acc = history_dict['val_binary_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)

# Loss chart
# bo -> blue dot
plt.plot(epochs, loss, 'bo', label='Training loss')
# b -> solid blue
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

# Accuracy chart
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')

plt.show()

# EXPORT MODEL
export_model = tf.keras.Sequential([
    vectorize_layer,
    model,
    layers.Activation('sigmoid')
])

export_model.compile(
    loss=losses.BinaryCrossentropy(from_logits=False),
    optimizer='adam',
    metrics=['accuracy']
)

# testing export with raw_test_ds
loss, accuracy = export_model.evaluate(raw_test_ds)
print(accuracy)

# forecasts for new examples
examples = [
  "The movie was great!",
  "The movie was okay.",
  "The movie was terrible..."
]

export_model.predict(examples)
