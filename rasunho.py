import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn as sns
import scipy.signal as sp
from scipy.interpolate import griddata

locA1ml=np.zeros((7,2))
FA1ml=np.zeros(7)
tapeteposA1ml=tapetepos.copy()

for i in range (0,tapetepos.shape[0]):
    for j in range (0,tapetepos.shape[1]):
        if tapetepos[i][j]==1:
            tapeteposA1ml[i][j]=(deltalambdaA1ml[0])*DadosVazioKs["K1"]#N
            locA1ml[0]=([i,j-1])
            FA1ml[0]=tapeteposA1ml[i][j]
            
        if tapetepos[i][j]==2:
            tapeteposA1ml[i][j]=(deltalambdaA1ml[1])*DadosVazioKs["K2"] #N
            locA1ml[1]=([i,j])
            FA1ml[1]=tapeteposA1ml[i][j]

        if tapetepos[i][j]==3:
            tapeteposA1ml[i][j]=(deltalambdaA1ml[2])*DadosVazioKs["K3"] #N
            locA1ml[2]=([i,j-1])
            FA1ml[2]=tapeteposA1ml[i][j]

        if tapetepos[i][j]==5:
            tapeteposA1ml[i][j]=((deltalambdaA1ml[3])*DadosVazioKs["K5"]) #N
            locA1ml[3]=([i,j-1])
            FA1ml[3]=tapeteposA1ml[i][j]

        if tapetepos[i][j]==6:  
            tapeteposA1ml[i][j]=((deltalambdaA1ml[4])*DadosVazioKs["K6"]) #N
            locA1ml[4]=([i,j-1])
            FA1ml[4]=tapeteposA1ml[i][j]
            
        if tapetepos[i][j]==7:
            tapeteposA1ml[i][j]=((deltalambdaA1ml[5])*DadosVazioKs["K7"]) #N
            locA1ml[5]=([i,j-1])
            FA1ml[5]=tapeteposA1ml[i][j]
            
        if tapetepos[i][j]==8:
            tapeteposA1ml[i][j]=(deltalambdaA1ml[6])*DadosVazioKs["K8"] #N
            locA1ml[6]=([i,j-1])
            FA1ml[6]=tapeteposA1ml[i][j]
            
interp_forcasA1ml= griddata(locA1ml,FA1ml,(xx,yy))


im1=plt.imshow(interp_forcasA1ml , cmap="hot")

plt.colorbar(im1)
plt.xlabel('x')
plt.ylabel('y')


deltalambdaA1ml=np.zeros(7)

deltalambdaA1ml[0]= medias[0] - BequerVaziopos1['PEAKS1']
deltalambdaA1ml[1]= medias[1] - BequerVaziopos1['PEAKS2']
deltalambdaA1ml[2]= medias[2] - BequerVaziopos1['PEAKS3']

deltalambdaA1ml[3]= medias[3] - BequerVaziopos1['PEAKS5']
deltalambdaA1ml[4]= medias[4] - BequerVaziopos1['PEAKS6']
deltalambdaA1ml[5]= medias[5] - BequerVaziopos1['PEAKS7']
deltalambdaA1ml[6]= medias[6] - BequerVaziopos1['PEAKS8']

BequerVaziopos1=pd.read_csv(open("Teste1/Béquer 1000mL/N0.2023.05.11.16.18.56(pos4).txt","r"),skiprows=65,names=["Timestamp","CH1","CH2","CH3","CH4","CH5","CH6","CH7","CH8","PEAKS1","PEAKS2","PEAKS3","PEAKS5","PEAKS6","PEAKS7","PEAKS8"], sep="\t", decimal=",")
BequerVaziopos1=pd.read_csv(open("Teste1/Béquer 1000mL/N0.2023.05.11.16.19.37(pos4).txt","r"),skiprows=65,names=["Timestamp","CH1","CH2","CH3","CH4","CH5","CH6","CH7","CH8","PEAKS1","PEAKS2","PEAKS3","PEAKS5","PEAKS6","PEAKS7","PEAKS8"], sep="\t", decimal=",")
BequerVaziopos1=pd.read_csv(open("Teste1/Béquer 1000mL/N0.2023.05.11.16.20.06(pos4).txt","r"),skiprows=65,names=["Timestamp","CH1","CH2","CH3","CH4","CH5","CH6","CH7","CH8","PEAKS1","PEAKS2","PEAKS3","PEAKS5","PEAKS6","PEAKS7","PEAKS8"], sep="\t", decimal=",")


FBpoS2ML= np.zeros([len(BequerVaziopos1),8])  
FBpoS2ML=pd.DataFrame(FBpoS2ML,columns=["FORCE1",'FORCE2','FORCE3','FORCE4','FORCE5','FORCE6','FORCE7','FORCE8'])
for i in range (0,len(BequerVaziopos1)):
    FBpoS2ML['PEAKS1']=(BequerVaziopos1['PEAKS1'][i] - medias[0])*DadosVazioKs['K1']
    FBpoS2ML['PEAKS2']=(BequerVaziopos1['PEAKS2'][i] - medias[1])*DadosVazioKs['K2']
    FBpoS2ML['PEAKS3']=(BequerVaziopos1['PEAKS3'][i] - medias[2])*DadosVazioKs['K3']
    # FBpoS2ML['PEAKS4']=BequerVaziopos1['PEAKS4'][i] #CASO ADICONE MAIS UM SENSOR ADICIONE O VALOR PADRÂO DELE EM MEDIAS    
    FBpoS2ML['PEAKS5']=(BequerVaziopos1['PEAKS5'][i] - medias[3])*DadosVazioKs['K5']
    FBpoS2ML['PEAKS6']=(BequerVaziopos1['PEAKS6'][i] - medias[4])*DadosVazioKs['K6']
    FBpoS2ML['PEAKS7']=(BequerVaziopos1['PEAKS7'][i] - medias[5])*DadosVazioKs['K7']
    FBpoS2ML['PEAKS8']=(BequerVaziopos1['PEAKS8'][i] - medias[6])*DadosVazioKs['K8']
    
FBpoS2ML.to_csv('Teste1/DADOS BRUTOS DE FORÇA/FBpoS2ML.csv')