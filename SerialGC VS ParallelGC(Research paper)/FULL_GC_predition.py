from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_log_error
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
x_a=[]
y_a=[]
data = pd.read_csv("dataset_P_S.csv")
X = data.iloc[:,:-4]
print(X)
y = data.iloc[:, -3]
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42, test_size=.40)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("DecisionTreeRegressor : "+str(r2_score(y_test, y_pred)*100))
y_a.append(r2_score(y_test, y_pred)*100)
x_a.append("DecisionTree")
lin = LinearRegression()
lin.fit(X_train, y_train)
y_pred = lin.predict(X_test)
print("LinearRegression : "+str(r2_score(y_test, y_pred)*100))
y_a.append(r2_score(y_test, y_pred)*100)
x_a.append("Linear")

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
rfr = RandomForestRegressor(n_estimators = 100)
rfr.fit(X_train,y_train)
y_pred = rfr.predict(X_test)
s = mean_squared_log_error(y_test, y_pred)
accuracy = 1 - s
print("RandomForestRegressor : "+str(accuracy*100))
y_a.append(accuracy*100)
x_a.append("RandomForest")
classifier = LogisticRegression(random_state = 10)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("LogisticRegression : "+str(r2_score(y_test, y_pred)*100))
y_a.append(r2_score(y_test, y_pred)*100)
x_a.append("Logistic")
plt.bar(x_a, y_a, width=0.25, color=['red'])
plt.xlabel('Algorithms')
plt.ylabel('Accuracy(0%-100%)')
plt.title('Number of FULL-GC Prediction Graph')
plt.legend()
plt.show()