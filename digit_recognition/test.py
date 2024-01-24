from sklearn import datasets
digits = datasets.load_digits()

from skimage import io, transform
import numpy as np
upscaled_data = np.array(list(map(
    lambda img: transform.resize(
        img.reshape(8,8),
        (32, 32),
        mode='constant',
        preserve_range=True
    ).ravel(),
    digits.data
)))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    upscaled_data,
    digits.target,
    test_size=0.2,
    random_state=42
)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=1000, batch_size=32)
clf.fit(x_train, y_train)

y_test_pred = clf.predict(x_test)
print((y_test_pred == y_test).mean())

for i in range(3):
    input_image = io.imread('temp_image_{}.png'.format(str(i+1)), as_gray=True)

    resized_image = transform.resize(input_image, (32, 32), anti_aliasing=False)

    print(clf.predict([resized_image.flatten()])[0])
