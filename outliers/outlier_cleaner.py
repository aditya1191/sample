#!/usr/bin/python
import numpy as np
from sklearn.metrics import mean_squared_error


def outlierCleaner(new_worth_predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    # The mean square error
    # np.mean((new_worth_predictions - net_worths)**2) 
    all_error = mean_squared_error(net_worths, new_worth_predictions)
    print(all_error)
    # return cleaned_data
'''
from sklearn.metrics import mean_squared_error
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
mean_squared_error(y_true, y_pred)
y_true = [[0.5, 1],[-1, 1],[7, -6]]
y_pred = [[0, 2],[-1, 2],[8, -5]]
mean_squared_error(y_true, y_pred)
mean_squared_error(y_true, y_pred, multioutput='raw_values')
mean_squared_error(y_true, y_pred, multioutput=[0.3, 0.7])
'''