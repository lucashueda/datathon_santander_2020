import numpy as np
import keras
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense, Flatten, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.applications.inception_v3 import decode_predictions
from sklearn.metrics import confusion_matrix
from sklearn.metrics import average_precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from tensorflow.keras.models import model_from_json
import itertools
import matplotlib.pyplot as plt
import time
import pandas as pd
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input

def get_image(path):
    img = image.load_img(path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return img, x

# Lendo o modelo

# Testando dando load no modelo
json_file = open('model_weigths/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model_weigths/model.h5")

# Prevendo o label para cada imagem no diretório "test_images"
import os 

map_item = {0 : 'Fone de ouvido', 1: 'Impressora', 2: 'Roteador'}

items = []
for item in os.listdir('test_images'):
  img, x = get_image('test_images/'+ item)
  pred = loaded_model(x)
  items.append(map_item[np.argmax(pred)])

pd.DataFrame({'inventario': items}).to_csv('inventario.csv', index = False)

print(f"Voce possui os seguintes itens no seu inventario: {items}")
