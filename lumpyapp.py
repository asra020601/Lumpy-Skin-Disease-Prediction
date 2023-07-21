from flask import Flask, render_template,request
from sklearn import *
from flask import *  
import numpy as np
app = Flask(__name__)
import pickle
import joblib
model = pickle.load(open("model.pkl",'rb'))
scale = pickle.load(open("scale.pkl",'rb'))
ct = joblib.load('column')
@app.route('/')
def home():
   return render_template('first_page.html')
@app.route('/form')
def form():
  return render_template('form_page.html')
@app.route('/eda')
def eda():
  return render_template('eda_page.html')
@app.route('/guest', methods = ["POST"])
def Guest():
   a = request.form['a']
   b = request.form['b']
   c = request.form['c']
   d = request.form['d']
   e = request.form['e']
   f = request.form['f']
   g = request.form['g']
   h = request.form['h']
   i = request.form['i']
   j = request.form['j']
   k = request.form['k']
   l = request.form['l']
   m = request.form['m']
   data = [[a,b,c,d,e,f,g,h,i,j,k,l,m]]
   data =ct.transform(data)
   data = scale.fit_transform(data)
   prediction = model.predict(data)  # features Must be in the form [[a, b]]
   if prediction==0:
      session['output'] = 'Yes. With the help of meteorological and geospatial features we suspect a strong possibility of the occurrence of Lumpy Skin Disease (LSD) in this area.'  
   else: session['output'] = 'No. With the help of meteorological and geospatial features we DO NOT  see the possibility of the occurrence of Lumpy Skin Disease (LSD) in this area'  
   
   return predict()

@app.route('/predict')
def predict():
    return render_template('predict_page.html', prediction_text=' {}'.format(session['output']))
if __name__ == '__main__':
   app.config['SECRET_KEY'] = 'some random string'
   app.secret_key = 'super secret key'
   app.run(debug = True)