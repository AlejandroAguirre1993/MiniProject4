{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import pickle
import pandas as pd
app = Flask(__name__)
api = Api(app)
model = pickle.load( open( "src/model.pkl", "rb" ) )
class MakePrediction(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        X = pd.DataFrame([posted_data])
      
#        Gender = posted_data['Gender']
#        Married = posted_data['Married']
#        Dependents = posted_data['Dependents']
#        Education = posted_data['Education']
#        Self_Employed = posted_data['Self_Employed']
#        ApplicantIncome = posted_data['ApplicantIncome']
#        CoapplicantIncome = posted_data['CoapplicantIncome']
#        LoanAmount = posted_data['LoanAmount']
#        Loan_Amount_Term= posted_data['Loan_Amount_Term']
#        Credit_History = posted_data['Credit_History']
#        Property_Area = posted_data['Property_Area']
        prediction =  model.predict(X)[0]
        if prediction == 'Y':
            predicted_class = 'Loan Accepted'
        elif prediction == 'N':
            predicted_class = 'Loan Rejected'
        else:
             predicted_class = 'No Results'
        return jsonify({
            'Prediction': predicted_class
        })
api.add_resource(MakePrediction, '/predict')
if __name__ == '__main__':
    app.run(debug=True)