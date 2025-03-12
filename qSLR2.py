import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
df_cars = sm.datasets.get_rdataset("cars", "datasets", cache=True).data

def PlotSLRCI(fit, data):
    X = data["speed"]
    Y = data["dist"]
    Xsorted = np.sort(X)
    Xwithconst = sm.add_constant(Xsorted)  
    pred = fit.get_prediction(Xwithconst)
    predm = pred.predicted_mean
    cilower, ciupper = pred.conf_int().T

    plt.scatter(X, Y, facecolors='none', edgecolors='black', label="Data", alpha=0.7)
    plt.plot(Xsorted, predm, label="Regression Line", color="black")
    plt.plot(Xsorted, cilower, linestyle="solid", color="black")
    plt.plot(Xsorted, ciupper, linestyle="solid", color="black")
    plt.xlabel("speed")
    plt.ylabel("dis")
    plt.show()

X = df_cars["speed"]
Y = df_cars["dist"]
X_const = sm.add_constant(X)  
fit = sm.OLS(Y, X_const).fit()
PlotSLRCI(fit, df_cars)
