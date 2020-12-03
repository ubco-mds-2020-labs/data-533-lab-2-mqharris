# summary_classes.py
import pandas as pd
import numpy as np


class Df_Info:
    """
    Dataframe class
    """


    def __init__(self, df, type="columns"):
        """
        Initializes dataframe class with option to select column or row.

        Parameters
        ----------
        df : pandas.DataFrame
            Pandas Dataframe to be viewed
        type : str, optional {"columns", "rows"}

        Returns
        -------
        None

        Examples
        --------
        >>> Df_Info(pd.DataFrame(df), "rows")
        """
        if not isinstance(df, pd.DataFrame):
            raise Exception("Input must be a pandas DataFrame")
        if not (type in ("columns", "rows")):
            raise Exception("choose another type option either: rows or columns")
        self.df = df
        self.type = type
        self.rows = self.df.shape[0]
        self.columns = self.df.shape[0]

    def total_max(self): 
        """
        Calculates the max value in the data frame.

        Parameters
        ----------
        None

        Returns
        -------
        float
        or 
        Null value
        """
        try:
            return self.df.max().max()
        except:
            return np.nan

    def total_min(self):
        """
        Calculates the min value in the data frame.

        Parameters
        ----------
        None

        Returns
        -------
        float
        or 
        Null value
        """
        try:
            return self.df.min().min()
        except:
            return np.nan

    def total_mean(self):
        """
        Calculates the mean value in the data frame.

        Parameters
        ----------
        None

        Returns
        -------
        float
        or 
        Null value
        """
        try:
            return self.df.mean(numeric_only=True).mean(numeric_only=True)
        except:
            return np.nan

    def total_missing(self):
        """
        Sums up the amount of missing values in the data frame.

        Parameters
        ----------
        None

        Returns
        -------
        int
        """
        return self.df.isnull().sum().sum()


class Missing(Df_Info):
    """
    Class used to show missing value stats of Pandas Dataframe
    """
    def __init__(self, df, type="columns"):
        """
        Initializes class with option to select column or row.

        Parameters
        ----------
        df : pandas.DataFrame
            Pandas Dataframe to be viewed
        type : str, optional {"columns", "rows"}

        Returns
        -------
        None

        Examples
        --------
        >>> Missing(pd.DataFrame(df), "rows")
        """
        Df_Info.__init__(self, df, type)
        if self.type == "columns":
            self.count_missing = df.isnull().sum()
            self.percent_missing = self.count_missing / self.columns
        else:
            self.count_missing = df.isnull().sum(axis=1)
            self.percent_missing = self.count_missing / self.rows


class Stats(Df_Info):
    """
    Class used to store min, max, and mean values of Pandas Dataframe
    """   
    def __init__(self, df, type="columns"):
        """
        Initializes class with option to select column or row.

        Parameters
        ----------
        df : pandas.DataFrame
            Pandas Dataframe to be viewed
        type : str, optional {"columns", "rows"}

        Returns
        -------
        None

        Examples
        --------
        >>> Stats(pd.DataFrame(df), "rows")
        """
        Df_Info.__init__(self, df, type)
        if self.type == "columns":
            self.sub_max = df.max(numeric_only=True)
            self.sub_min = df.min(numeric_only=True)
            self.sub_mean = df.mean(numeric_only=True)
        else:
            self.sub_max = df.max(axis=1, numeric_only=True)
            self.sub_min = df.min(axis=1, numeric_only=True)
            self.sub_mean = df.mean(axis=1, numeric_only=True)
