import tensorflow as tf
from flask import Flask, request, jsonify
import numpy as np

# Load the dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the images
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build the model
model = tf.keras.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
model.evaluate(x_test, y_test)

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the default URL
@app.route('/')
def generate_image():
  # Generate an image
  image = model.predict(np.random.rand(1, 28, 28))
  
  # Return the image as a response
  return jsonify(image.tolist())

# Run the app
if __name__ == '__main__':
  app.run(debug=True)
