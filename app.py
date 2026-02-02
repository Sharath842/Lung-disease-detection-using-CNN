  # File: app.py
from flask import Flask, request, jsonify, render_template
from ml_module import predict_function

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Call your ML function to make predictions
    result = predict_function(file)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
