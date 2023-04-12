!pip install -q tflite-model-maker
!pip install -q tflite-support

import numpy as np
import os

from tflite_model_maker.config import ExportFormat, QuantizationConfig
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

from tflite_support import metadata

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)


from google.colab import drive
drive.mount('/content/gdrive')
!ln -s /content/gdrive/My\ Drive/ /mydrive
!ls /mydrive

train_data = object_detector.DataLoader.from_pascal_voc(
    'adv_iot/train',
    'adv_iot/train',
    ['sharp', 'guns']
)

val_data = object_detector.DataLoader.from_pascal_voc(
    'adv_iot/validate',
    'adv_iot/validate',
    ['sharp', 'guns']
)

spec = model_spec.get('efficientdet_lite0')

model = object_detector.create(train_data, model_spec=spec, batch_size=4, train_whole_model=True, epochs=20, validation_data=val_data)

model.evaluate(val_data)

model.export(export_dir='.', tflite_filename='android.tflite')



