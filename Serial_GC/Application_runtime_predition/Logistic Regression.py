import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
data = pd.read_csv("../dataset.csv")
X = data.iloc[:,:-4]
y = data.iloc[:, -4]
for i in range(0,len(y)):
    y[i]=int(y[i])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.40, random_state =42)
sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)
classifier = LogisticRegression(random_state = 10)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(r2_score(y_test, y_pred))