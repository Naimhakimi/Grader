import gradio as gr
import tensorflow as tf
class_names = ['Overripe', 'Ripe', 'Underipe', 'Unripe']
# Load the trained model
model = tf.keras.models.load_model("palm_oil_grader_100.h5")
def predict_image(img):
  img_3d=img.reshape(-1,224,224,3)
  prediction=model.predict(img_3d).flatten()
  return {class_names[i]: float(prediction[i]) for i in range(4)}


image = gr.inputs.Image(shape=(224,224))
label = gr.outputs.Label(num_top_classes=4)

gr.Interface(fn=predict_image, inputs=image, outputs=label,interpretation='default').launch(debug='True')
