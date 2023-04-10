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
        
        # Declaring the output containers
        dict_ = dict()
        min_ssd = list()
        col_names = list()

        for colA in self.dfA.columns[1:]:
            dict_[colA] = [(np.sum(np.absolute(self.dfA[colA] - self.dfB[colB])**2)) for colB in self.dfB.columns[1:]]

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
        
        for colA in self.dfA.columns[1:]:
            dict_[colA] = [(np.sum(np.absolute(self.dfA[colA] - self.dfB[colB])**2)) for colB in self.dfB.columns[1:]]

        #Creating the column names
        for key, val in dict_.items():
            col_names.append('y' + str(val.index(np.min(val))+1))
        
        # Creating the dataframe for the idealfour dataset
        idealfour_df = pd.DataFrame(self.dfB[["x"]])
        
        for col in col_names:
            idealfour_df[col] = self.dfB[col]
          
        return idealfour_df


class pwpDeviation(pwpOLS):
    """
    This class will hold the common variables that will be used as variables in
    create the squared_dev method (method to compute sum of squared deviations)
    and max_dev method (method to compute the max deviation and return a value).
    """
    
    def max_dev(self):
        """
        This class will compute the max deviations from the two DataFrame inputs.
        
        Argument(s): dfA, dfB
        
        Return(s): max_deviation
        """
        # Inheriting the two DataFrame inputs from the pwpOLS class.
        super().__init__(self.dfA, self.dfB)
        
        
        # Computing the max_dev
        
        # Collecting the max deviation for each y-df values over the numerous y-dfB values
        dict_ = dict()
        
        for colA in self.dfA.columns[1:]:
            dict_[colA] = [(np.max(np.absolute(self.dfA[colA] - self.dfB[colB]))) for colB in self.dfB.columns[1:]]
        
        # Building the column names and the max deviation
        dfB_cols = [colB for colB in self.dfB.columns[1:]]
        max_deviation = [[dfB_cols[value.index(np.max(value))], np.max(value)] for key, value in dict_.items()]

        return max_deviation


class pwpTasks():
    """
    This class will be used to perform some of the additional task of the 
    programming with python course final project at IU International Hoschule.
    It will have the df_loader method that will be used for loading the dataset.
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
        self.filepath = filepath

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
             raise Exception('File not found or encoding error!!!')        # Defining the variable inputs of the the df_loader
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