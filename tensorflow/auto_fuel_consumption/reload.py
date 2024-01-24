import tensorflow as tf
import pandas as pd
import dataset_provider

reloaded = tf.keras.models.load_model('dnn_model.keras')

test_features, test_labels = dataset_provider.get_test_dataset()

test_results = {}

test_results['reloaded'] = reloaded.evaluate(
    test_features, test_labels, verbose=0
)

print(pd.DataFrame(test_results, index=['Mean absolute error [MPG]']).T)
