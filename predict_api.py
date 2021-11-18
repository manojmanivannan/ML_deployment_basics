import pickle
model = pickle.load(open('model.pkl','rb'))

from flask import Flask, request
from flask_ngrok import run_with_ngrok
import requests

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/predict',methods=['POST'])
def home():
    X = int(request.args.get('X',''))
    Y = int(request.args.get('Y',''))
    month = int(request.args.get('month',''))
    day = int(request.args.get('day',''))
    FFMC = float(request.args.get('FFMC',''))
    DMC = float(request.args.get('DMC',''))
    DC = float(request.args.get('DC',''))
    ISI = float(request.args.get('ISI',''))
    temp = float(request.args.get('temp',''))
    RH = float(request.args.get('RH',''))
    wind = float(request.args.get('wind',''))
    rain = float(request.args.get('rain',''))
    prediction = model.predict([[X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,wind,rain]])
    print('**************************************')
    print(prediction)
    return 'Prediction is ' + str(prediction[0])

app.run()

