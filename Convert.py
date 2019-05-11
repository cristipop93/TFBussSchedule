import tensorflow as tf

converter = tf.contrib.lite.TFLiteConverter.from_saved_model('/home/cpop/Documents/1557607409', signature_key='predict')
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
