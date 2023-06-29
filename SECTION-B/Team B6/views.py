from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from math import sqrt

global dataset, kmeans_cluster, theft_cls, rape_cls, murder_cls

sc = MinMaxScaler(feature_range = (0, 1))
le1 = LabelEncoder()
le2 = LabelEncoder()

le3 = LabelEncoder()
le4 = LabelEncoder()

global mse, rmse

def calculateError(alg, X_test, y_test):
    predict = alg.predict(X_test)
    #predict = predict.reshape(predict.shape[0],1)
    #predict = sc.inverse_transform(predict)
    predict = predict.ravel()
    #labels = sc.inverse_transform(y_test)
    labels = y_test.ravel()
    mse_error = mean_squared_error(labels,predict)
    rmse_error = sqrt(mse_error)
    mse.append(mse_error/1000)
    rmse.append(rmse_error)

def UploadDatasetAction(request):
    if request.method == 'POST':
        global dataset, kmeans_cluster, theft_cls, rape_cls, murder_cls, mse, rmse
        mse = []
        rmse = []
        myfile = request.FILES['t1']
        dataset = pd.read_csv("Dataset/Dataset.csv", usecols=['States/UTs','District', 'Murder', 'Rape', 'Theft', 'Dowry_Deaths', 'Year'])
        dataset.fillna(0, inplace = True)
        cols = ['States/UTs', 'District']
        dataset[cols[0]] = pd.Series(le1.fit_transform(dataset[cols[0]].astype(str)))
        dataset[cols[1]] = pd.Series(le2.fit_transform(dataset[cols[1]].astype(str)))
        X = dataset.values
        X = sc.fit_transform(X)
        kmeans_cluster = KMeans(n_clusters=2, n_init=1200)
        kmeans_cluster.fit(X)

        dataset = pd.read_csv("Dataset/Dataset.csv", usecols=['States/UTs','District', 'Year', 'Theft', 'Murder', 'Rape'])
        dataset.fillna(0, inplace = True)
        print(dataset)
        cols = ['States/UTs', 'District']
        dataset[cols[0]] = pd.Series(le3.fit_transform(dataset[cols[0]].astype(str)))
        dataset[cols[1]] = pd.Series(le4.fit_transform(dataset[cols[1]].astype(str)))
        theft_Y = dataset['Theft'].values
        murder_Y = dataset['Murder'].values
        rape_Y = dataset['Rape'].values
        dataset.drop(['Theft'], axis = 1,inplace=True)
        dataset.drop(['Murder'], axis = 1,inplace=True)
        dataset.drop(['Rape'], axis = 1,inplace=True)
        X = dataset.values

        X_train1, X_test1, y_train1, y_test1 = train_test_split(X, theft_Y, test_size = 0.2)
        X_train2, X_test2, y_train2, y_test2 = train_test_split(X, rape_Y, test_size = 0.2)
        X_train3, X_test3, y_train3, y_test3 = train_test_split(X, murder_Y, test_size = 0.2)

        theft_cls = RandomForestRegressor()
        theft_cls.fit(X, theft_Y)
        calculateError(theft_cls, X_test1, y_test1)

        rape_cls = RandomForestRegressor()
        rape_cls.fit(X, rape_Y)
        calculateError(rape_cls, X_test2, y_test2)

        murder_cls = RandomForestRegressor()
        murder_cls.fit(X, murder_Y)
        calculateError(murder_cls, X_test3, y_test3)
        
        dataset = pd.read_csv("Dataset/Dataset.csv")
        dataset.fillna(0, inplace = True)
        columns = list(dataset.columns)
        strdata = '<table border=1 align=center width=100%><tr><th><font size="" color="black">'+columns[0]+'</th>'
        for i in range(1,len(columns)):
            strdata+='<th><font size="" color="black">'+columns[i]+'</th>'
        strdata += "</tr>"
        dataset = dataset.values
        for i in range(len(dataset)):
            strdata += "<tr>"
            for j in range(len(dataset[i])):
                strdata+='<td><font size="" color="black">'+str(dataset[i,j])+'</td>'
            strdata += "</tr>"
        context= {'data':strdata}            
        return render(request, 'ViewDataset.html', context)                    
    
