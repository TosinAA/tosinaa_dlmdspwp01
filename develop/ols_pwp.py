# Loading all the required libraries

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bokeh as bk
import seaborn as sns

class pwpOLS:   
    def __init__(self, dfA, dfB):
        self.dfA = dfA
        self.dfB = dfB
        
    def squared_dev(self):
               
        # Removing the x column from the dataset
        try:
            if 'x' in self.dfA.columns:
                self.dfA = self.dfA.drop(['x'], axis=1)
                
            if 'x' in self.dfB.columns:
                self.dfB = self.dfB.drop(['x'], axis=1)
            else:
                print("There is no x on this DataFrame")
                pass
        except:
            raise Exception("The inputs must be DataFrames")
        
        # Declaring the output containers
        dict_ = dict()
        min_ssd = list()

        for colA in self.dfA.columns:
            dict_[colA] = [(np.sum(np.absolute(self.dfA[colA] - self.dfB[colB])**2)) for colB in self.dfB.columns]

        for key, val in dict_.items():
            min_ssd.append({key:['y' + str(val.index(np.min(val))+1), np.min(val)]})
            
        return min_ssd
    
    def idealfour_builder(self):
        """
        This program will build the dataset of the four ideal functions.
        It will take input from dfA and dfB.
        Then it will compute the four ideal functions from the dfB.
        And the dataset can then be built.

        Argument(s): dfA, dfB

        Return(s): pandas DataFrame
        """
        
        # Declaring the output containers
        dict_ = dict()
        col_names = list()
        

        for colA in self.dfA.columns:
            dict_[colA] = [(np.sum(np.absolute(self.dfA[colA] - self.dfB[colB])**2)) for colB in self.dfB.columns]

        for val in dict_.values():
            col_names.append('y' + str(val.index(np.min(val))+1))
        
        idealfour_df = pd.DataFrame()
        idealfour_df["x"] = self.dfA["x"]
        for col in col_names:
            idealfour_df[col] = self.dfB[col]
            
        return idealfour_df



class pwpTasks():
    """
    This class will be used for the programming with python
    course final project at IU International Hoschule.
    The components based on the UML diagram provided on the project document
    are methods that can perform the following functions:
    a.  Load the datasets
    b.  Write the datasets to sql_file
    c.  Perform ols and compute the 4 ideal functions
        and build the dataframe for the 4 ideal functions.
    d.  Compute the max deviation
    """
    
    def df_loader(self, filepath, sep=','):
        """
        This method will load any dataset supported by pandas library.
        Five (5) pandas read_formats are supported.
        They are '.csv', '.txt', '.json', '.html' formats.
        The delimiter is set to ',' by default, but it can be changed as an
        additional argument incases where the delimiter is a tab "\t", " ", etc.

        Argument(s):  filepath --> the path where the file is stored. If raw path is used, 
                    must be in double quotes " ".
        
        Return(s): The dfname 
        """
        # Defining the variable inputs of the the df_loader
        self.filepath = str(filepath)

        # List of supported file formats
        pd_formats = ['.csv', '.txt', '.json', '.html']

        # Extracting the file extension from filepath
        # It returns the file part (index 0) and file extension (index 1)
        split_ext = list(os.path.splitext(self.filepath))
        
        # Selecting the correct file format that matches the file extension
        try:
            if split_ext[1] == pd_formats[0]:
                dfname = pd.read_csv(self.filepath)
                return dfname
        
            if split_ext[1] == pd_formats[1]:
                dfname = pd.read_csv(self.filepath)
                return dfname
        
            if split_ext[1] == pd_formats[2]:
                dfname = pd.read_json(self.filepath)
                return dfname
        
            if split_ext[1] == pd_formats[3]:
                with open(self.filepath, 'r') as f:
                    dfname = pd.read_html(f.read())
                return dfname
            
            else:
                 print('Format Error: Unsupported file format')
        
        except:
             raise Exception('File not found or encoding error!!!')

    def df_toSQL(self, df):