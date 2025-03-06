import pandas as pd
import numpy as np
import pickle
import os
from flask import Flask , render_template , jsonify, request,redirect

app= Flask (__name__)

#pre = pickle.load(open('model.pkl','rb'))

decision_tree = os.path.join('static','img')
app.config['UPLOAD_FOLDER']=decision_tree
temp=[];

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/selectpg')
def selectpg():
    return render_template('selectmodel.html')

@app.route('/selectmodel',methods=['GET' , 'POST'])
def selectmodel():
    opt=request.form['Model']
    temp.append(opt)
    return render_template('MLmodel.html')

#@app.route('/nxtpg')
#def nxtpg():
#    return render_template('MLmodel.html')



@app.route('/MLmodel', methods=['GET' , 'POST'])
def MLmodel():
   # opt=request.form['Model']
    ML = temp.pop()
    if ML == '1':
        pre = pickle.load(open('CART.pkl','rb'))
        d1=request.form['gender']
        d2=request.form['age']
        d3=request.form['region']
        d4=request.form['healthcheckup']
        d5=request.form['healthscale']
        d6=request.form['capacity']
        d7=request.form['stepcount']
        d8=request.form['sleephrs']
        d9=request.form['chronicpain']
        d10=request.form['Diseases']
        d11=request.form['Addiction']
        d12=request.form['Activities']
        d13=request.form['mentalhealth']
        d14=request.form['Insurance']
        arr=np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]])
        ip=arr.reshape(1,-1)
        pred = pre.predict(ip)
        dti = os.path.join(app.config['UPLOAD_FOLDER'], 'physical_health.png')
        return render_template('result.html',data=pred,user_image =dti,SML=ML)
    
    elif ML == '2':
        pre = pickle.load(open('C45.pkl','rb'))
        d1=request.form['gender']
        d2=request.form['age']
        d3=request.form['region']
        d4=request.form['healthcheckup']
        d5=request.form['healthscale']
        d6=request.form['capacity']
        d7=request.form['stepcount']
        d8=request.form['sleephrs']
        d9=request.form['chronicpain']
        d10=request.form['Diseases']
        d11=request.form['Addiction']
        d12=request.form['Activities']
        d13=request.form['mentalhealth']
        d14=request.form['Insurance']
        arr=np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]])
        ip=arr.reshape(1,-1)
        pred = pre.predict(ip)
        dti = os.path.join(app.config['UPLOAD_FOLDER'], 'C4.5_physical_health.png')
        return render_template('result.html',data=pred,user_image =dti,SML=ML)
    
    elif ML == '3':
        pre = pickle.load(open('RBC.pkl','rb'))
        d1=request.form['gender']
        d2=request.form['age']
        d3=request.form['region']
        d4=request.form['healthcheckup']
        d5=request.form['healthscale']
        d6=request.form['capacity']
        d7=request.form['stepcount']
        d8=request.form['sleephrs']
        d9=request.form['chronicpain']
        d10=request.form['Diseases']
        d11=request.form['Addiction']
        d12=request.form['Activities']
        d13=request.form['mentalhealth']
        d14=request.form['Insurance']
        arr=np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]])
        ip=arr.reshape(1,-1)
        pred = pre.predict(ip)
        dti = os.path.join(app.config['UPLOAD_FOLDER'], 'RFC_tree.png')
        return render_template('result.html',data=pred,user_image =dti,SML=ML)
    
    elif ML == '4':
        pre = pickle.load(open('GBC.pkl','rb'))
        d1=request.form['gender']
        d2=request.form['age']
        d3=request.form['region']
        d4=request.form['healthcheckup']
        d5=request.form['healthscale']
        d6=request.form['capacity']
        d7=request.form['stepcount']
        d8=request.form['sleephrs']
        d9=request.form['chronicpain']
        d10=request.form['Diseases']
        d11=request.form['Addiction']
        d12=request.form['Activities']
        d13=request.form['mentalhealth']
        d14=request.form['Insurance']
        arr=np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]])
        ip=arr.reshape(1,-1)
        pred = pre.predict(ip)
        dti = os.path.join(app.config['UPLOAD_FOLDER'], 'GBC_tree.png')
        return render_template('result.html',data=pred,user_image =dti,SML=ML)
    
    else : 
        return render_template('selectmodel.html')
    
    

@app.route('/result')
def result():
        return render_template('result.html')



if __name__=="__main__":
    app.run(debug=True)
