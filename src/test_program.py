import unittest
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from program import LoadData
from program import PrepData
from program import findPK

class TestPK(unittest.TestCase):
    print("test1 is running")
    def test_LoadData(self):
        result=LoadData('Test_PK.xlsx')
        self.assertIsInstance(result,pd.DataFrame)
    def test_badLoadData(self):
        print("test is running")
        result=LoadData("Functional Specification.docx")
        self.assertIsInstance(result,pd.DataFrame)
    
    #def test_PrepData(self):
        #result=LoadData('Test_PK.xlsx')
     #   self.assertNotIn(np.nan,PrepData(result),"No nulls")


        if __name__ == '__main__':
            unittest.main()