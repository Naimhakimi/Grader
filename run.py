from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

model = tf.keras.models.load_model('palm_oil_grader_100.h5')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()
    image = input_data['image']
    image = image.reshape(-1, 28, 28, 1)
    prediction = model.predict(image).tolist()[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run()
