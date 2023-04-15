import unittest
import pandas as pd
from ols_pwp import pwpTasks, pwpDeviation, pwpOLS


class Testolspwp(unittest.TestCase):

    def setUp(self):
        """
        This method is used for initializing the variables that will be
        used in the rest of the methods or test cases in the test program.
        Loading the three datasets is very important for all the test cases.
        Therefore, following the "Do not repeat yourself" (DRY) principle,
        using the setUP/tearDown methods combination is necessary.
        """

        # Creating the pwpTasks object for loading datasets.
        pt = pwpTasks()
        
        # Load the train, ideal and test datasets as pandas DataFrame objects
        self.train = pt.df_loader(r"C:\Users\tosin\GIT_clones\tosinaa_dlmdspwp01\implement\train.csv")
        self.ideal = pt.df_loader(r"C:\Users\tosin\GIT_clones\tosinaa_dlmdspwp01\implement\ideal.csv")
        self.test = pt.df_loader(r"C:\Users\tosin\GIT_clones\tosinaa_dlmdspwp01\implement\test.csv")

    def tearDown(self):
        pass
    
    def test_df_loader(self):
        """
        This is the df_loader method for loading datasets.
        It is built ontop of the pandas library.
        The test will compare the shape of the dataset loaded with
        the df_loader method and that loaded with pandas module.
        If the shape in both cases assert equal and true, that is
        the expected outcome. Other tests will check the shape of each dataset.
        """
        # Declaring the expected dataset loaded with pandas directly
        expected1 = pd.read_csv(r"C:\Users\tosin\GIT_clones\tosinaa_dlmdspwp01\implement\train.csv")
        expected2 = pd.read_csv(r"C:\Users\tosin\GIT_clones\tosinaa_dlmdspwp01\implement\ideal.csv")
        expected3 = pd.read_csv(r"C:\Users\tosin\GIT_clones\tosinaa_dlmdspwp01\implement\test.csv")
        
        train_shape = (400, 5)
        ideal_shape = (400, 51)
        test_shape = (100, 2)
        
        # Performing the test to compare the shapes of the train
        # dataset loaded with the olspwp.pwpTasks.df_loader and 
        # that loaded with pandas
        self.assertEqual(self.train.shape, expected1.shape)
        self.assertEqual(self.ideal.shape, expected2.shape)
        self.assertEqual(self.test.shape, expected3.shape)

        # Check the shape of each dataframe
        self.assertEqual(self.train.shape, train_shape)
        self.assertEqual(self.ideal.shape, ideal_shape)
        self.assertEqual(self.test.shape, test_shape)

    def test_squared_dev(self):
        """This tests the squared_dev method. It will check the output of the output of the
        squared_dev method to see if it is a list or not a list.
        """
        # Creating the instance of the pwpOLS object
        po = pwpOLS(self.train, self.ideal)

        # Performing the type check test
        self.assertEqual(type(po.squared_dev()), list)

    
    def test_idealfour_builder(self):
        """
        This method will be used to test the idealfour_builder method.
        It will require the use of the 2 class objects such as:
        1.    pwpTasks.df_loader()
        2.    pwpOLS.idealfour_builder()

        Argument(s): train, ideal

        Return: assertEqual len(idealfour.columns) = 5
        """

        # Initializing the class objects
        po = pwpOLS(self.train, self.ideal)

        # Declaring the expected output variable
        expected_len = 5

        # Performing the test
        self.assertEqual(len(po.idealfour_builder().columns), expected_len)

    def test_pwpDeviation(self):
        """
        This method will test if the result of the calculation of the max_deviation test dataset vs idf_in_test dataset.
        It passes when it is equal to the expected list output.

        Argument(s): test dataset, train dataset, ideal dataset

        Return(s): assert max_deviation(test, idf_in_test) = expected_lst
        """
        # Declaring the expected outcome
        expected_lst = [["y24", 20451.356]]

        # Initializing the class objects
        po = pwpOLS(self.train, self.ideal)
        
        # Create the idealfour dataset
        idealfour = po.idealfour_builder()

        # Subsetting the idealfour dataset to output the idf_in_test dataset.
        idf_in_test = idealfour[idealfour['x'].isin(self.test['x'])]

        # Creating the instance of the pwpDeviation object to gain access to the max_dev() method.       
        pdd = pwpDeviation(self.test, idf_in_test)
        max_deviation = pdd.max_dev()

        # Performing the test
        self.assertAlmostEquals(max_deviation, expected_lst)


if __name__ == "__main__":
    unittest.main()