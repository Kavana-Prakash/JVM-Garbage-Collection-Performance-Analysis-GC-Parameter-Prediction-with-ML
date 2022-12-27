import csv
import matplotlib.pyplot as plt
file_P = open('result_P.csv')
csvreader_P = csv.reader(file_P)
header_P = []
header_P = next(csvreader_P)
rows_P = []
for row_P in csvreader_P:
    if len(row_P)>0:
        rows_P.append(row_P)
XMX_P=[]
Throughput_P=[]
Latency_P=[]
Application_runtime_P=[]
FULL_GC_P=[]
GC_P=[]
RandomForest_P=[]
KNeighbors_P=[]
DecisionTree_P=[]
MLP_P=[]
Ensemble_P=[]
for i_P in range(0,len(rows_P)):
    if int(rows_P[i_P][0])%200==0 or int(rows_P[i_P][0])==2:
        XMX_P.append(rows_P[i_P][0])
        Throughput_P.append(float(rows_P[i_P][1]))
        Latency_P.append(float(rows_P[i_P][2]))
        Application_runtime_P.append(float(rows_P[i_P][3]))
        FULL_GC_P.append(float(rows_P[i_P][4]))
        GC_P.append(float(rows_P[i_P][5]))
        RandomForest_P.append(float(rows_P[i_P][6]))
        KNeighbors_P.append(float(rows_P[i_P][7]))
        DecisionTree_P.append(float(rows_P[i_P][8]))
        MLP_P.append(float(rows_P[i_P][9]))
        Ensemble_P.append(float(rows_P[i_P][10]))

file_S = open('result_S.csv')
csvreader_S = csv.reader(file_S)
header_S = []
header_S = next(csvreader_S)
rows_S = []
for row_S in csvreader_S:
    if len(row_S)>0:
        rows_S.append(row_S)
XMX_S=[]
Throughput_S=[]
Latency_S=[]
Application_runtime_S=[]
FULL_GC_S=[]
GC_S=[]
RandomForest_S=[]
KNeighbors_S=[]
DecisionTree_S=[]
MLP_S=[]
Ensemble_S=[]
for i_S in range(0,len(rows_S)):
    if int(rows_S[i_S][0])%200==0 or int(rows_S[i_S][0])==2:
        XMX_S.append(rows_S[i_S][0])
        Throughput_S.append(float(rows_S[i_S][1]))
        Latency_S.append(float(rows_S[i_S][2]))
        Application_runtime_S.append(float(rows_S[i_S][3]))
        FULL_GC_S.append(float(rows_S[i_S][4]))
        GC_S.append(float(rows_S[i_S][5]))
        RandomForest_S.append(float(rows_S[i_S][6]))
        KNeighbors_S.append(float(rows_S[i_S][7]))
        DecisionTree_S.append(float(rows_S[i_S][8]))
        MLP_S.append(float(rows_S[i_S][9]))
        Ensemble_S.append(float(rows_S[i_S][10]))

