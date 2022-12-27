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
fields_P = ['XMX','Throughput(%)','Latency(Max GC pause time)(s)','Application runtime','FULL GC','GC','RandomForest','KNeighbors','DecisionTree','MLP','Ensemble']
filename_P = "result_P.csv"
#Extracting columns from dataset1 as array
with open(filename_P, 'w') as csvfile_P:
    csvwriter_P = csv.writer(csvfile_P)
    csvwriter_P.writerow(fields_P)
data_P = pd.read_csv("dataset_P1.csv")  #appending to resultant_dataset
Throughput_P=data_P['Throughput(%)']
Latency_P=data_P['Latency(Max GC pause time)(s)']
Application_runtime_P=data_P['Application runtime(s)']
FULL_GC_P=data_P['FULL GC']
GC_P=data_P['GC']
n_f_P=2
Next_P=0

for C_P in range(0, 178):
    stor_P = []
    stor_P.append(n_f_P)
    stor_P.append(Throughput_P[Next_P])
    stor_P.append(Latency_P[Next_P])
    stor_P.append(Application_runtime_P[Next_P])
    stor_P.append(FULL_GC_P[Next_P])
    stor_P.append(GC_P[Next_P])
    dataset_name_P = "dataset_P/Xms2m_Xmx" + str(n_f_P) + "m_PGC.csv"
    data_P = pd.read_csv(dataset_name_P)
    fig, ax = plt.subplots()
    ax.scatter(x=data_P['CPU Time(s)'], y=data_P['GC/FULL-GC(1->GC,0->FULL-GC)'])
    #giving x and y column
    X_P = data_P.iloc[:, :-1]
    y_P = data_P.iloc[:, -1]
    #splitting train and test
    X_train_P, X_test_P, y_train_P, y_test_P = train_test_split(X_P, y_P, random_state=42, test_size=.40)
    classifier_P = RandomForestClassifier(n_estimators=50) #Intitializing algorithm
    classifier_P.fit(X_train_P, y_train_P) #building model
    y_pred_P = classifier_P.predict(X_test_P) #y value prediction
    result2_P = accuracy_score(y_test_P, y_pred_P) #accuracy calculation
    stor_P.append(result2_P * 100) #stroing RF accuracy to classifier_dataset
    # length of train n test values
    l_y_train_P = len(y_train_P)
    l_y_test_P = len(y_test_P)
    GC_FULL_GC_P = []
    YoungGen_allocated_space_P = []
    YoungGen_Before_GC_P = []
    YoungGen_After_GC_P = []
    Old_Gen_allocated_space_P = []
    Old_Gen_Before_GC_P = []
    Old_Gen_After_GC_P = []
    GC_Pause_Time_P = []
    Real_Time_P = []
    CPU_Time_P = []
    User_P = []
    Sys_P = []
    #appending values to temporary csv file
    for i_P in X_train_P['Real Time(s)']:
        Real_Time_P.append(i_P)
    for i_P in X_train_P['CPU Time(s)']:
        CPU_Time_P.append(i_P)
    for i_P in X_train_P['YoungGen (allocated space)(KB)']:
        YoungGen_allocated_space_P.append(i_P)
    for i_P in X_train_P['YoungGen (Before GC)(KB)']:
        YoungGen_Before_GC_P.append(i_P)
    for i_P in X_train_P['YoungGen (After GC)(KB)']:
        YoungGen_After_GC_P.append(i_P)
    for i_P in X_train_P['Old Gen(allocated space)(KB)']:
        Old_Gen_allocated_space_P.append(i_P)
    for i_P in X_train_P['Old Gen (Before GC)(KB)']:
        Old_Gen_Before_GC_P.append(i_P)
    for i_P in X_train_P['Old Gen(After GC)(KB)']:
        Old_Gen_After_GC_P.append(i_P)
    for i_P in X_train_P['GC Pause Time(ms)']:
        GC_Pause_Time_P.append(i_P)
    for i_P in X_train_P['User(s)']:
        User_P.append(i_P)
    for i_P in X_train_P['Sys(s)']:
        Sys_P.append(i_P)
    for i_P in y_train_P:
        GC_FULL_GC_P.append(i_P)
    for i_P in X_test_P['Real Time(s)']:
        Real_Time_P.append(i_P)
    for i_P in X_test_P['CPU Time(s)']:
        CPU_Time_P.append(i_P)
    for i_P in X_test_P['YoungGen (allocated space)(KB)']:
        YoungGen_allocated_space_P.append(i_P)
    for i_P in X_test_P['YoungGen (Before GC)(KB)']:
        YoungGen_Before_GC_P.append(i_P)
    for i_P in X_test_P['YoungGen (After GC)(KB)']:
        YoungGen_After_GC_P.append(i_P)
    for i_P in X_test_P['Old Gen(allocated space)(KB)']:
        Old_Gen_allocated_space_P.append(i_P)
    for i_P in X_test_P['Old Gen (Before GC)(KB)']:
        Old_Gen_Before_GC_P.append(i_P)
    for i_P in X_test_P['Old Gen(After GC)(KB)']:
        Old_Gen_After_GC_P.append(i_P)
    for i_P in X_test_P['GC Pause Time(ms)']:
        GC_Pause_Time_P.append(i_P)
    for i_P in X_test_P['User(s)']:
        User_P.append(i_P)
    for i_P in X_test_P['Sys(s)']:
        Sys_P.append(i_P)
    for i_P in y_test_P:
        GC_FULL_GC_P.append(i_P)
    fields_P = ['YoungGen (allocated space)(KB)', 'YoungGen (Before GC)(KB)',
              'YoungGen (After GC)(KB)', 'Old Gen(allocated space)(KB)', 'Old Gen (Before GC)(KB)',
              'Old Gen(After GC)(KB)', 'GC Pause Time(ms)', 'User(s)', 'Sys(s)', 'Real Time(s)', 'CPU Time(s)', 'GC/FULL-GC(1->GC,0->FULL-GC)']
    rows_P = []
