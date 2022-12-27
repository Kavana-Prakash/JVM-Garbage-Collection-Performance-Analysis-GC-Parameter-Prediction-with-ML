import csv
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
root_P = tk.Tk()
root_P.withdraw()
file_path_P= filedialog.askopenfilename()
f_P = open(file_path_P)
csvreader_P = csv.reader(f_P)
header_P = []
header_P = next(csvreader_P)
rows_P = []
for row_P in csvreader_P:
    if len(row_P)>0:
        rows_P.append(row_P)
GC_FULL_P=[]
GC_Pause_Time_P=[]
Before_GC_P=[]
After_GC_P=[]
num_P=[]
User_P=[]
Sys_P=[]
GC_Nubmer_P=[]
Real_P=[]
CPU_Time_P=[]
Sys_P=[]
User_P=[]
for i_P in range(0,len(rows_P)):
    num_P.append(i_P)
    if int(rows_P[i_P][11])==0:
        GC_FULL_P.append("FULL GC")
    else:
        GC_FULL_P.append("GC")
    GC_Pause_Time_P.append(rows_P[i_P][6])
    Before_GC_P.append(int(rows_P[i_P][1])+int(rows_P[i_P][4]))
    After_GC_P.append(int(rows_P[i_P][2])+int(rows_P[i_P][5]))
    Real_P.append(float(rows_P[i_P][9]))
    CPU_Time_P.append(float(rows_P[i_P][10]))
    Sys_P.append(float(rows_P[i_P][8]))
    User_P.append(float(rows_P[i_P][7]))

file_path=file_path_P.split("PGC")
file_path=str(file_path[0])+"SGC.csv"
file_path=file_path.split("dataset_P")
file_path="dataset_S"+file_path[1]
f = open(file_path)
csvreader = csv.reader(f)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    if len(row)>0:
        rows.append(row)
print(rows)

GC_FULL=[]
GC_Pause_Time=[]
Before_GC=[]
After_GC=[]
num=[]
User=[]
Sys=[]
GC_Nubmer=[]
Real=[]
CPU_Time=[]
Sys=[]
User=[]
for i in range(0,len(rows)):
    num.append(i)
    if int(rows[i][11])==0:
        GC_FULL.append("FULL GC")
    else:
        GC_FULL.append("GC")
    GC_Pause_Time.append(rows[i][6])
    Before_GC.append(int(rows[i][1])+int(rows[i][4]))
    After_GC.append(int(rows[i][2])+int(rows[i][5]))
    Real.append(float(rows[i][9]))
    CPU_Time.append(float(rows[i][10]))
    Sys.append(float(rows[i][8]))
    User.append(float(rows[i][7]))


file_path=file_path.split("Xmx")
file_path=file_path[1].split("m")
print(file_path[0])



'''plt.xticks(rotation=90)
plt.plot(GC_Pause_Time_P, GC_FULL_P,label="Parallel GC")
plt.plot(GC_Pause_Time, GC_FULL,label="Serial GC")
plt.xlabel('GC Pause Time(ms)')
plt.ylabel('GC/FULL-GC')
plt.title('Frequency Graph')
plt.legend()
plt.show()'''
#font = {'size':15,'weight':'bold'}
#plt.rc('font', **font)
plt.plot(num_P, GC_FULL_P,label="PARALLEL GC",linewidth=2)
plt.plot(num, GC_FULL,label="SERIAL GC",linewidth=2)
plt.xlabel('GC NUMBER(XMX='+str(file_path[0])+')')
plt.ylabel('GC/FULL-GC')
plt.title('FREQUENCY GRAPH')
plt.legend()
plt.show()

plt.xticks(rotation=90)
plt.plot(num_P, Before_GC_P,label="PARALLEL GC",linewidth=2)
plt.plot(num, Before_GC,label="SERIAL GC",linewidth=2)
plt.xlabel('GC NUMBER(XmX='+str(file_path[0])+')')
plt.ylabel('MEMORY(KB)')
plt.title('HEAP USAGE(BEFORE GC) GRAPH')
plt.legend()
plt.show()


plt.xticks(rotation=90)
plt.plot(num_P, After_GC_P,label="PARALLEL GC",linewidth=2)
plt.plot(num, After_GC,label="SERIAL GC",linewidth=2)
plt.xlabel('GC NUMBER(XMX='+str(file_path[0])+')')
plt.ylabel('MEMORY(KB)')
plt.title('HEAP USAGE(AFTER GC) GRAPH')
plt.legend()
plt.show()

#font = {'size':15,'weight':'bold'}
#plt.rc('font', **font)
plt.plot(num_P, Real_P,label="PARALLEL GC REAL TIME(S)",linewidth=2)
plt.plot(num_P, CPU_Time_P,label="PARALLEL GC CPU TIME(S)",linewidth=2)
plt.plot(num, Real,label="SERIAL GC REAL TIME(S)",linewidth=2)
plt.plot(num, CPU_Time,label="SERIAL GC CPU TIME(S)",linewidth=2)
plt.xlabel('GC NUMBER(XMX='+str(file_path[0])+')')
plt.ylabel('TIME(S)')
plt.title('CPU AND REAL TIME GRAPH')
plt.legend()
plt.show()


#font = {'size':15,'weight':'bold'}
#plt.rc('font', **font)
plt.plot(num_P, Sys_P,label="PARALLEL GC SYS TIME(S)",linewidth=2)
plt.plot(num_P, User_P,label="PARALLEL GC USER TIME(S)",linewidth=2)
plt.plot(num, Sys,label="SERIAL GC SYS TIME(S)",linewidth=2)
plt.plot(num, User,label="SERIAL GC USER TIME(S)",linewidth=2)
plt.xlabel('GC NUMBER(XMX='+str(file_path[0])+')')
plt.ylabel('TIME(S)')
plt.title('SYSTEM AND USER TIME GRAPH')
plt.legend()
plt.show()