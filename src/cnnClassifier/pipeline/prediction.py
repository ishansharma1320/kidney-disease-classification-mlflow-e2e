import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, file_name):
        self.filename = file_name

    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))
        image_name = self.filename
        test_image = image.load_img(image_name, target_size=(299, 299))

        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)

        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
        else:
            prediction = 'Normal'

        return [{"image": prediction}]