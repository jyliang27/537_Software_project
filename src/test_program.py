import unittest
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from program import LoadData
from program import PrepData
from program import findCmax
from program import findCo
from program import findT_half
from program import findPK

testdf=LoadData("Test_PK.xlsx")
testdf2=PrepData(testdf,"IV Concentration","LnConc")

class TestModelPK(unittest.TestCase):
    print("test1 is running")
    def test_LoadData(self):
        result=LoadData('Test_PK.xlsx')
        self.assertIsInstance(result,pd.DataFrame)
    def test_badLoadData(self):
        print("test is running")
        result=LoadData("Functional Specification.docx")
        self.assertIsInstance(result,pd.DataFrame)
    

    def test_PrepData(self):
        result=PrepData(testdf,"IV Concentration","LnConc")
        self.assertNotIn(np.nan,result)
        self.assertIsInstance(result,pd.DataFrame)
    

    def test_findT_half(self):
        result=findT_half(testdf2,"Time","IV Concentration",10)
        #self.assertNotIn(np.nan,PrepData(result),"No nulls")

    def test_findCmax(self):
        result=findCmax(testdf2,"Time","IV Concentration")
        self.assertEquals(result[0],np.nanmax(testdf2["IV Concentration"]))
        self.assertEquals(len(result),2)

    def test_findCo(self):
        result=findCo(testdf2,"Time","LnConc")
        #self.assertNotIn(np.nan,PrepData(result),"No nulls")
        self.assertEquals(len(result),2)

    def test_findPK(self):
        result=findPK(testdf2,"Time","IV Concentration","LnConc",10)
        self.assertIsInstance(result,tuple)     
        self.assertEquals(len(result),5)
    
        if __name__ == '__main__':
            unittest.main()