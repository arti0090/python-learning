from sklearn import datasets
import matplotlib.pyplot as plt

# load example digits
digits = datasets.load_digits()

number_of_samples = len(digits.images)

# convert images to list of pixels
data = digits.images.reshape((number_of_samples, -1))

from sklearn.model_selection import train_test_split

# _train -> training data (data used for training)
# _test -> test data (data used for testing)
# x -> examples, or images in this case
# y -> answers
# train_test_split splits in this example 30% of data to test set
x_train, x_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.3
)

# import MLP type neural network
from sklearn.neural_network import MLPClassifier

# clf -> classifier, algo which classifies elements (images) to categories (nums from 0 to 9)
clf = MLPClassifier(hidden_layer_sizes=(100, 100))
# fit data to categories
clf.fit(x_train, y_train)

# y_train_pred and y_train are tables with numpy
y_train_pred = clf.predict(x_train)
print((y_train_pred == y_train).mean())  # 1.0

# testing with y_test data
y_test_pred = clf.predict(x_test)
print((y_test_pred == y_test).mean()) # ~0.98