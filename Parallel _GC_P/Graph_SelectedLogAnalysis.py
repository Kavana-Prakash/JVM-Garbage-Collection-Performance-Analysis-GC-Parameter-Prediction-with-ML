import csv
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
root_P = tk.Tk() #helps to display root window & manages all other components of tkinter application
root_P.withdraw() #hides the window without destroying it internally
file_path_P= filedialog.askopenfilename() #display open file dialog that allows users to select one file.
f_P = open(file_path_P)
csvreader_P = csv.reader(f_P)
header_P = []
header_P = next(csvreader_P)
rows_P = []
for row_P in csvreader_P:
    #print(row_P)
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
Sys_p=[]
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
    Sys_p.append(float(rows_P[i_P][8]))
    User_P.append(float(rows_P[i_P][7]))

plt.xticks(rotation=90)
plt.plot(GC_Pause_Time_P, GC_FULL_P)
plt.xlabel('GC Pause Time(ms)')
plt.ylabel('GC/FULL-GC')
plt.title('Frequency Graph')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(num_P, Before_GC_P)
plt.xlabel('GC NUMBER')
plt.ylabel('Before GC(KB)')
plt.title('Heap Usage(before GC) Graph')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(num_P, After_GC_P)
plt.xlabel('GC NUMBER')
plt.ylabel('After GC(KB)')
plt.title('Heap Usage(After GC) Graph')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(num_P, Real_P,label=header_P[9])
plt.plot(num_P, CPU_Time_P,label=header_P[10])
plt.xlabel('GC NUMBER')
plt.ylabel('Time(s)')
plt.legend()
plt.show()
plt.xticks(rotation=90)
plt.plot(num_P, Sys_p,label=header_P[8])
plt.plot(num_P, User_P,label=header_P[7])
plt.xlabel('GC NUMBER')
plt.ylabel('Time(s)')
plt.legend()
plt.show()