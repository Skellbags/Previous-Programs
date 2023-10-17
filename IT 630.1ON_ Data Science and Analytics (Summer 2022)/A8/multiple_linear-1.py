"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
A8 - 6/26/22 - Purpose:
    Testing Scikit-learns Linear Regression capabilities
    on the pimaSmall data set
Note:
    None
Supported Files:
    pimaSmall.csv
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#from sklearn.cross_validation import train_test_split
#new version of sklearn has train_test_split in model_selection library
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn import metrics  

#fill up a dataframe with data
dataset = pd.read_csv('pimaSmall.csv')  
print(dataset.shape)
print(dataset.head())
print(dataset.describe())

#prepare the data
#create attributes and labels
#use column names for creating an attribute set and label
x = dataset[['Pregnancy','Plasma-Glucose','Blood-Pressure','Tricep-Thickness','Serum-Insulin','BMI','Diabetes-Ancestory','Age']]
y = dataset['hasDiabetes'] 
"""paste into csv header
Pregnancy,Plasma-Glucose,Blood-Pressure,Tricep-Thickness,Serum-Insulin,BMI,Diabetes-Ancestory,Age,hasDiabetes
"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(x_train, y_train) 

print()
#the regression model has to find the most optimal coefficients for all the attributes
coeff_df = pd.DataFrame(regressor.coef_, x.columns, columns=['Coefficient'])  
print(coeff_df)

y_pred = regressor.predict(x_test)  
print()
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
print(df)
print()
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)),"\n")
print("Based on the output values, what I've read online, and what we went over in class, I know that Linear Regression is a suitable candidate for classifying this data. I know this due to the output of the root mean square error value being close to 0. \nThe RMSD or RMSE(Deviation vs Error) value is a summary of how good a job the algorithm selects the classification, a value of absolute 0 indicates perfect prediction, while large values indicate prediction complications. \nThe RMSE of ~0.5 is comparativly much better than the RMSE of the petroleum dataset(~68.3).")
print("\n#####################################################\n")




