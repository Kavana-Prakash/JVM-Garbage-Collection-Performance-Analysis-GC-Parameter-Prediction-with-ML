import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import dataset

data = pd.read_csv("dataset_P_S.csv")
X = data.iloc[:,:-4]
y = data.iloc[:, -4]
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42, test_size=.20)
lin = LinearRegression()
lin.fit(X_train, y_train)
y_pred = lin.predict(X_test)
print("LinearRegression : "+str(r2_score(y_test, y_pred)*100))

sns.regplot(x=y_test,y=y_pred,scatter_kws={"color": "black"}, line_kws={"color": "red"});
#sns.regplot(x=y_test,y=y_pred,ci=None,scatter_kws={"color": "black"}, line_kws={"color": "red"});

plt.show()
