import os
import math
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from coordinates import LocalCoord
import coordinates as coord

# Load data from files
# input_size = 39
input_size = 55 
PRN_size = 32
res_size = 1
label_size = 3

# Origin of NED coordinate system
# Latitude, Longitude, and Altitude
# # Rural area
# origin_ned = np.array([37.471338, -122.237757, 13])

# Urban area
origin_ned = np.array([37.334342, -121.887827, 24])

local_coord = LocalCoord(origin_ned, coord.geodetic2ecef(origin_ned))

# %% *********************************** Reading training data in multiple data files ***********************************
training_data_dir = "../data/Dynamic/Data4QE/RouteUS/Training/"
# Get all files in the current directory
training_data_files = os.listdir(training_data_dir)
inputs_list = []
labels_list = []
for data_file in training_data_files:
    # If the object is not a directory, we will open and read it
    data_file_path = training_data_dir+'/'+data_file
    if not os.path.isdir(data_file_path):
        # Read one data file
        data = pd.read_csv(data_file_path)
        
        # Input features: E, N, C/N0, Elevation
        # Convert Ground truth location from ECEF to NED
        NED = local_coord.ecef2ned(np.array(data.iloc[:, 10:13].values))
        inputs = np.concatenate([NED[:, 1::-1], np.array(data.iloc[:, 8:9].values), np.array(data.iloc[:, 6:7].values/math.pi*180)], axis =1)
        
        # Unsmoothed pseudorange residuals
        labels = np.array(data.iloc[:, 31:32].values)
        
        inputs_list.append(inputs)
        labels_list.append(labels)

InputsAll = np.concatenate(inputs_list, axis = 0) 
LabelsAll = np.ravel(np.concatenate(labels_list, axis = 0))

# %% *********************************** Train Random Forest ***********************************

# Number of features randomly selected for node splitting 
s = 2

# Number of trees
m = 2000

# K-fold cross validated grid-search for hyperparameter tweaking
rfRegressor = RandomForestRegressor(n_estimators=m, max_features=s)
parameters = {'max_depth':[3, 5, 7, 10, 20], 'max_samples':[0.1, 0.2, 0.3, 0.4, 0.5]}
regr = GridSearchCV(rfRegressor, parameters, scoring='neg_mean_squared_error', cv=5)
regr.fit(InputsAll, LabelsAll)

# save the model to disk
filename = 'finalized_RF_bestModel_urban.sav'
pickle.dump(regr.best_estimator_, open(filename, 'wb'))

regr.best_params_
