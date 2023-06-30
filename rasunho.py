import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn as sns
import scipy.signal as sp
from scipy.interpolate import griddata

locC4=np.zeros((7,2))
FC4=np.zeros(7)
tapeteposC4=tapetepos.copy()

for i in range (0,tapetepos.shape[0]):
    for j in range (0,tapetepos.shape[1]):
        if tapetepos[i][j]==1:
            tapeteposC4[i][j]=(deltalambdaC4[0])*DadosVazioKs["K1"]#N
            locC4[0]=([i,j-1])
            FC4[0]=tapeteposC4[i][j]
            
        if tapetepos[i][j]==2:
            tapeteposC4[i][j]=(deltalambdaC4[1])*DadosVazioKs["K2"] #N
            locC4[1]=([i,j])
            FC4[1]=tapeteposC4[i][j]

        if tapetepos[i][j]==3:
            tapeteposC4[i][j]=(deltalambdaC4[2])*DadosVazioKs["K3"] #N
            locC4[2]=([i,j-1])
            FC4[2]=tapeteposC4[i][j]

        if tapetepos[i][j]==5:
            tapeteposC4[i][j]=((deltalambdaC4[3])*DadosVazioKs["K5"]) #N
            locC4[3]=([i,j-1])
            FC4[3]=tapeteposC4[i][j]

        if tapetepos[i][j]==6:  
            tapeteposC4[i][j]=((deltalambdaC4[4])*DadosVazioKs["K6"]) #N
            locC4[4]=([i,j-1])
            FC4[4]=tapeteposC4[i][j]
            
        if tapetepos[i][j]==7:
            tapeteposC4[i][j]=((deltalambdaC4[5])*DadosVazioKs["K7"]) #N
            locC4[5]=([i,j-1])
            FC4[5]=tapeteposC4[i][j]
            
        if tapetepos[i][j]==8:
            tapeteposC4[i][j]=(deltalambdaC4[6])*DadosVazioKs["K8"] #N
            locC4[6]=([i,j-1])
            FC4[6]=tapeteposC4[i][j]
            
interp_forcasC4= griddata(locC4,FC4,(xx,yy))


im1=plt.imshow(interp_forcasC4 , cmap="hot")

plt.colorbar(im1)
plt.xlabel('x')
plt.ylabel('y')