import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import cross_validate

from sklearn.model_selection import KFold
from glmnet_python import glmnet

slump_data = pd.read_csv('C:/Krishna/UB/Spring18/CSE 574 ML/proj1/slump_test_data_mod.csv')

slump_data.info()
#print(slump_data.columns)

#choosing explanatory variables : X
exp_vars = ['Cement', 'Slag', 'Fly_ash', 'Water', 'SP', 'Coarse_Aggr', 'Fine_Aggr']
X = slump_data[exp_vars]

# selecting response variable : y
y = slump_data.SLUMP

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,train_size = (85/103), test_size=(18/103))

X_train_mat = X_train.as_matrix()
# print(X_train_mat)

from glmnet_python import cvglmnet
from glmnet_python import glmnet
#from glmnetPlot import glmnetPlot
from glmnet_python import cvglmnet

gauss_m = cvglmnet(x = X_train, y = y_train, family = 'gaussian', nfolds = 5, grouped = True)