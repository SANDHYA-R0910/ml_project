from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,predictPipeline

application = Flask(__name__)

app = application 

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        reading_score = request.form.get('reading_score')
        writing_score = request.form.get('writing_score')
        print(reading_score, writing_score)
        if reading_score is None or writing_score is None:
            # Handle the case when one or both values are None
            # You can assign default values or take alternative actions
            # For example:
            reading_score = 0.0
            writing_score = 0.0
        else:
            reading_score = float(reading_score)
            writing_score = float(writing_score)
            
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score = reading_score,
            writing_score = writing_score,
        )
        pred_df = data.get_data_as_data_frame()
        pred_df.columns = ["gender","race/ethnicity","parental level of education","lunch","test preparation course","reading score","writing score"]
        print(pred_df)
        predict_pipeline = predictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    
if __name__ == '__main__':
    app.run(host="0.0.0.0")