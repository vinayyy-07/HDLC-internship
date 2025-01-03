import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#Question 1
data=pd.read_csv("windpower.csv")
#Question 2
print(data.head(10).to_string())
#Question 3
print(data.tail(5).to_string())
#Question 4
print(data.info())
#Question 5
mean=data["Wind Speed (m/s)"].mean()
print("mean of wind power is:",mean)
std=data["Wind Speed (m/s)"].std()
print("standard deviation of wind power is:",std)
mi=data["Wind Speed (m/s)"].min()
print("mininum of wind power is:",mi)
ma=data["Wind Speed (m/s)"].max()
print("maximum of wind power is:",ma)
#Question 6
#Null values exit only in windspeed column therefore
data["Wind Speed (m/s)"].fillna(data["Wind Speed (m/s)"].mean(),inplace=True)
print(data.info())
#Question 7
data["Wind Speed (m/s)"].plot(kind="hist")
plt.show()
#Question 8
data.plot(x="Wind Speed (m/s)",y="Theoretical_Power_Curve (KWh)",kind="scatter")
plt.show()
#Question 9
print(data[data["Wind Speed (m/s)"]<5].to_string())
#Question 10
data1=data[data["Wind Direction (°)"]>200]
print(data1.to_string())
