import pandas as pd
import matplotlib.pyplot as plt
#Question 1
data=pd.read_csv("insurance.csv")
data.dropna(inplace=True)
print(data.to_string())
#Question 2
#using mean
data=pd.read_csv("insurance.csv")
data["charges"].fillna(data["charges"].mean(),inplace=True)
print(data.to_string())
#using median
data=pd.read_csv("insurance.csv")
data["charges"].fillna(data["charges"].median(),inplace=True)
print(data.to_string())
#using mode
data=pd.read_csv("insurance.csv")
data["charges"].fillna(data["charges"].mode(),inplace=True)
print(data.to_string())
#Question 3
data=pd.read_csv("insurance.csv")
for x in data.index:
    if data.loc[x,"age"]>60:
        data.loc[x,"age"]=50
print(data.to_string())
#Question 4
data=pd.read_csv("insurance.csv")
x=data.duplicated()
print(x.to_string())
data.drop_duplicates(inplace=True)
print(data.to_string())
#Question 5
data=pd.read_csv("insurance.csv")
print(data.corr().to_string())
#Question 6
data=pd.read_csv("insurance.csv")
data.plot(kind="scatter",x="age",y="bmi")
plt.show()
#Question 7
data=pd.read_csv("insurance.csv")
data["age"].plot(kind="hist")
plt.show()

