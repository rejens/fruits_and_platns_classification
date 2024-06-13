from flask import Flask,render_template,request
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)


print(tf.__version__)
print(hub.__version__)


def load_model(model_path):
  model = tf.keras.models.load_model(model_path,custom_objects={"KerasLayer":hub.KerasLayer})
  return model

model = load_model("model.h5")
  

def load_labels():
   image_labels = pd.read_csv("labels.csv")["0"].values
   return image_labels

image_labels = load_labels()


def process_image(image):
   """ this function here is to pro process the image to be in the right format for the model to predict"""
   # image = tf.io.read_file(image_path)
   image = tf.io.decode_jpeg(image,channels=3)
   # image =tf.image.convert_image_dtype(image,tf.float32)
   image = np.expand_dims(image,axis=0)
   image = tf.image.resize(image, size=[224, 224])
   return image

def perform_prediction(image):
  # process the image first
  image = process_image(image)
  # # predict the image now
  predict = model.predict(image)
  # find the label of the image
  label = image_labels[predict.argmax()]
  return label
  


@app.route('/',methods=['GET','POST'])
def hello_world():
      if (request.method == 'POST'):
            image = request.files["image"].read()

            label = perform_prediction(image)
            return("the prediction is"+ label)
           
      else:
         # return("prediction here "+perform_prediction("D:/ml/flask/fruits_and_platns_classification/img/apple.jpg"))

         return render_template('form.html')
      


if __name__ == '__main__':
      app.run()
      