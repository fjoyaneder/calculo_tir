#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:image.png)

# In[2]:


import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# In[3]:


out_file = 'LOA_20200508_TIR.txt'


# In[4]:


#Meses indica la cantidad de 0 que se deben agregar
#Cuotas indica las cuotas que se aplazaron
headers = ['LLAVE_NOROPE','LLAVE','MESES','CAPITAL_MESES_CUOTAS']


# In[5]:


#data = pd.read_csv('LOA_PESOS_CEROS.txt',sep = "|", header=None, names = headers, nrows=10)
data = pd.read_csv('LOA_20200508.txt',sep = "|", header=None, names = headers, skiprows=1)


# In[6]:


data.head()


# In[7]:


def irrCalc(array):
    #array = [array]
    irr = round(np.irr(array)*100, 5)
    return irr


# In[8]:


data['CAPITAL_MESES_CUOTAS'] = data['CAPITAL_MESES_CUOTAS'].str.strip()
    
df = pd.DataFrame(columns=['LLAVE_NOROPE','LLAVE','TIR'])

for index, row in data.iterrows():
    float_vals = [float(x) for x in  row['CAPITAL_MESES_CUOTAS'].split(",")]
    tir = irrCalc(float_vals)
    #tirAnual = (pow((1+tir),12)-1)*100
    #tirAnual2 = (np.power((1+tir),12)-1)*100
    #tirAnual3 = (((1+tir)**12)-1)*100
    #print(float_vals, tir, type(tir), tirAnual, tirAnual2, tirAnual3)
    
    df = df.append({'LLAVE_NOROPE': row['LLAVE_NOROPE'], 'LLAVE': row['LLAVE'], 'TIR': irrCalc(float_vals)}, ignore_index=True)
    #print(row['LLAVE_NOROPE'], row['LLAVE'], row['CAPITAL_MESES_CUOTAS'], irrCalc(float_vals))
    
df.head()


# In[9]:


df.to_csv(out_file, encoding='latin1', sep=';', index=False, decimal='.')


# In[ ]:




