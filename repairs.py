import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px
from datetime import datetime



repairs=pd.read_csv('device_repairs.csv')
print(repairs.columns)
df=DataFrame(repairs)
#print(df)

#extract fbruary certain day
#2/2/2020
f1=df[df.timestamp_utc=='1/2/2020']
print(f1)
f2=df[df.timestamp_utc=='2/2/2020']
print(f2)
f5=df[df.timestamp_utc=='5/2/2020']
print(f5)
f6=df[df.timestamp_utc=='6/2/2020']
print(f6)
f4=df[df.timestamp_utc=='4/2/2020']
print(f4)
f3=df[df.timestamp_utc=='3/2/2020']
print(f3)
f7=df[df.timestamp_utc=='7/2/2020']
print(f7)
f8=df[df.timestamp_utc=='8/2/2020']
print(f8)
f9=df[df.timestamp_utc=='9/2/2020']
print(f9)
f10=df[df.timestamp_utc=='10/2/2020']
print(f10)
f11=df[df.timestamp_utc=='11/2/2020']
print(f11)
f12=df[df.timestamp_utc=='12/2/2020']
print(f12)
f13=df[df.timestamp_utc=='13/2/2020']
print(f13)
f14=df[df.timestamp_utc=='14/2/2020']
print(f14)
f15=df[df.timestamp_utc=='15/2/2020']
print(f15)
f16=df[df.timestamp_utc=='16/2/2020']
print(f16)
f17=df[df.timestamp_utc=='17/2/2020']
print(f17)
f18=df[df.timestamp_utc=='18/2/2020']
print(f18)
f19=df[df.timestamp_utc=='19/2/2020']
print(f19)
f20=df[df.timestamp_utc=='20/2/2020']
print(f20)
f21=df[df.timestamp_utc=='21/2/2020']
print(f21)
f22=df[df.timestamp_utc=='22/2/2020']
print(f22)
f23=df[df.timestamp_utc=='23/2/2020']
print(f23)
f24=df[df.timestamp_utc=='24/2/2020']
print(f24)
f25=df[df.timestamp_utc=='25/2/2020']
print(f25)
f26=df[df.timestamp_utc=='26/2/2020']
print(f26)
f27=df[df.timestamp_utc=='27/2/2020']
print(f27)
f28=df[df.timestamp_utc=='28/2/2020']
print(f28)
f29=df[df.timestamp_utc=='29/2/2020']
print(f29)








#eda
#corr
#multilinear regression
#vis
 


 



#use py to analyse whatever and make graphs 
#analyze whatever 
#plotly or sns

#it is the last phse of ex which is best create etc. 
#may be us etableau 