'''plt.xticks(rotation=90)
plt.plot(XMX_P, RandomForest_P, label=header_P[6]+" ParallelGC")
plt.plot(XMX_S, RandomForest_S, label=header_S[6]+" SerialGC")
plt.plot(XMX_P, KNeighbors_P, label=header_P[7]+" ParallelGC")
plt.plot(XMX_S, KNeighbors_S, label=header_S[7]+" SerialGC")
plt.plot(XMX_P, DecisionTree_P, label=header_P[8]+" ParallelGC")
plt.plot(XMX_S, DecisionTree_S, label=header_S[8]+" SerialGC")
plt.plot(XMX_P, MLP_P, label=header_P[9]+" Parallel")
plt.plot(XMX_S, MLP_S, label=header_S[9]+" SerialGC")
plt.plot(XMX_P, Ensemble_P, label=header_P[10]+" ParallelGC")
plt.plot(XMX_S, Ensemble_S, label=header_S[10]+" SerialGC")
plt.xlabel('Xmx (ParallelGC & SerialGC)')
plt.ylabel('Accuracy(0%-100%)')
plt.title('Classifier Algorithms')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(XMX_P, RandomForest_P, label=header_P[6]+" ParallelGC")
plt.plot(XMX_S, RandomForest_S, label=header_S[6]+" SerialGC")
plt.xlabel('Xmx (ParallelGC & SerialGC)')
plt.ylabel('Accuracy(0%-100%)')
plt.title('Classifier Algorithm')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(XMX_P, KNeighbors_P, label=header_P[7]+" ParallelGC")
plt.plot(XMX_S, KNeighbors_S, label=header_S[7]+" SerialGC")
plt.xlabel('Xmx (ParallelGC & SerialGC)')
plt.ylabel('Accuracy(0%-100%)')
plt.title('Classifier Algorithm')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(XMX_P, DecisionTree_P, label=header_P[8]+" ParallelGC")
plt.plot(XMX_S, DecisionTree_S, label=header_S[8]+" SerialGC")
plt.xlabel('Xmx (ParallelGC & SerialGC)')
plt.ylabel('Accuracy(0%-100%)')
plt.title('Classifier Algorithm')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(XMX_P, MLP_P, label=header_P[9]+" ParallelGC")
plt.plot(XMX_S, MLP_S, label=header_S[9]+" SerialGC")
plt.xlabel('Xmx (ParallelGC & SerialGC)')
plt.ylabel('Accuracy(0%-100%)')
plt.title('Classifier Algorithm')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(XMX_P, Ensemble_P, label=header_P[10]+" ParallelGC")
plt.plot(XMX_S, Ensemble_S, label=header_S[10]+" SerialGC")
plt.xlabel('Xmx (ParallelGC & SerialGC)')
plt.ylabel('Accuracy(0%-100%)')
plt.title('Classifier Algorithm')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(XMX_P, Latency_P, label=header_P[2]+" ParallelGC")
plt.plot(XMX_P, Application_runtime_P, label=header_P[3]+" ParallelGC")
plt.plot(XMX_S, Latency_S, label=header_S[2]+" SerialGC")
plt.plot(XMX_S, Application_runtime_S, label=header_S[3]+" SerialGC")
plt.xlabel('Xmx (ParallelGC & SerialGC)')
plt.ylabel('Time(s)')
plt.title('Application Runtime/Latency Graph')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(XMX_P, Application_runtime_P, label=header_P[3]+" ParallelGC")
plt.plot(XMX_S, Application_runtime_S, label=header_S[3]+" SerialGC")
plt.xlabel('Xmx (ParallelGC & SerialGC)')
plt.ylabel('Time(s)')
plt.title('Application Runtime Graph')
plt.legend()
plt.show()'''
#font = {'size':15,'weight':'bold'}
#plt.rc('font', **font)
''''plt.xticks(rotation=90)
plt.plot(XMX_P, Throughput_P, label="PARALLEL GC",linewidth=2)
plt.plot(XMX_S, Throughput_S, label="SERIAL GC",linewidth=2)
plt.xlabel('XMX (PARALLEL GC & SERIAL GC)')
plt.ylabel('THROUGHPUT(%)')
plt.title('PERFORMANCE(THROUGHPUT) GRAPH')
plt.legend()
plt.show()'''
#font = {'size':15,'weight':'bold'}
#plt.rc('font', **font)
plt.xticks(rotation=90)
plt.plot(XMX_P, Latency_P, label="PARALLEL GC",linewidth=2)
plt.plot(XMX_S, Latency_S, label="SERIAL GC",linewidth=2)
plt.xlabel('XMX (PARALLEL GC & SERIAL GC)')
plt.ylabel('TIME(S)')
plt.title('PERFORMANCE(LATENCY) GRAPH')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(XMX_P, GC_P, label="PARALLEL GC",linewidth=2)
plt.plot(XMX_P, FULL_GC_P, label="PARALLEL FULL-GC",linewidth=2)
plt.plot(XMX_S, GC_S, label="SERIAL GC",linewidth=2)
plt.plot(XMX_S, FULL_GC_S, label="SERIAL FULL-GC",linewidth=2)
plt.xlabel('XMX (PARALLEL GC & SERIAL GC)')
plt.ylabel('GC/FULL-GC COUNT')
plt.title('GC AND FULL-GC COUNT GRAPH')
plt.legend()
plt.show()
'''plt.xticks(rotation=90)
plt.plot(XMX_P, GC_P, label="PARALLEL GC",linewidth=2)
plt.plot(XMX_S, GC_S, label="SERIAL GC",linewidth=2)
plt.xlabel('XMX (PARALLEL GC & SERIAL GC)')
plt.ylabel('GC COUNT')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(XMX_P, FULL_GC_P, label="PARALLEL GC",linewidth=2)
plt.plot(XMX_S, FULL_GC_S, label="SERIAL GC",linewidth=2)
plt.xlabel('XMX (PARALLEL GC & SERIAL GC)')
plt.ylabel('FULL GC COUNT')
plt.legend()
plt.show()'''