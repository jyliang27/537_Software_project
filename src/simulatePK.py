import numpy as np
import pandas as pd
import tellurium as te

MODEL1="1 compartment, IV"

model_1C='''
#equation for 1 compartment model (IV, mostly distributed in blood):
Ct' = -k*Ct

Ct=5.96
e=exp(1)
k=.005
'''

modellib={MODEL1:model_1C}

def findSubtherapeuticTail(findPKresult:str, subther_threshold:float,  subther_target:float, numiterations: float=1000, starttime:float=0, simruntime:float=100, setCo:float="default", model:str=MODEL1):
    """
    Takes in extracted PK parameters, Antimony model, model parameters, and values for target subtherapeutic concentration and threshold. Simulates model and returns the first timepoint at which subtherapeutic concentration is reached.
    Allows users to find i) time to subtherpeutic tail based on experimental data and ii) time to subtherpeutic tail with varying Co (here, a proxy for drug dose administered via IV bolus)

    Inputs:
    findPKresult: variable assigned to findPK results, input as a string
    subther_threshold: a percent (sign not needed) representing percent. Ex: a value of 10 should be interpreted as within 10% of target subtherapeutic concentration value
    numiterations: max number of iterations allowed for function to find the time to subtherapeutic tail
    subther_target: subtherapeutic concentration of drug
    starttime: Simulation start time
    simruntime: Simulation run time
    setCo: if "default", Co is calculated from experimental data. Otherwise, Co is any initial drug concentration in the body.
    model: Key from modellib entered as string.

    Output:
    A plot of the simulated change in drug concentration over time with the chosen Co
    A float representing the time (units consistent with experimental data) it takes for drug concentrations to reach subtherapeutic levels.
    """
    try:
        modeltoload = modellib[model]
    except KeyError:
        raise ValueError(f"Model '{model}' not found in modellib.")    
    r=te.loada(modeltoload)
    r.reset()
    result=findPKresult
    r['k']=result[1]
    if setCo=="default":
        r['Ct']=result[0]
    else:
        r['Ct']=setCo
    storeCt=r['Ct']
    data=r.simulate(starttime,simruntime)
    breakstatement=0
    for iteration in range(1,numiterations):
        if breakstatement==1:
            break
        else:
            for i in range(0,len(data)):
                conc=data[i,1]
                thresh=subther_target*(subther_threshold/100)
                simtime=data[i,0]
                if i==len(data)-1 and conc>subther_target:
                    r.reset()
                    r['Ct']=storeCt
                    data=r.simulate(0,simtime*1.5)
                    #print("Extended simulation time")
                    break
                if conc<subther_target:
                    #print("Not enough steps, simulation time too long")
                    r.reset()
                    r['Ct']=storeCt
                    data=r.simulate(0,simtime/2)
                    break
                if subther_target-thresh<=conc<=subther_target+thresh:
                    #print("Found time to subtherapeutic tail")
                    subthertime=data[i,0]
                    breakstatement=1
                    r.plot(data, True, "Time","Drug Concentration")
                    #print("breakstatement changed",breakstatement)
                    break
    return subthertime