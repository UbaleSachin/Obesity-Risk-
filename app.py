from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.ObesityRisk.pipeline.prediction import PredictionPipeline,CoustomData

app = Flask(__name__)

@app.route('//', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/train', methods=['GET'])
def training():
    os.system('python main.py')
    return 'Training Successful..'


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = CoustomData(
        Gender = request.form.get('Gender'),
        Age = request.form.get('Age'),
        Height = request.form.get('Height'),
        Weight = request.form.get('Weight'),
        family_history_with_overweight = request.form.get('family_history_with_overweight'),
        FAVC = request.form.get('FAVC'),
        FCVC = request.form.get('FCVC'),                            
        NCP = request.form.get('NCP'),
        CAEC = request.form.get('CAEC'),   
        SMOKE = request.form.get('SMOKE'),
        CH2O = request.form.get('CH2O'),
        SCC = request.form.get('SCC'),
        FAF = request.form.get('FAF'),  
        TUE = request.form.get('TUE'),  
        CALC = request.form.get('CALC'),  
        MTRANS = request.form.get('MTRANS'),)

        
        prediction_df = data.get_data_as_dataframe()

        prediction = PredictionPipeline()
        result = prediction.predict(prediction_df)

        map_list={0:'Insufficient_Weight', 1:'Normal_Weight', 2:'Obesity_Type_I', 3:'Obesity_Type_II',
                    4:'Obesity_Type_III', 5:'Overweight_Level_I' ,6:'Overweight_Level_II'}
        for key, value in map_list.items():
            if result == key:
                return render_template('index.html', result=value)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000)