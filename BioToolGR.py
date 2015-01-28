# Made by Garam Factory

# This program is made for ease of data access on python environment.
# Users are recommended to run this program on ipython
# 
# Usage
# On ipython, %run <name of index column>

# <name of index column> refers to the first column name of the given dataset.
# Therefore, before running this program, user has to check out the first column name


import pandas as pd



class BioToolGR:
    def __init__(self):
        pass


    # This function parses a raw file from UC SANTA CRUZ("https://genome-cancer.ucsc.edu")
    # The format of files from UC SANTA CRUZ is usually text file
    # that numbers are separated by '\t' character.
    # Therefore, if you have a raw file not separted by '\t',
    # this function might not be useful.
    def parse(self,filename,index_col=None):
        if index_col == None:
            return pd.read_csv(open(filename),sep='\t')
        else:
            return pd.read_csv(open(filename),sep='\t',index_col = index_col)

    # This function drops rows whose column name is parameter "name",
    # if the value of the column is NaN.
    def dropnabycolumn(self,data,name):
        return data[data[name].notnull()]



    #------------------------------------------------------------------------------------- 


    # This is the process of what I have done the Hyun-Hwan's order.
    # 2015-1-27
    def HyunOrder(self,data):
        t = self.parse('clinical_data','sampleID')
        self.dropnabycolumn(t,'_OS_IND')
        data = data[((data['_OS_IND'] == 0) & (data['_OS'] > 1080)) | (data['_OS_IND'] == 1)]