def AdminLogin(request):
    if request.method == 'POST':
        user = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        if user == 'admin' and password == 'admin':
            context= {'data':user}            
            return render(request, 'AdminScreen.html', context)
        else:
            context= {'data':"Invalid login details"}            
            return render(request, 'Admin.html', context)            
        
def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def Admin(request):
    if request.method == 'GET':
       return render(request, 'Admin.html', {})

def UploadDataset(request):
    if request.method == 'GET':
       return render(request, 'UploadDataset.html', {})

def MSEGraph(request):
    if request.method == 'GET':
        strdata = '<table border=1 align=center width=100%><tr><th><font size="" color="black">Algorithm Name</th><th><font size="" color="black">RMSE</th>'
        strdata+='<th><font size="" color="black">MSE</th></tr>'
        strdata+='<tr><td><font size="" color="black">Random Forest Theft Prediction</td><td><font size="" color="black">'+str(rmse[0])+'</td>'
        strdata+='<td><font size="" color="black">'+str(mse[0])+'</td>'
        strdata+='<tr><td><font size="" color="black">Random Forest Rape Prediction</td><td><font size="" color="black">'+str(rmse[1])+'</td>'
        strdata+='<td><font size="" color="black">'+str(mse[1])+'</td>'
        strdata+='<tr><td><font size="" color="black">Random Forest Murder Prediction</td><td><font size="" color="black">'+str(rmse[2])+'</td>'
        strdata+='<td><font size="" color="black">'+str(mse[2])+'</td></tr></table>'

        df = pd.DataFrame([['Random Forest Theft Prediction','RMSE',rmse[0]],['Random Forest Theft Prediction','MSE',mse[0]],
                           ['Random Forest Rape Prediction','RMSE',rmse[1]],['Random Forest Rape Prediction','MSE',mse[1]],
                           ['Random Forest Murder Prediction','RMSE',rmse[2]],['Random Forest Murder Prediction','MSE',mse[2]],
                          ],columns=['Parameters','Algorithms','Value'])
        df.pivot("Parameters", "Algorithms", "Value").plot(kind='bar')
        plt.show()
        context= {'data':strdata}
        return render(request, 'Comparison.html', context)
                                                        
                                                                                                                               

def ClusterPrediction(request):
    if request.method == 'GET':
        dataset = pd.read_csv("Dataset/Dataset.csv", usecols=['States/UTs','District', 'Year'])
        dataset.fillna(0, inplace = True)
        states = np.unique(dataset['States/UTs'].values)
        output = '<tr><td><font size="" color="black">States</b></td><td><select name="t1">'
        for i in range(len(states)):
            output += '<option value="'+states[i]+'">'+states[i]+'</option>' 
        output += "</select></td></tr>"
        output += '<tr><td><font size="" color="black">District</b></td><td><select name="t2">'
        for i in range(len(states)):
            district = dataset[dataset['States/UTs'] == states[i]]['District']
            district = district.values
            output += '<option value="'+states[i]+'"><b>--'+states[i]+'--</b></option>'
            for j in range(len(district)):
                output += '<option value="'+district[j]+'">'+district[j]+'</option>' 
        output += "</select></td></tr>"
        output += '<tr><td><font size="" color="black">Year</b></td><td><select name="t3">'
        year = np.unique(dataset['Year'].values)
        for i in range(len(year)):
            output += '<option value="'+str(year[i])+'">'+str(year[i])+'</option>'         
        output += "</select></td></tr>"
        context= {'states':output}
        return render(request, 'ClusterPrediction.html', context)

def ClusterPredictionAction(request):
    if request.method == 'POST':
        state = request.POST.get('t1', False)
        district = request.POST.get('t2', False)
        year = request.POST.get('t3', False)
        murder = request.POST.get('t4', False)
        rape = request.POST.get('t5', False)
        theft = request.POST.get('t6', False)
        dowry = request.POST.get('t7', False)
        temp = []
        temp.append([state, district, murder, rape, theft, dowry, year])
        test = pd.DataFrame(temp, columns=['States/UTs','District', 'Murder', 'Rape', 'Theft', 'Dowry_Deaths', 'Year'])
        test.fillna(0, inplace = True)
        test['States/UTs'] = pd.Series(le1.transform(test['States/UTs'].astype(str)))
        test['District'] = pd.Series(le2.transform(test['District'].astype(str)))
        test = test.values
        test = sc.transform(test)
        predict = kmeans_cluster.predict(test)
        print(predict)
        output = district+" Low Crime Rate Area"
        if predict == 1:
            output = district+" High Crime Rate Area"
        context= {'data':output}
        return render(request, 'index.html', context)    
        


