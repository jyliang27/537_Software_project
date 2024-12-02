import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def LoadData(filename:str):
    if ".csv" in filename:
        dataframe=pd.read_excel(str(filename))
    if ".xlsx" in filename:
        dataframe=pd.read_excel(str(filename)) 
    else:
        return print("File in wrong format") 
    return dataframe

def PrepData(dataframe:str,concentration:str,lnConc:str) :
    tempdf=dataframe.copy()
    ln_list=[]
    for i in dataframe.index:
        if dataframe[concentration][i]!=np.nan:
            ln_list.append(np.log(dataframe[concentration][i]))
        else:
            ln_list.append(np.nan)
    tempdf[lnConc]=ln_list
    tempdf.dropna(subset=[lnConc],inplace=True)
    return tempdf

def findCmax(dataframe:str,time:str, concentration:str)->float:
    for i in dataframe.index:
        if dataframe[concentration][i]==np.nanmax(dataframe[concentration]):
            if i==0:
                Cmax=dataframe[concentration][i]
                max_idx=i
                Tmax=dataframe[time][max_idx]
                return Cmax, Tmax
            elif dataframe[concentration][i]!=dataframe[concentration][i-1]:
                Cmax=dataframe[concentration][i]
                max_idx=i
                Tmax=dataframe[time][max_idx]
    print("Cmax=",Cmax)
    print("Tmax=",Tmax)
    return Cmax, Tmax

def findT_half(dataframe, time, concentration, percent_threshold)->float:
    t_half="Not Assigned, consider adjusting threshold"
    for i in dataframe.index:
        if dataframe[concentration][i]==np.nanmax(dataframe[concentration]):
            if i==0:
                max_idx=i
            elif dataframe[concentration][i]!=dataframe[concentration][i-1]:
                max_idx=i
        for j in dataframe.index:
            if i > max_idx and j>i:
                thresh=dataframe[concentration][j]*(percent_threshold/100)
                if dataframe[concentration][i]/2 >= dataframe[concentration][j]-thresh and dataframe[concentration][i]/2 <= dataframe[concentration][j]+thresh:
                    t_half=dataframe[time][j]-dataframe[time][i]
                    break
    return t_half

def findCo(dataframe:str,time:str,lnConc:str) -> float:
    """
    This function takes in a dataframe with a column for time and a column with ln(drug concentration)
    and returns the elimination constant k, which is equivalent to -1 * the coefficient (or slope);
    and the drug concentration at t=0, which is equivalent to the y intercept.
    
    This function currently assumes data is linear.
    
    dataframe: the name of the dataframe
    time: the name of time column
    lnConc: the name of the column with ln(drug concentration)
    """
    x = []
    y = []
    model = LinearRegression()
    for i in dataframe.index:
        tempvalue = dataframe[time][i]
        templist = []
        templist.append(tempvalue)
        x.append(templist)
        tempvalue2 = dataframe[lnConc][i]
        templist2 = []
        templist2.append(tempvalue2)
        y.append(templist2)
    model.fit(x,y)
    lnCo = float(model.intercept_)
    Co = np.exp(lnCo)
    k = float(-1*model.coef_)
    return Co,k

def findPK(dataframe:str,time:str, concentration:str,lnConc:str, percent_threshold:float)->float:
    result1 = findCo(dataframe, time, lnConc)
    result2 = findCmax(dataframe,time, concentration)
    result3 = findT_half(dataframe, time, concentration, percent_threshold)
    k = result1[1]
    Co = result1[0]
    Cmax = result2[0]
    Tmax = result2[1]
    t_half = result3

    return Co,k,Cmax,Tmax,t_half