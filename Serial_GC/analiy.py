import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from csv import writer
fields = ['XMX','Throughput(%)','Latency(Max GC pause time)(s)','Application runtime','FULL GC','GC','RandomForest','KNeighbors','DecisionTree','MLP','Ensemble']
filename = "reslut.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
data = pd.read_csv("dataset.csv")
Throughput=data['Throughput(%)']
Latency=data['Latency(Max GC pause time)(s)']
Application_runtime=data['Application runtime(s)']
FULL_GC=data['FULL GC']
GC=data['GC']
n_f=2
add=0
while n_f<17701:
    stor = []
    stor.append(n_f)
    stor.append(Throughput[add])
    stor.append(Latency[add])
    stor.append(Application_runtime[add])
    stor.append(FULL_GC[add])
    stor.append(GC[add])
    dataset_name= "dataset/Xms2m_Xmx"+str(n_f)+"m_SGC.csv"
    data = pd.read_csv(dataset_name)
    fig, ax = plt.subplots()
    ax.scatter(x=data['CPU Time(s)'], y=data['GC/FULL-GC(1->GC,0->FULL-GC)'])
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.40)
    classifier = RandomForestClassifier(n_estimators=50)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    result = confusion_matrix(y_test, y_pred)
    result1 = classification_report(y_test, y_pred)
    result2 = accuracy_score(y_test, y_pred)
    stor.append(result2*100)
    le1 = len(y_train)
    le2=len(y_test)
    GC_FULL_GC = []
    DefNew_allocated_space = []
    DefNew_Before_GC = []
    DefNew_After_GC = []
    Tenured_allocated_space = []
    Tenured_Before_GC = []
    Tenured_After_GC = []
    User_Time = []
    System_Time = []
    Real_Time = []
    CPU_Time = []
    GC_Pause_Time = []
    for i in X_train['User(s)']:
        User_Time.append(i)
    for i in X_train['Sys(s)']:
        System_Time.append(i)
    for i in X_train['Real Time(s)']:
        Real_Time.append(i)
    for i in X_train['CPU Time(s)']:
        CPU_Time.append(i)
    for i in X_train['DefNew (allocated space)(KB)']:
        DefNew_allocated_space.append(i)
    for i in X_train['DefNew (Before GC)(KB)']:
        DefNew_Before_GC.append(i)
    for i in X_train['DefNew (After GC)(KB)']:
        DefNew_After_GC.append(i)
    for i in X_train['Tenured (allocated space)(KB)']:
        Tenured_allocated_space.append(i)
    for i in X_train['Tenured (Before GC)(KB)']:
        Tenured_Before_GC.append(i)
    for i in X_train['Tenured (After GC)(KB)']:
        Tenured_After_GC.append(i)
    for i in X_train['GC Pause Time(ms)']:
        GC_Pause_Time.append(i)
    for i in y_train:
        GC_FULL_GC.append(i)
    for i in X_test['User(s)']:
        User_Time.append(i)
    for i in X_test['Sys(s)']:
        System_Time.append(i)
    for i in X_test['Real Time(s)']:
        Real_Time.append(i)
    for i in X_test['CPU Time(s)']:
        CPU_Time.append(i)
    for i in X_test['DefNew (allocated space)(KB)']:
        DefNew_allocated_space.append(i)
    for i in X_test['DefNew (Before GC)(KB)']:
        DefNew_Before_GC.append(i)
    for i in X_test['DefNew (After GC)(KB)']:
        DefNew_After_GC.append(i)
    for i in X_test['Tenured (allocated space)(KB)']:
        Tenured_allocated_space.append(i)
    for i in X_test['Tenured (Before GC)(KB)']:
        Tenured_Before_GC.append(i)
    for i in X_test['Tenured (After GC)(KB)']:
        Tenured_After_GC.append(i)
    for i in X_test['GC Pause Time(ms)']:
        GC_Pause_Time.append(i)
    for i in y_test:
        GC_FULL_GC.append(i)
    fields = ['DefNew (allocated space)(KB)', 'DefNew (Before GC)(KB)',
              'DefNew (After GC)(KB)', 'Tenured (allocated space)(KB)', 'Tenured (Before GC)(KB)',
              'Tenured (After GC)(KB)', 'GC Pause Time(ms)', 'User(s)', 'Sys(s)', 'Real Time(s)', 'CPU Time(s)',
              'GC/FULL-GC(1->GC,0->FULL-GC)']
    rows = []
    for i in range(0, len(DefNew_allocated_space)):
        arr = []

        arr.append(DefNew_allocated_space[i])
        arr.append(DefNew_Before_GC[i])
        arr.append(DefNew_After_GC[i])
        arr.append(Tenured_allocated_space[i])
        arr.append(Tenured_Before_GC[i])
        arr.append(Tenured_After_GC[i])
        arr.append(GC_Pause_Time[i])
        arr.append(User_Time[i])
        arr.append(System_Time[i])
        arr.append(Real_Time[i])
        arr.append(CPU_Time[i])
        arr.append(GC_FULL_GC[i])
        rows.append(arr)
    dataset_name = "next_agl.csv"
    filename = dataset_name
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    dataset = pd.read_csv(dataset_name)
    ds1 = dataset.dropna()
    x = ds1.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8,9,10]].values
    y = ds1.iloc[:, 11].values
    train_x, train_y = x[:le1], y[:le1]
    test_x, test_y = x[le2:], y[le2:]
    base_learners = []
    knn = KNeighborsClassifier(n_neighbors=2)
    base_learners.append(knn)
    dtr = DecisionTreeClassifier(max_depth=2)
    base_learners.append(dtr)
    mlpc = MLPClassifier(hidden_layer_sizes=(100,), solver='lbfgs', max_iter=3000, random_state=123456)
    base_learners.append(mlpc)
    meta_learner = LogisticRegression(solver='lbfgs', max_iter=3000)
    meta_data = np.zeros((len(base_learners), len(train_x)))
    meta_targets = np.zeros(len(train_x))
    KF = KFold(n_splits=5)
    meta_index = 0
    for train_indices, test_indices in KF.split(train_x):
        for i in range(len(base_learners)):
            learner = base_learners[i]
            learner.fit(train_x, train_y)
            predictions = learner.predict_proba(train_x[test_indices])[:, 0]
            meta_data[i][meta_index:meta_index + len(test_indices)] = predictions
        meta_targets[meta_index:meta_index + len(test_indices)] = train_y[test_indices]
        meta_index += len(test_indices)
    meta_data = meta_data.transpose()
    test_meta_data = np.zeros((len(base_learners), len(test_x)))
    base_acc = []
    for i in range(len(base_learners)):
        learner = base_learners[i]
        learner.fit(train_x, train_y)
        predictions = learner.predict_proba(test_x)[:, 0]
        test_meta_data[i] = predictions
        acc = metrics.accuracy_score(test_y, learner.predict(test_x))
        base_acc.append(acc)
    test_meta_data = test_meta_data.transpose()
    meta_learner.fit(meta_data, meta_targets)
    ensemble_predictions = meta_learner.predict(test_meta_data)
    acc = metrics.accuracy_score(test_y, ensemble_predictions)
    for i in range(len(base_learners)):
        learner = base_learners[i]
        stor.append(base_acc[i] * 100)
    stor.append(acc * 100)
    with open('reslut.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(stor)
        f_object.close()
    add=add+1
    if n_f==2:
        n_f=n_f+98
    else:
        n_f=n_f+100