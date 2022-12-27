import pandas as pd
import csv

data_P = pd.read_csv("dataset_P.csv")
Throughput_P=data_P['Throughput(%)']
Latency_P=data_P['Latency(Max GC pause time)(s)']
Application_runtime_P=data_P['Application runtime(s)']
FULL_GC_P=data_P['FULL GC']
GC_P=data_P['GC']
XMX_P=data_P['XMX']


data_S = pd.read_csv("dataset_S.csv")
Throughput_S=data_S['Throughput(%)']
Latency_S=data_S['Latency(Max GC pause time)(s)']
Application_runtime_S=data_S['Application runtime(s)']
FULL_GC_S=data_S['FULL GC']
GC_S=data_S['GC']
XMX_S=data_S['XMX']


fields = ['Throughput(%)','Latency(Max GC pause time)(s)','Type of GC(0->parllal,1->serial)','Application runtime(s)','FULL GC','GC','XMX']
rows = []
for i in range(0, len(Throughput_P)):
    arr = []
    arr.append(Throughput_P[i])
    arr.append(Latency_P[i])
    arr.append(0)
    arr.append(Application_runtime_P[i])
    arr.append(FULL_GC_P[i])
    arr.append(GC_P[i])
    arr.append(XMX_P[i])
    rows.append(arr)

for i in range(0, len(Throughput_S)):
    arr = []
    arr.append(Throughput_S[i])
    arr.append(Latency_S[i])
    arr.append(1)
    arr.append(Application_runtime_S[i])
    arr.append(FULL_GC_S[i])
    arr.append(GC_S[i])
    arr.append(XMX_S[i])
    rows.append(arr)
dataset_name = "daset_P_S.csv"
with open(dataset_name, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)