#merging as 2D array
    for i_P in range(0, len(YoungGen_allocated_space_P)):
        arr_P = []

        arr_P.append(YoungGen_allocated_space_P[i_P])
        arr_P.append(YoungGen_Before_GC_P[i_P])
        arr_P.append(YoungGen_After_GC_P[i_P])
        arr_P.append(Old_Gen_allocated_space_P[i_P])
        arr_P.append(Old_Gen_Before_GC_P[i_P])
        arr_P.append(Old_Gen_After_GC_P[i_P])
        arr_P.append(GC_Pause_Time_P[i_P])
        arr_P.append(User_P[i_P])
        arr_P.append(Sys_P[i_P])
        arr_P.append(Real_Time_P[i_P])
        arr_P.append(CPU_Time_P[i_P])
        arr_P.append(GC_FULL_GC_P[i_P])
        rows_P.append(arr_P)
    filename_P = "temporary.csv"
    with open(filename_P, 'w') as csvfile_P:
        csvwriter_P = csv.writer(csvfile_P)
        csvwriter_P.writerow(fields_P)
        csvwriter_P.writerows(rows_P)
    dataset_P = pd.read_csv(filename_P)
    ds1_P = dataset_P.dropna()

    # giving x and y column
    x_P = ds1_P.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8.9,10]].values
    y_P = ds1_P.iloc[:, 11].values
    train_x_P, train_y_P = x_P[:l_y_train_P], y_P[:l_y_train_P]
    test_x_P, test_y_P = x_P[l_y_test_P:], y_P[l_y_test_P:]
    base_learners_P = []

    #Initializing 3 base algorithms
    knn_P = KNeighborsClassifier(n_neighbors=2)
    base_learners_P.append(knn_P)
    dtr_P = DecisionTreeClassifier(max_depth=2)
    base_learners_P.append(dtr_P)
    mlpc_P = MLPClassifier(hidden_layer_sizes=(100,), solver='lbfgs', max_iter=3000, random_state=123456)
    base_learners_P.append(mlpc_P)

    meta_data_P = np.zeros((len(base_learners_P), len(train_x_P)))
    meta_targets_P = np.zeros(len(train_x_P))
    KF_P = KFold(n_splits=5)
    meta_index_P = 0
    for train_indices_P, test_indices_P in KF_P.split(train_x_P):
        #building model for 3 algo
        for i_P in range(len(base_learners_P)):
            learner_P = base_learners_P[i_P]
            learner_P.fit(train_x_P, train_y_P)
            predictions_P = learner_P.predict_proba(train_x_P[test_indices_P])[:, 0]
            meta_data_P[i_P][meta_index_P:meta_index_P + len(test_indices_P)] = predictions_P
        meta_targets_P[meta_index_P:meta_index_P + len(test_indices_P)] = train_y_P[test_indices_P]
        meta_index_P += len(test_indices_P)
    meta_data_P = meta_data_P.transpose()
    test_meta_data_P = np.zeros((len(base_learners_P), len(test_x_P)))
    base_acc_P = []
    #predict and finding accuracy for 3 algo
    for i_P in range(len(base_learners_P)):
        learner_P = base_learners_P[i_P]
        learner_P.fit(train_x_P, train_y_P)
        predictions_P = learner_P.predict_proba(test_x_P)[:, 0]
        test_meta_data_P[i_P] = predictions_P
        acc_P = metrics.accuracy_score(test_y_P, learner_P.predict(test_x_P))
        base_acc_P.append(acc_P)
    #Initializing ensemble
    test_meta_data_P = test_meta_data_P.transpose()
    meta_learner_P = LogisticRegression(solver='lbfgs', max_iter=3000)
    #fitting ensemble and predicting y value then finding accuracy
    meta_learner_P.fit(meta_data_P, meta_targets_P)
    ensemble_predictions_P = meta_learner_P.predict(test_meta_data_P)
    acc_P = metrics.accuracy_score(test_y_P, ensemble_predictions_P)
    #storing accuracy of 3 algo to classifier dataset(array)
    for i_P in range(len(base_learners_P)):
        learner_P = base_learners_P[i_P]
        stor_P.append(base_acc_P[i_P] * 100)
    stor_P.append(acc_P * 100) #storing accuracy of ensemble to classifier dataset
    #appending 1 row(1logfile prediction_accuracy) to classifier dataset from stored array
    with open('result_P.csv', 'a') as f_object_P:
        writer_object_P = writer(f_object_P)
        writer_object_P.writerow(stor_P)
        f_object_P.close()
    Next_P=Next_P+1
    if n_f_P==2:
        n_f_P=n_f_P+98
    else:
        n_f_P=n_f_P+100