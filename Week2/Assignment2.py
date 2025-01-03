import numpy as np
A1=np.array([11,33,22,44,66,55])
A2=np.array([10,30,20,40,60,50])
print("Given Arrays are:")
print("A1=",A1)
print("A2=",A2)
#Question 1
res=A1[2:6]
print("Elements in A1 from 2 to 5 is:",res)
#Question 2
res=A1.reshape(3,2)
print("After reshaping the array A1 into(3,2):")
print(res)
#Question 3
res=np.concatenate((A1,A2))
print("By joining A1 and A2 we get:",res)
#Question 4
res=np.split(A1,3)
print("By Spliting the arrays into 3 parts we get:")
for i in res:
    print(i)
#Question 5
res=np.where(A1==44)
print("The value 44 in A1 is at indices:",res[0])
#Question 6
res=np.where(A1%2==0)
print("Even numbers in A1 are :")
for i in res[0]:
    print(A1[i],end=" ")
print()
#Question 7
A1.sort()
print("After Sorting the Array A1:",A1)
#Question 8
res=A1[A1%2!=0]
print("The Odd numbers in array A1 are:",res) 

