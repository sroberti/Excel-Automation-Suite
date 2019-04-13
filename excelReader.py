
import os
import pandas as pd

def excel(filename):
    return pd.read_excel(os.path.join(os.path.curdir,filename))
