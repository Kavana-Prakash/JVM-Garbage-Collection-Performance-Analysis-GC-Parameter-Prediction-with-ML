from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
data = pd.read_csv("../dataset.csv")
X = data.iloc[:,:-4]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42, test_size=.40)
lin = LinearRegression()
lin.fit(X_train, y_train)
y_pred = lin.predict(X_test)
print(r2_score(y_test, y_pred))
