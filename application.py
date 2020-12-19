from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np

application = Flask(__name__)

model = load_model('ahraz_major1_prediction')
cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

@application.route('/')
def home():
    return render_template("index.html")

@application.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)
    prediction = int(prediction.Label[0])
    return render_template('index.html',pred='Expected Bill will be {}'.format(prediction))

if __name__ == '__main__':
    application.run(debug=True)
