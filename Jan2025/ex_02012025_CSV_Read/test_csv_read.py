import csv
import pandas as pd

class Test_READ():

    def test_read_pandas(self):
        df = pd.read_csv('userdata.csv')
        print(df)
