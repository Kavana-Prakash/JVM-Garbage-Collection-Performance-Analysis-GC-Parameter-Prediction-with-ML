from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_log_error
import matplotlib.pyplot as plt
data = pd.read_csv("dataset_P_S.csv")
X = data.iloc[:,:-4]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42, test_size=.98)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("DecisionTreeRegressor : "+str(r2_score(y_test, y_pred)*100))

tree.plot_tree(regressor);
fn=['Throughput(%)','Latency(Max GC pause time)(s)','Type of GC(0->parllal,1->serial)']
cn=['Maximum Heap Size(Xmx)']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
tree.plot_tree(regressor,
               feature_names = fn,
               class_names=cn,
               filled = True);
fig.savefig('imagename.png')