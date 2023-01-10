 from flask import Flask, render_template, request
import tensorflow as tf
app = Flask(__name__)
model = tf.keras.models.load_model('path/to/trained_model.h5')

@app.route('/generate', methods=['POST'])
def generate():
    noise = tf.random.normal([1, 100])
    generated_images = model(noise, training=False)
    # Saving the generated image with a random filename
    image_name = 'generated_image_{}.png'.format(random.randint(0,10000))
    tf.keras.preprocessing.image.save_img(image_name, generated_images[0])
    return render_template('show_image.html', image_path=image_name) 
