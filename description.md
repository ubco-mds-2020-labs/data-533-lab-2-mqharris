# Package: quickscreen

The quickscreen package provides simple tools for quickly reviewing a dataframe. The package includes three subpackages: one for plotting data, another for providing a simple summary statistics, and another which does simple manipulations and linear correlation. The package is basically a wrapper for various matplotlib and pandas functionality.

## Plot Subpackage 

The plot subpackage includes two modules, one module `plotter.py` creates a generic plotting class and the second module `grapher.py` uses the generic Plotter class to allow a user to create specific plots including a historgram, scatterplot, or scatter matrix. 

**plotter.py**

This module includes the Plotter parent class and has the following:

- Plotter(data, plot_title=None, label_names=None)
    - creates Plotter class object with input from a Pandas DataFrame
- Plotter.add_title(title)
    - add or update the plot title
- Plotter.add_label_names(x_label, y_label)
    - add or update plot x-axis and y-axis labels
- Plotter.show_plot()
    - provides a plot of the Plotter class object
- Plotter.save_plot(save_loc="", file_name=None)

This Plotter class is not meant to be called directly but is used as the parent class for the grapher module.

**grapher.py**

This module includes the HistogramPlot, ScatterPlot, and ScatterMatrix child classes of the Plotter parent class as follows:

- HistogramPlot(data, plot_title=None, label_names=None)
    - creates Histogram class object with input from a Pandas DataFrame
    - methods from Plotter class inherited
- ScatterPlot(data, plot_title=None, label_names=None)
    - creates ScatterPlot class object with input from a Pandas DataFrame
    - methods from Plotter class inherited
- ScatterMatrix(data, plot_title=None, label_names=None)
    - creates ScatterMatrix class object with input from a Pandas DataFrame
    - methods from Plotter class inherited

## Summary Subpackage

The summary subpackage includes a module `summary_classes.py` that has several classes which take a pandas DataFrame and auto-generate various statistics such as missing data counts, max/min/mean, and number of rows and columns. The second module `summary_stats.py` uses the classes from the `summary_classes` module to provide user functions for accessing the summary information.

**summary_classes.py**

This module has the class:
- Df_Info (df, type="columns")
    - Creates a Df_Info class object from a Pandas DataFrame.
    - This class is the building block for the Missing and Stats class.
Which contains the methods:
- Df_Info.total_max()
    - This returns the maximum value of the database.
- Df_Info.total_min()
    - This returns the minimum value of the database.
- Df_Info.total_mean()
    - This returns the average value of the database.
- Df_Info.total_missing()
    - This returns the total amount of missing values.
    
This module also has the class:
- Missing (df, type="columns")
    - Creates a Missing class object from a Pandas DataFrame.
    - Inherits methods from the Df_Info class.
    - Returns the total missing values and the percentage of missing values for each column (or row if type specified "row") upon initializiation.

This final class in this module is:
- Stats(df, type="columns")
    - Creates a Stats class object from a Pandas Dataframe.
    - Inherits methods from the Df_Info class.
    - Returns the maximum, minimum, and average value for each column (or row if type specified "row") upon initialization.
    

**summary_stats.py**

This module has the following functions which use the classes available in the `summary_classes` module:
- missing_summary(df, type="columns")
    - Takes a Pandas Dataframe and generates a Missing class object from the summary_classes module.
    - Returns the total missing values and the percentage of missing values for each column (or row if type specified "row").
- stats_summary(df, type="columns")
    - Takes a Pandas Dataframe and generates a Stats class object from the summary_classes module.
    - Returns the maximum, minimum, and average value for each column (or row if type specified "row").
- all_summary(df, type="columns")
    - Takes a Pandas Dataframe and calls upon the missing_summary() and stats_summary methods.
- simple_summary(df, type="columns")
    - Takes a Pandas Dataframe and generates a Df_Info class object from the summary_classes module.
    - Returns minimum, maximum, average, number of rows, number of columns, and number of missing values.


## Analysis Subpackage 

The analysis subpackage includes a module `datafill.py` that provides simple data manipulation functionality. The module has the DataEdit class which includes various methods for manipulating data outlined below.  The subpackage also includes the `linear_analysis.py` module to perform and plot simple linear analysis on selected columns in the dataframe.

**datafill.py**

This module includes the DataEdit parent class and includes the following:

- DataEdit(data)
    - creates DataEdit class object with input from a Pandas DataFrame
- DataEdit.display()
    - getter for the data attribute of the DataEdit instance
- DataEdit.columntype(column)
    - returns the datatype of the column given (either as a column name or column index)
- DataEdit.\_\_add__(other)
    - appends other (given as pandas.DataFrame) to DataEdit's data
- DataEdit.\_\_sub__(other)
    - removes from DataEdit.data the rows it shares with other (other is given as a pandas.DataFrame object)
- DataEdit.rm_duplicates()
    - removes duplicates from DataEdit.data
- DataEdit.rm_nan()
    - removes rows that contain NaN/None values from DataEdit.data
- DataEdit.quick_clean()
    - removes duplicate rows as well as removes rows with NaN/None values

This DataEdit class can be used directly or in conjunction with the Lm class.

**linear_analysis.py**

This module includes the Lm child class of the DataEdit parent class .The LM class includes the following:

- Lm(data)
    - creates Lm class object with input from a Pandas DataFrame
    - methods from DataEdit class inherited
- Lm.single_linear(predictor, estimator)
    - creates a single linear model between predictor and estimator (predictor is y, estimator is x)
    - returns the linear model's prediction on the estimator values
- Lm.single_linear_plot(predictor, estimator)
    - creates a plot of predictor vs estimator, displays the data as well as the created best fit line
- Lm.single_linear_eqn(predictor, estimator)
    - fits a single linear model to the predictor vs estimator
    - prints the equation of the line