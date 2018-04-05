import numpy as np
import pandas as pd
slump_data = pd.read_csv('C:/Krishna/UB/Spring18/CSE 574 ML/proj1/slump_test_data_mod.csv')

#choosing explanatory variables : X
exp_vars = ['Cement', 'Slag', 'Fly_ash', 'Water', 'SP', 'Coarse_Aggr', 'Fine_Aggr']
X = slump_data[exp_vars]

# selecting response variable : y
y = slump_data.SLUMP

from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import linear_model

# 10 iterations

r2_scr_fin_lin, mse_fin_lin_lst = [], []
mse_fin_las_lst, mse_fin_rig_lst = [], []

for _ in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=(85 / 103), test_size=(18 / 103))

    r2_scr_lin = []
    mse_lin_lst, mse_las_lst, mse_rig_lst = [], [], []
    r2_val_dict_lin = {}
    mse_val_dict_lin, mse_val_dict_las, mse_val_dict_rig = {}, {}, {}

    clf_lin = linear_model.LinearRegression()  # selecting the model: linear
    clf_las = linear_model.Lasso(alpha=1.0)  # selecting the model: lasso
    clf_rig = linear_model.Ridge(alpha=0.0)  # selecting the model: ridge

    for i in range(0, len(X_train), len(X_train) // 5):  # 5 fold CV
        val_X = X_train[i:i + 17]
        val_y = y_train[i:i + 17]
        train_X = pd.concat([X_train[0:i], X_train[i + 17:]])
        train_y = pd.concat([y_train[0:i], y_train[i + 17:]])

        # linear regression
        lm = linear_model.LinearRegression()  # selecting the model
        lm.fit(train_X, train_y)  # fitting the model
        val_y_pred_lin = lm.predict(val_X)  # predicting the model
        r2_lin = r2_score(val_y, val_y_pred_lin)  # calculating r^2
        mse_lin = mean_squared_error(val_y, val_y_pred_lin)
        mse_lin_lst.append(mse_lin)
        r2_scr_lin.append(r2_lin)  # saving r^2 value of the current iteration
        r2_val_dict_lin[r2_lin] = [train_X, train_y]  # saving the model data into a dict
        mse_val_dict_lin[mse_lin] = [train_X, train_y]  # saving the model data into a dict

        # lasso regression
        ls = linear_model.Lasso(alpha=1.0)
        ls.fit(train_X, train_y)
        val_y_pred_las = ls.predict(val_X)
        mse_las = mean_squared_error(val_y, val_y_pred_las)
        mse_las_lst.append(mse_las)
        mse_val_dict_las[mse_las] = [train_X, train_y]  # saving the model data into a dict

        # ridge regression
        ri = linear_model.Ridge(alpha=0.0)
        ri.fit(train_X, train_y)
        val_y_pred_rig = ri.predict(val_X)
        mse_rig = mean_squared_error(val_y, val_y_pred_rig)
        mse_rig_lst.append(mse_rig)
        mse_val_dict_rig[mse_rig] = [train_X, train_y]  # saving the model data into a dict

    # training the classifier again using the best model returned by CV

    # linear regression r2_square calculation
    clf_lin.fit(r2_val_dict_lin[max(r2_scr_lin)][0], r2_val_dict_lin[max(r2_scr_lin)][1])
    y_test_pred_lin = clf_lin.predict(X_test)
    r2_fin_lin = r2_score(y_test, y_test_pred_lin)  # calculating r^2
    r2_scr_fin_lin.append(r2_fin_lin)
    # mse calculation
    clf_lin.fit(mse_val_dict_lin[min(mse_lin_lst)][0], mse_val_dict_lin[min(mse_lin_lst)][1])
    y_test_pred_lin = clf_lin.predict(X_test)
    mse_fin_lin = mean_squared_error(y_test, y_test_pred_lin)
    mse_fin_lin_lst.append(mse_fin_lin)

    # lasso regression mse calculation
    clf_las.fit(mse_val_dict_las[min(mse_las_lst)][0], mse_val_dict_las[min(mse_las_lst)][1])
    y_test_pred_las = clf_las.predict(X_test)
    mse_fin_las = mean_squared_error(y_test, y_test_pred_las)  # calculating r^2
    mse_fin_las_lst.append(mse_fin_las)

    # ridge regression mse calculation
    clf_rig.fit(mse_val_dict_rig[min(mse_rig_lst)][0], mse_val_dict_rig[min(mse_rig_lst)][1])
    y_test_pred_rig = clf_rig.predict(X_test)
    mse_fin_rig = mean_squared_error(y_test, y_test_pred_rig)  # calculating r^2
    mse_fin_rig_lst.append(mse_fin_rig)

r2_square_mean_lin = np.mean(r2_scr_fin_lin)
print("r2_scr_fin_lin: ", r2_scr_fin_lin)
print("r2_square_mean_lin: ", r2_square_mean_lin)
mse_mean_lin = np.mean(mse_fin_lin_lst)
print("mse_fin_lin_lst: ", mse_fin_lin_lst)
print("mse_mean_lin: ", mse_mean_lin)

mse_mean_las = np.mean(mse_fin_las_lst)
print("mse_fin_las_lst: ", mse_fin_las_lst)
print("mse_mean_las: ", mse_mean_las)

mse_mean_rig = np.mean(mse_fin_rig_lst)
print("mse_fin_rig_lst: ", mse_fin_rig_lst)
print("mse_mean_rig: ", mse_mean_rig)
