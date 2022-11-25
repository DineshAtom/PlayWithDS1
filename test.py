import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('Data\people-100.csv',parse_dates=['First Name'])
print(sales)
salesInfo = sales.info
# print("Info is :" + salesInfo)
saleShape = sales.shape
print("Shape is") 
# print(sales.info) 


