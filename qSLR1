import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
def MyLM(formula, data):
fit = smf.ols(formula=formula, data=data).fit()
return fit
x = np.arange(1, 4)
y = x * np.random.normal(2, 0.1, 3)
f = "y ~ x"
df = pd.DataFrame({'x': x, 'y': y})
model = smf.ols(f, data=df).fit()
print(model.summary())
