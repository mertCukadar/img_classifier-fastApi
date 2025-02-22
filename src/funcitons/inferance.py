from PIL import Image
import numpy as np
from io import BytesIO 
from src.funcitons.Utils import Utils
import tensorflow as tf


model = tf.keras.models.load_model('src/models/Trafic_signs_model.h5')  # Modelin yolu

def inference(image_data):
    image = Image.open(BytesIO(image_data)) 
    image = image.convert('RGB')
    image = image.resize((30, 30))  
    image = np.array(image)  
    image = np.expand_dims(image, axis=0)  

    pred = np.argmax(model.predict(image), axis=1)[0]  
    sign = Utils.classes[pred + 1]  
    
    print(sign)
    print(pred)

    return sign
