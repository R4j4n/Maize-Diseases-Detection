import os
import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

# Create flask instance
app = Flask(__name__)
class_labels = ['Cercospora leaf spot (Gray leaf spot)',
                'Common rust',
                'Northern Leaf Blight',
                'healthy']

class_preventive_measures = [
    'Hybrids with partial resistance to GLS are available. Ask your seed supplier for these hybrids.A two-year crop rotation away from corn is effective if reduced tillage must be maintained for conservation purposes or a one-year rotation with clean plowing is recommended in fields that have had a problem with the disease.',
    'Use resistant/tolerant sweet corn products.Many sweet corn products have resistance  gene that provides nearly complete control.Applying strobilurin-and sterol-inhibiting fungicides as preventive measure.',
    'Management of Northern Leaf Blight can be achieved primarily by using hybrids with resistance, but because resistance may not be complete or may fail, it is advantageous to utilize an integrated approach with different cropping practices and fungicides',
    'Your plant is heathy :)']


img_rows, img_cols = 224, 224
image_size = [244, 244, 3]


def get_model():
    global model
    model = load_model('my_model.h5')
    print(" * Model loaded!")


# Set Max size of file as 10MB.
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# Allow files with extension png, jpg and jpeg
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def check(path):
    # prediction
    img = load_img(path, target_size=image_size)
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x.astype('float32') / 255
    z = model.predict(x)
    index = np.argmax(z)

    accuracy = int(np.array(z).max() * 100)
    return [index, accuracy]


get_model()


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if (file):
            try:
                if file and allowed_file(file.filename):
                    filename = file.filename
                    file_extension = filename.split('.')[-1]
                    file_path = os.path.join('static/images', "testing-image."+file_extension)
                    file.save(file_path)
                    result = check(file_path)
                    # Predict the class of an image
                    disease_name = class_labels[result[0]]

                    accuracy = result[1]

                    return render_template('predict.html',
                                           disease_name=disease_name,
                                           user_image=file_path,
                                           accuracy=accuracy,
                                           preventive_measures=class_preventive_measures[result[0]])
            except Exception as e:
                return "Error : " + str(e)

        else:
            eMessage = "Please Upload the diseased file"
            return redirect(url_for('predict', error = eMessage))

    elif (request.method == 'GET'):
        # redirect(url_for("home"))
        return redirect(url_for('predict'))

@app.route('/download-image/<path:filename>')
def download(filename):
    return send_from_directory('static', filename, as_attachment=True, mimetype='image/jpg', attachment_filename=(str(filename) + '.jpg'))


if __name__ == "__main__":
    app.run(debug=True)
