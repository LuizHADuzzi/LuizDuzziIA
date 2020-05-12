# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:10:00 2020

@author: duzzi
"""

from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input as preprocess_input2
from tensorflow.keras.applications.vgg16 import decode_predictions as decode_predictions2
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from tensorflow.keras.applications.inception_resnet_v2 import preprocess_input as preprocess_input3
from tensorflow.keras.applications.inception_resnet_v2 import decode_predictions as decode_predictions3
from tensorflow.keras.preprocessing import image
import numpy as np

## ResNet50##################################
model1 = ResNet50(weights="imagenet")
print("-----------RESNET50---------------")
img_path = 'elephant1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'elephant2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'elephant3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'microphone1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'microphone2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'microphone3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'chair1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'chair2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'chair3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'pen1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'pen2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'pen3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'spider1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'spider2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'spider3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'snake1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'snake2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

img_path = 'snake3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model1.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])

## VGG16##################################
model2 = VGG16(weights='imagenet')

print("-----------VGG16--------------")
img_path = 'elephant1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'elephant2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'elephant3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'microphone1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'microphone2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'microphone3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'chair1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'chair2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'chair3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'pen1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'pen2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'pen3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'spider1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'spider2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'spider3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'snake1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'snake2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

img_path = 'snake3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input2(x)
preds = model2.predict(x)
print('Predicted:', decode_predictions2(preds, top=3)[0])

## InceptionResNetV2##################################
model3 = InceptionResNetV2(weights='imagenet')

print("-----------NasNetLARGE--------------")
img_path = 'elephant1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'elephant2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'elephant3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'microphone1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'microphone2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'microphone3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'chair1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'chair2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'chair3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'pen1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'pen2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'pen3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'spider1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'spider2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'spider3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'snake1.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'snake2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])

img_path = 'snake3.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input3(x)
preds = model3.predict(x)
print('Predicted:', decode_predictions3(preds, top=3)[0])
