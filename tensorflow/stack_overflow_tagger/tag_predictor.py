import tensorflow as tf
from tensorflow.keras import losses

model_save_path = 'saved_model/dupa'
model = tf.keras.models.load_model(model_save_path)

model.summary()

raw_test_ds = tf.keras.utils.text_dataset_from_directory(
    'test',
    batch_size=32
)

model.compile(
    loss=losses.SparseCategoricalCrossentropy(),
    optimizer='adam',
    metrics=['accuracy']
)

label_mapping = {
    0: 'C#',
    1: 'Java',
    2: 'JS',
    3: 'Python'
}

for text_batch, label_batch in raw_test_ds.take(1):
    text = text_batch.numpy()[0].decode()

    predictions = model.predict(text_batch)
    predicted_label = tf.argmax(predictions[0]).numpy()

    print("Text", text)
    print("Predicted label", label_mapping.get(predicted_label, 'Unknown Label'))