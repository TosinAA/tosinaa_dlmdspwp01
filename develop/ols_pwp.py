# Loading all the required libraries

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bokeh as bk
import seaborn as sns



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