from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
data = pd.read_csv("../dataset.csv")
X = data.iloc[:,:-4]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42, test_size=.40)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(r2_score(y_test, y_pred))