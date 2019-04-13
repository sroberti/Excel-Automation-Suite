import os
import numpy as np
import pandas as pd

#loading metadata
#csv, excel file
#without loading entire thing into memory,


class Query:
    EQ="=="
    GT=">"
    GE=">="
    LT="<"
    LE="<="
    IN="is in"
    NI="not in"
    NE="!="
    #constructor
    #df == Pandas DataField object
    def __init__(self, df):
        self.setDF(df)
    #set DataField object that is being looked at
    def setDF(self, df):
        self.df=df
    #query functions for getting rows whose column value colName is
        #related to value by the given operation
    def rowsWithColumnEqualTo(self, colName, value):
        yield self.df.loc[self.df[colName] == value]
    def rowsWithColumnNotEqualTo(self, colName, value):
        yield self.df.loc[self.df[colName] != value]
    def rowsWithColumnLessThan(self, colName, value):
        yield self.df.loc[self.df[colName] < value]
    def rowsWithColumnLessThanOrEqualTo(self, colName, value):
        yield self.df.loc[self.df[colName] <= value]
    def rowsWithColumnGreaterThan(self, colName, value):
        yield self.df.loc[self.df[colName] > value]
    def rowsWithColumnGreaterThanOrEqualTo(self, colName, value):
        yield self.df.loc[self.df[colName] >= value]
    def rowsWithColumnIn(self, colName, value):
        yield self.df.loc[self.df[colName].isin(value)]
    def rowsWithColumnNotIn(self, colName, value):
        yield self.df.loc[~self.df[colName].isin(value)]
    #generate all the rows that satisfy the requirements
        #yield rows for which data in column colName (op) value
    def rows(self, colName, op, value):
        if op==Query.EQ: #is the data == value?
            yield self.df.loc[self.df[colName] == value]
        elif op==Query.NE: #is the data != value?
            yield self.df.loc[self.df[colName] != value]
        elif op==Query.GT: #is the data > value?
            yield self.df.loc[self.df[colName] > value]
        elif op==Query.GE: #is the data >= value?
            yield self.df.loc[self.df[colName] >= value]
        elif op==Query.LT: #is the data < value?
            yield self.df.loc[self.df[colName] < value]
        elif op==Query.LE: #is the data <= value?
            yield self.df.loc[self.df[colName] <= value]
        elif op==Query.IN: #is the data contained in the iterable value?
            yield self.df.loc[self.df[colName].isin(value)]
        elif op==Query.NI: #is the data NOT contained in the iterable value?
            yield self.df.loc[~self.df[colName].isin(value)]


#2.76992
            
#filename=input("filename is : ")
#df=pd.read_excel(os.path.join(os.path.curdir,filename))

#Example use        
#query=Query(df)
#for row in query.rows("RCap_DChg(mAh/g)", "==", 2.76992):
#    print("row: ",row)
#for row in query.rows("Voltage", ">", 2.85):
#    print("row: ",row)
#for row in query.rows("Voltage", "<=", 2.45):
#    print("row: ",row)
'''for row in query.rows("colname", "is in", [2.44553,2.88918,2.73451,]):
    df.copy(row)
query.setDF(newDF)
for row in query.rows("colname", ">", 2.5):
    df.copy(row)'''


