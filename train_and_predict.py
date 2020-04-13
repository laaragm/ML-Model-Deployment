import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

#df = pd.read_csv('/home/larag/Documents/Projetos Data Science/ML Model Deployment/train.csv')
df = pd.read_csv('train.csv')

df.isnull().any() #checking which are the columns that contains NaN values in it
df = df.fillna(method='ffill') #removing all the null values

features = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_REDACAO']
target = 'NU_NOTA_MT'

x_train = df[features] #data frame
y_train = df[target] #series

model = RandomForestRegressor()
model.fit(x_train, y_train)  

#exporting trained model to a file
file = 'model.pkl'
pickle.dump(model, open(file, 'wb'))

def predict(data):
    df = pd.DataFrame([data], columns=features)
    x_test = df[features]
    y_pred = model.predict(x_test)
   
    return y_pred

"""
data = {"NU_NOTA_CN": 450.3, "NU_NOTA_CH": 600.5, "NU_NOTA_LC": 634.9, "NU_NOTA_REDACAO": 800.0}
y_pred = predict(data)
print(float(y_pred))
"""