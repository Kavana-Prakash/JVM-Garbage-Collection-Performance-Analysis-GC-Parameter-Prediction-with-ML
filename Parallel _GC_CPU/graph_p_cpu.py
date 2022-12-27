import csv
import matplotlib.pyplot as plt
XMX=[]
Throughput=[]
Latency=[]
Application_runtime=[]
FULL_GC=[]
GC=[]
for cpu_n in range(1,9):
    file_P = open('dataset_P_'+str(cpu_n)+'.csv')
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
    for i_P in range(0,len(rows_P)):
        XMX_P.append(int(rows_P[i_P][5]))
        Throughput_P.append(float(rows_P[i_P][0]))
        Latency_P.append(float(rows_P[i_P][1]))
        Application_runtime_P.append(float(rows_P[i_P][2]))
        FULL_GC_P.append(int(rows_P[i_P][3]))
        GC_P.append(int(rows_P[i_P][4]))
    XMX.append(XMX_P)
    Throughput.append(Throughput_P)
    Latency.append(Latency_P)
    Application_runtime.append(Application_runtime_P)
    FULL_GC.append(FULL_GC_P)
    GC.append(GC_P)
x=[]
L_y1=[]
L_y2=[]
L_y3=[]
L_y4=[]
L_y5=[]
L_y6=[]
L_y7=[]
L_y8=[]
for i in range(0,6):
    x.append(XMX[0][i])
    L_y1.append(Latency[0][i])
    L_y2.append(Latency[1][i])
    L_y3.append(Latency[2][i])
    L_y4.append(Latency[3][i])
    L_y5.append(Latency[4][i])
    L_y6.append(Latency[5][i])
    L_y7.append(Latency[6][i])
    L_y8.append(Latency[7][i])


plt.plot(x, L_y1, label="1 CPU",linewidth=2)
plt.plot(x, L_y2, label="2 CPU",linewidth=2)
plt.plot(x, L_y3, label="3 CPU",linewidth=2)
plt.plot(x, L_y4, label="4 CPU",linewidth=2)
plt.plot(x, L_y5, label="5 CPU",linewidth=2)
plt.plot(x, L_y6, label="6 CPU",linewidth=2)
plt.plot(x, L_y7, label="7 CPU",linewidth=2)
plt.plot(x, L_y8, label="8 CPU",linewidth=2)
plt.xlabel('XMX (PARALLEL GC)')
plt.ylabel('TIME(S)')
plt.title('PERFORMANCE GRAPH')
plt.legend()
plt.show()

