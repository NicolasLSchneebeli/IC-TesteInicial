import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn as sns
import scipy.signal as sp
from scipy.interpolate import griddata

locD4=np.zeros((7,2))
FD4=np.zeros(7)
tapeteposD4=tapetepos.copy()

for i in range (0,tapetepos.shape[0]):
    for j in range (0,tapetepos.shape[1]):
        if tapetepos[i][j]==1:
            tapeteposD4[i][j]=(deltalambdaD4[0])*DadosVazioKs["K1"]#N
            locD4[0]=([i,j-1])
            FD4[0]=tapeteposD4[i][j]
            
        if tapetepos[i][j]==2:
            tapeteposD4[i][j]=(deltalambdaD4[1])*DadosVazioKs["K2"] #N
            locD4[1]=([i,j])
            FD4[1]=tapeteposD4[i][j]

        if tapetepos[i][j]==3:
            tapeteposD4[i][j]=(deltalambdaD4[2])*DadosVazioKs["K3"] #N
            locD4[2]=([i,j-1])
            FD4[2]=tapeteposD4[i][j]

        if tapetepos[i][j]==5:
            tapeteposD4[i][j]=((deltalambdaD4[3])*DadosVazioKs["K5"]) #N
            locD4[3]=([i,j-1])
            FD4[3]=tapeteposD4[i][j]

        if tapetepos[i][j]==6:  
            tapeteposD4[i][j]=((deltalambdaD4[4])*DadosVazioKs["K6"]) #N
            locD4[4]=([i,j-1])
            FD4[4]=tapeteposD4[i][j]
            
        if tapetepos[i][j]==7:
            tapeteposD4[i][j]=((deltalambdaD4[5])*DadosVazioKs["K7"]) #N
            locD4[5]=([i,j-1])
            FD4[5]=tapeteposD4[i][j]
            
        if tapetepos[i][j]==8:
            tapeteposD4[i][j]=(deltalambdaD4[6])*DadosVazioKs["K8"] #N
            locD4[6]=([i,j-1])
            FD4[6]=tapeteposD4[i][j]
            
interp_forcasD4= griddata(locD4,FD4,(xx,yy))


im1=plt.imshow(interp_forcasD4 , cmap="hot")

plt.colorbar(im1)
plt.xlabel('x')
plt.ylabel('y')


deltalambdaD4=np.zeros(7)

deltalambdaD4[0]= medias[0] - Bequer1000pos3['PEAKS1'].mean()
deltalambdaD4[1]= medias[1] - Bequer1000pos3['PEAKS2'].mean()
deltalambdaD4[2]= medias[2] - Bequer1000pos3['PEAKS3'].mean()

deltalambdaD4[3]= medias[3] - Bequer1000pos3['PEAKS5'].mean()
deltalambdaD4[4]= medias[4] - Bequer1000pos3['PEAKS6'].mean()
deltalambdaD4[5]= medias[5] - Bequer1000pos3['PEAKS7'].mean()
deltalambdaD4[6]= medias[6] - Bequer1000pos3['PEAKS8'].mean()

Bequer1000pos3=pd.read_csv(open("Teste1/Béquer 1000mL/N0.2023.05.11.16.18.56(pos3).txt","r"),skiprows=65,names=["Timestamp","CH1","CH2","CH3","CH4","CH5","CH6","CH7","CH8","PEAKS1","PEAKS2","PEAKS3","PEAKS5","PEAKS6","PEAKS7","PEAKS8"], sep="\t", decimal=",")
Bequer1000pos3=pd.read_csv(open("Teste1/Béquer 1000mL/N0.2023.05.11.16.19.37(pos3).txt","r"),skiprows=65,names=["Timestamp","CH1","CH2","CH3","CH4","CH5","CH6","CH7","CH8","PEAKS1","PEAKS2","PEAKS3","PEAKS5","PEAKS6","PEAKS7","PEAKS8"], sep="\t", decimal=",")
Bequer1000pos3=pd.read_csv(open("Teste1/Béquer 1000mL/N0.2023.05.11.16.20.06(Pos3).txt","r"),skiprows=65,names=["Timestamp","CH1","CH2","CH3","CH4","CH5","CH6","CH7","CH8","PEAKS1","PEAKS2","PEAKS3","PEAKS5","PEAKS6","PEAKS7","PEAKS8"], sep="\t", decimal=",")
Bequer1000pos4