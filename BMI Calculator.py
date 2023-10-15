#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator
# 

# In[1]:


name = input("Enter your name: ")
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

BMI = (weight)/(height * height)

print(BMI)

if BMI>0:
    if(BMI<18.5):
        print(name +", you are underweight.")
    elif(BMI<=24.9):
        print(name +", you are normal weight.")
    elif(BMI<29.9):
        print(name +", you are overweight.")
    elif(BMI<34.9):
        print(name +", you are obsese.")
    elif(BMI<39.9):
        print(name +", you are severly obesed.")
    else:
        print(name +", you are morbidly obssed.")
        
else:
    print("enter the valid input.")


# In[ ]:




