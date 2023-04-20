# Loading all the required libraries

import os
import numpy as np
import pandas as pd

# Creating the pwpOLS class

class pwpOLS:   
    """
    This class contains the squared_dev() and idealfour_builder() methods.
    Both methods work based on the sum of squared deviation method from the
    ordinary least squares method.
    idealfour_builder builds a dataset based on the findings of the squared_dev()
    and returns a pandas DataFrame.
    """
    
    def __init__(self, dfA, dfB):
        self.dfA = dfA
        self.dfB = dfB
        
    def squared_dev(self):
        """
        This method computes the sum of squared deviation using the train and ideal
        datasets as the inputs.

        Argument(s): dfA, dfB

        Returns: list of dictionaries object
        """
        # Declaring the output containers
        dict_ = dict()
        min_ssd = list()
        col_names = list()

        try:
            for colA in self.dfA.columns[1:]:
                dict_[colA] = [(np.sum(np.absolute(self.dfA[colA] - self.dfB[colB])**2)) for colB in self.dfB.columns[1:]]

            for key, val in dict_.items():
                min_ssd.append({key:['y' + str(val.index(np.min(val))+1), np.min(val)]})
                
            return min_ssd
        except:
            raise TypeError
    
    def idealfour_builder(self):
        """
        This program will build the dataset of the four ideal functions.
        It will take input from dfA and dfB.
        And use it to build the resulting dataset.

        Argument(s): dfA, dfB

        Return(s): pandas DataFrame
        """
        try:
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
        except:
            raise TypeError


class pwpDeviation(pwpOLS):
    """
    This class is designed to have the max_dev() method used for computing the
    deviation or errors between two different datasets containing historical data
    and prediction data. We can call the two datasets dfA and dfB.
    """
    
    def max_dev(self):
        """
        This class will compute the max deviations from the two DataFrame inputs.
        
        Argument(s): dfA, dfB
        
        Return(s): max_deviation (list object)
        """
        # Inheriting the two DataFrame inputs from the pwpOLS class.
        super().__init__(self.dfA, self.dfB)
        
        try:
            # Collecting the max deviation for each y-df values over the numerous y-dfB values
            dict_ = dict()
            
            for colA in self.dfA.columns[1:]:
                dict_[colA] = [(np.max(np.absolute(self.dfA[colA] - self.dfB[colB]))) for colB in self.dfB.columns[1:]]
            
            # Building the column names and the max deviation
            dfB_cols = [colB for colB in self.dfB.columns[1:]]
            max_deviation = [[dfB_cols[value.index(np.max(value))], np.max(value)] for key, value in dict_.items()]

            return max_deviation
        except:
            raise TypeError
            print("You must input pandas DataFrame objects!!!")

class pwpEvaluate():
    """
    This class will have the model evaluation module comprising:
    1.  r-squared method for checking accuracy
    2.  Root Mean Square Error (RMSE) method
    3.  Mean Square Error (MSE) method
    4.  Mean Absolute Error (MAE) method
    5.  logcosh loss method.
    """

    def r_sqr(self, df1, df2):
        
        """
        This method will compute the r-squared of two input features/fields.

        Argument(s): df1, df2

        Return(s): r_2
        """
        # Declaring the arguments
        self.df1 = df1
        self.df2 = df2

        # Declaring the mean of the real observations
        mean_df1 = np.mean(self.df1)

        # Computing the deviations of the each real observations and predictions
        # from the mean of the real observations
        df1_sum_squares = np.sum((self.df1 - mean_df1)**2)
        df2_sum_squares = np.sum((self.df2 - mean_df1)**2)

        # Finalizing the r-squared calculations
        r_2 = round(df2_sum_squares / df1_sum_squares, 2)
    
        return r_2

    def rmse(self, df1, df2):
        """
        This method will compute the r-squared of two input features/fields.

        Argument(s): df1, df2

        Return(s): rmse
        """
        # Declaring the arguments
        self.df1 = df1
        self.df2 = df2

        # Computing the square of residuals
        sum_residual_sqr = np.sum((self.df2 - self.df1)**2)

        # Finalizing the rmse calculations
        rmse = round(np.sqrt(sum_residual_sqr / len(self.df1)), 2)
    
        return rmse
    
    def mse(self, df1, df2):
        """
        This method will compute the r-squared of two input features/fields.

        Argument(s): df1, df2

        Return(s): mse
        """
        # Declaring the arguments
        self.df1 = df1
        self.df2 = df2

        # Computing the square of residuals
        res_sqr = np.sum((self.df2 - self.df1)**2)

        # Finalizing the rmse calculations
        mse = round(res_sqr / len(self.df1), 2)
    
        return mse
    

    def mae(self, df1, df2):
        """
        This method will compute the mean absolute error of two input features/fields.

        Argument(s): df1, df2

        Return(s): mae
        """

        # Declaring the arguments
        self.df1 = df1
        self.df2 = df2

        # Computing the square of residuals
        abs_res_sqr = np.sum(np.absolute(self.df1 - self.df2))

        # Finalizing the rmse calculations
        mae = round(abs_res_sqr / len(self.df1), 2)
    
        return mae
    
    def logcosh(self, df1, df2):
        """
        This method will compute the Log-Cosh Loss function.

        Argument(s): df1, df2

        Return(s): lgcosh
        """

        # Declaring the arguments
        self.df1 = df1
        self.df2 = df2

        # Computing the logcosh
        lgh = np.sum(np.log(np.cosh(np.absolute(self.df1 - self.df2))))
        return lgh


class pwpTasks():
    """
    This class contains the df_loader() method for loading different datasets with
    different extensions. This project will continue to be developed after this project.
    Support is highly welcome when a separate GitHub project folder is opened for it.
    """
    
    def df_loader(self, filepath, sep=','):
        """
        This method will load any dataset supported by pandas library.
        Four (4) pandas read_formats are supported.
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
