from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd
from sklearn.svm import SVR
data = pd.read_csv("../dataset.csv")
X = data.iloc[:,:-4]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42, test_size=.40)
SVM_regression = SVR()
SVM_regression.fit(X_train, y_train)
y_hat = SVM_regression.predict(X_test)
print(r2_score(y_test, y_hat))

