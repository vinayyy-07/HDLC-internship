

Question 1
"""

import pandas as pd
import numpy as nu
d={"c1":[10,20,30],"c2":[40,50,60],"c3":[70,80,90],"c4":[100,110,120]}
Table=pd.DataFrame(data=d)
print(Table)
print("No of Rows:",Table.shape[0])
print("No of columns:",Table.shape[1])

"""Question 2"""

Table2=pd.read_csv("data.csv")
print("The Given data is:")
print(Table2)
print("The first 5 rows data is:")
print(Table2.head(5))
Table2.dropna(axis=0,inplace=True)
print("After removing null& error values:")
print(Table2)
print("From given data the Final Analysis is given by:")
print(Table2.describe())