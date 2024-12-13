# Install package and any necessary dependencies. Import modules.
!pip install ModelPK
from ModelPK import simulatePK as sim
from ModelPK import extractPKparam as extract

#Please ensure the file "Test_PK.xlsx has been downloaded into your working directory."
#Load data into dataframe, remove null values, log transform data.
testdf=extract.LoadData("Test_PK.xlsx")
testdf2=extract.PrepData(testdf,"IV Concentration", "LnConc")
testdf2

#Extract PK parameters from experimental data.
params=extract.findPK(testdf2,"Time","IV Concentration","LnConc",10)
params

#Find the time it takes for a starting concentration of 100 (units not specified) to a subtherapeutic concentration of 3 (units not specified).
simresult=sim.findSubtherapeuticTime(params,10,3,numsteps=100, setCo=100)
simresult