import pandas as pd
import numpy as np

pfile1 = pd.read_csv('file_1.csv')
print(pfile1.shape)
print(type(pfile1.iloc[0,0]))

sample_arr = np.asarray(pfile1.iloc[0,:])
print(type(sample_arr))
print(sample_arr.shape)
print (sample_arr[0])

rawdata = np.asarray(pfile1)
