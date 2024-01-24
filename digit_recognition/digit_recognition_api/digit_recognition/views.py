from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from skimage import io, color, transform
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression


# Load the digits dataset (8x8 images)
digits = datasets.load_digits()

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)

def predict_digit(image_path):
    # Load and preprocess the image
    input_image = io.imread(image_path)[:,:,:3]
    gray_image = color.rgb2gray(input_image)  # Convert to grayscale
    resized_image = transform.resize(gray_image, (8, 8), anti_aliasing=True)
    
    # Make a prediction
    prediction = logisticRegr.predict([resized_image])
    print(prediction[0])
    return int(prediction[0])

@csrf_exempt
def predict_digit_api(request):
    if request.method == 'POST':
        try:
            # Assuming the image is sent as a file in the 'image' field
            image_file = request.FILES['image']
            image_path = 'temp_image.png'
            with open(image_path, 'wb') as f:
                f.write(image_file.read())

            # Make a prediction
            result = predict_digit(image_path)

            # Return the result as JSON
            return JsonResponse({"predicted_digit": result})
        except Exception as e:
            return JsonResponse({"error": str(e)})
        finally:
            f.close()
    else:
        return JsonResponse({"error": "Invalid request method"})
    