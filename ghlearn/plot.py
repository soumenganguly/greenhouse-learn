import math 
from numpy import sum as arraysum
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

# set this value after every training phase on new dataset
PI_INTERVAL = 4.88

# to be run internally to calculate the PI everytime the model is trained with new datapoints
def confidence_interval(actual, prediction, alpha):
    ci_upper = []
    ci_lower = []
    
    z = st.norm.ppf(1-(1-alpha)/2) 
    sum_errs = arraysum((actual-prediction)**2)
    stdev = math.sqrt(1/(len(actual)-2) * sum_errs)
    ci_interval = z*stdev

    for pred in prediction:
        ci_upper.append(pred+ci_interval)
        ci_lower.append(pred-ci_interval)
    return ci_upper, ci_lower

def forecast_plot(y_pred, path=None):
    ci_l = []
    ci_u = []
    for pred in y_pred:
        ci_l.append(pred-PI_INTERVAL)
        ci_u.append(pred+PI_INTERVAL)
    
    figure = plt.figure(figsize=(12,5))
    
    plt.plot(y_pred, marker='.', label="Actual", color='navy')
    plt.fill_between(np.arange(0,len(y_pred),1), ci_l, ci_u ,alpha=0.3, label = 'Confidence inerval (80%)',color='firebrick')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.savefig(path)