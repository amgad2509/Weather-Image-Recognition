#from gettext import install

import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import cv2
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from tensorflow.keras.backend import argmax
from keras.models import load_model
from efficientnet.tfkeras import EfficientNetB0
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)

model = load_model(r'best_model_.h5', compile=False)

def get_className(classNo):
    if classNo==0:
        return "dew"
    elif classNo==1:
        return "fogsmog"
    elif classNo==2: 
        return "frost"
    elif classNo==3:
        return "glaze"
    elif classNo==4:
        return "hail"  
    elif classNo==5:
        return "lightning"
    elif classNo==6:
        return "rain"
    elif classNo==7:
        return "rainbow"
    elif classNo==8:
        return "rime"
    elif classNo==9:
        return "sandstorm"
    elif classNo==10:
        return "snow"

# class_mapping = {
#     0: 'dew',
#     1: 'fogsmog',
#     2: 'frost',
#     3: 'glaze',
#     4: 'hail',
#     5: 'lightning',
#     6: 'rain',
#     7: 'rainbow',
#     8: 'rime',
#     9: 'sandstorm',
#     10: 'snow'
# }
def getResult(img):
    imge = cv2.imread(img)
    img = Image.fromarray(imge)
    
    img = img.resize((224,224))
    img = np.array(img)
    
    input_img = np.expand_dims(img,axis=0)
    img_array = input_img / 255.0
    img_array = tf.keras.applications.efficientnet.preprocess_input(input_img)
    
    #Predication
    predictions = model.predict(img_array)
    classes_x=argmax(predictions,axis=1)
    #print(classes_x)
    return classes_x


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('logo.html')

@app.route('/take_photo', methods=['GET'])
def take_photo():
    return render_template('photo.html')

@app.route('/predict', methods = ['POST'])
def predict():
    f = request.files['file']
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
    f.save(file_path)
    value=getResult(file_path)
    result=get_className(value) 
    return render_template('photo.html', prediction_text= result)


if __name__ == '__main__':
    app.run(debug=True)