def FuturePrediction(request):
    if request.method == 'GET':
        dataset = pd.read_csv("Dataset/Dataset.csv", usecols=['States/UTs','District', 'Year'])
        dataset.fillna(0, inplace = True)
        states = np.unique(dataset['States/UTs'].values)
        output = '<tr><td><font size="" color="black">States</b></td><td><select name="t1">'
        for i in range(len(states)):
            output += '<option value="'+states[i]+'">'+states[i]+'</option>' 
        output += "</select></td></tr>"
        output += '<tr><td><font size="" color="black">District</b></td><td><select name="t2">'
        for i in range(len(states)):
            district = dataset[dataset['States/UTs'] == states[i]]['District']
            district = district.values
            output += '<option value="'+states[i]+'"><b>--'+states[i]+'--</b></option>'
            for j in range(len(district)):
                output += '<option value="'+district[j]+'">'+district[j]+'</option>' 
        output += "</select></td></tr>"
        output += '<tr><td><font size="" color="black">Year</b></td><td><select name="t3">'
        year = np.unique(dataset['Year'].values)
        for i in range(len(year)):
            output += '<option value="'+str(year[i])+'">'+str(year[i])+'</option>'
        output += '<option value="2022">2022</option>'
        output += '<option value=2023>2023</option>' 
        output += "</select></td></tr>"
        context= {'states':output}
        return render(request, 'FuturePrediction.html', context)


def FuturePredictionAction(request):
    if request.method == 'POST':
        state = request.POST.get('t1', False)
        district = request.POST.get('t2', False)
        year = request.POST.get('t3', False)
        classify_type = request.POST.get('t4', False)
        temp = []
        temp.append([state, district, year])
        test = pd.DataFrame(temp, columns=['States/UTs','District', 'Year'])
        test.fillna(0, inplace = True)
        test['States/UTs'] = pd.Series(le1.transform(test['States/UTs'].astype(str)))
        test['District'] = pd.Series(le2.transform(test['District'].astype(str)))
        test = test.values
        predict = 0
        if classify_type == "Theft":
            predict = "Future Predicted Thefts = "+str(int(theft_cls.predict(test)[0]))
        if classify_type == "Murder":
            predict = "Future Predicted Murders = "+str(int(murder_cls.predict(test)[0]))
        if classify_type == "Rape":
            predict = "Future Predicted Rapes = "+str(int(rape_cls.predict(test)[0]))    
        context= {'data':predict}
        return render(request, 'index.html', context)  

def Analysis(request):
    if request.method == 'GET':
       return render(request, 'Analysis.html', {})

def AnalysisAction(request):
    if request.method == 'POST':
        classify_type = request.POST.get('t1', False)
        strdata = '<table border=1 align=center width=100%>'
        if classify_type == "Theft":
            strdata += '<tr><td><img src="static/analysis/theft_bar.png" height="300" width="500"/></td></tr>'
            strdata += '<tr><td><img src="static/analysis/theft_pie.png" height="300" width="500"/></td></tr>'
        if classify_type == "Murder":
            strdata += '<tr><td><img src="static/analysis/murder_bar.png" height="300" width="500"/></td></tr>'
            strdata += '<tr><td><img src="static/analysis/murder_pie.png" height="300" width="500"/></td></tr>'
        if classify_type == "Rape":
            strdata += '<tr><td><img src="static/analysis/rape_bar.png" height="300" width="500"/></td></tr>'
            strdata += '<tr><td><img src="static/analysis/rape_pie.png" height="300" width="500"/></td></tr>'    
        context= {'data':strdata}            
        return render(request, 'ViewGraphs.html', context)    





    
    
