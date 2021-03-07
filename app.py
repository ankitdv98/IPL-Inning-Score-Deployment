# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:44:30 2021

@author: Ankit Yadav
"""

from flask import Flask, render_template, redirect, url_for, request
import pickle
import numpy as np
app= Flask(__name__)

file= 'lasso_regressor.pickle'
regressor= pickle.load(open(file, 'rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods= ["POST","GET"])
def predict():
    temp= []
    if request.method== "POST":
        runs= int(request.form['runs'])
        overs= float(request.form['overs'])
        wickets= int(request.form['wickets'])
        runs_last_5= int(request.form['runs_last_5'])
        wickets_last_5= int(request.form['wickets_last_5'])
        
        temp = temp + [runs, overs, wickets, runs_last_5, wickets_last_5]
        batting_team= request.form['batting-team']
        if batting_team== "Chennai Super Kings":
            temp= temp + [0,0,0,0,0,0,0]
        elif batting_team== "Delhi Daredevils":
            temp= temp + [1,0,0,0,0,0,0]
        elif batting_team== "Kings XI Punjab":
            temp= temp + [0,1,0,0,0,0,0]
        elif batting_team== "Kolkata Knight Riders":
            temp= temp + [0,0,1,0,0,0,0]
        elif batting_team== "Mumbai Indians":
            temp= temp + [0,0,0,1,0,0,0]
        elif batting_team== "Rajasthan Royals":
            temp= temp + [0,0,0,0,1,0,0]
        elif batting_team== "Royal Challengers Bangalore":
            temp= temp + [0,0,0,0,0,1,0]
        elif batting_team== "Sunrisers Hyderabad":
            temp= temp + [0,0,0,0,0,0,1]
        
        bowling_team= request.form['bowling-team']
        if bowling_team== "Chennai Super Kings":
            temp= temp + [0,0,0,0,0,0,0]
        elif bowling_team== "Delhi Daredevils":
            temp= temp + [1,0,0,0,0,0,0]
        elif bowling_team== "Kings XI Punjab":
            temp= temp + [0,1,0,0,0,0,0]
        elif bowling_team== "Kolkata Knight Riders":
            temp= temp + [0,0,1,0,0,0,0]
        elif bowling_team== "Mumbai Indians":
            temp= temp + [0,0,0,1,0,0,0]
        elif bowling_team== "Rajasthan Royals":
            temp= temp + [0,0,0,0,1,0,0]
        elif bowling_team== "Royal Challengers Bangalore":
            temp= temp + [0,0,0,0,0,1,0]
        elif bowling_team== "Sunrisers Hyderabad":
            temp= temp + [0,0,0,0,0,0,1]
        
        array= np.array(temp)
        my_pred= int(regressor.predict(array.reshape(1, -1))[0])
        
        return render_template('result.html', lower_limit= my_pred-10, upper_limit= my_pred+5)
    else:
        return render_template('index.html')







if __name__== '__main__':
    app.run(debug= True)