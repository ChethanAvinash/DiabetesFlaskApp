# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 23:06:58 2020

@author: user
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
from keras.models import load_model
from time import sleep

app = Flask(__name__)
model = load_model("diabetes-model.h5")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    prediction = model.predict([int_features])
    output = round(prediction[0][0])
    print(output)
    
    if output == 1:
        return render_template('index.html', prediction_text='78% Sure! You Have Diabetes')
    else:
        return render_template('index.html', prediction_text='78% Sure! You Dont Have Diabetes')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port='3000',debug=True,)
