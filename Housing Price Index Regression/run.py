import pandas as pd
price_index = pd.read_csv('monthly-hpi.csv')
unemployment = pd.read_csv('unemployment-macro.csv')
fed_rate = pd.read_csv('fed_funds.csv')
shiller = pd.read_csv('shiller.csv')
gdp = pd.read_csv('gdp.csv')
df = shiller.merge(price_index, on='date')\
.merge(unemployment, on='date')\
.merge(fed_rate, on='date')\
.merge(gdp, on='date')
#print df.head()
import statsmodels as sm
from statsmodels.formula.api import ols
from statsmodels.graphics.regressionplots import plot_regress_exog
housing_model = ols('housing_price_index~total_unemployed',data=df).fit()
s = housing_model.summary()
print s 
#%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(15,8))
print plot_regress_exog
fig = plot_regress_exog(housing_model,'total_unemployed',fig=fig)
plt.show()
