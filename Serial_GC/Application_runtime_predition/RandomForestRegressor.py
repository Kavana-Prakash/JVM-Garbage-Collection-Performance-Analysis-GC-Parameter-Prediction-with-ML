import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_log_error
data = pd.read_csv("../dataset.csv")
X = data.iloc[:,:-4]
y = data.iloc[:, -4]
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42, test_size=0.40)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
rfr = RandomForestRegressor(n_estimators = 100)
rfr.fit(X_train,y_train)
y_pred = rfr.predict(X_test)
s = mean_squared_log_error(y_test, y_pred)
accuracy = 1 - s
print(accuracy)




