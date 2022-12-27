import csv
from csv import writer
#Dataset1 for prediction
fields_P = ['Throughput(%)','Latency(Max GC pause time)(s)','Application runtime(s)','FULL GC','GC','XMX']
filename_P = "dataset_P1.csv"
with open(filename_P, 'w') as csvfile_P:
    csvwriter_P = csv.writer(csvfile_P)
    csvwriter_P.writerow(fields_P)
n_f_P=2
#reading logfiles
for C_P in range(0, 178):
    fgc_P = 0
    gc_P = 0
    c_P = 1
    GC_FULL_GC_P = []
    YoungGen_allocated_space_P = []
    YoungGen_Before_GC_P = []
    YoungGen_After_GC_P = []
    Old_Gen_allocated_space_P = []
    Old_Gen_Before_GC_P = []
    Old_Gen_After_GC_P = []
    GC_Pause_Time_P=[]
    Real_P=[]
    CPU_Time_P= []
    User_P=[]
    Sys_P=[]
    #logfile name for reading
    f_name_P = "log_file_P/Xms2m_Xmx" + str(n_f_P) + "m_PGC.log"
    f_P = open(f_name_P)
    Lines_P = f_P.readlines()
    #reading lines in one logfile line by line
    for l_p in range(0,len(Lines_P)):
        temp1_P=Lines_P[l_p] #storing particular[l_p=line number] single line
        if "PSYoungGen" in temp1_P and "GC" in temp1_P:
            if "Marking Phase" in Lines_P[l_p - 10]: #checking for fullgc or gc
                fgc_P=fgc_P+1 #fullgc count
                c_P = 0 #initializing 0 for fullgc
            else:
                gc_P=gc_P+1 #gc count
                c_P = 1
            #print(temp1_P)
            temp2_P=temp1_P.split(": ") #splitting as string to store values in array
            #print(temp2_P)
            temp2_P=temp2_P[1]
            #print(temp2_P)
            temp2_P=temp2_P.split("K")
            #print(temp2_P)
            GC_FULL_GC_P.append(c_P)
            YoungGen_Before_GC_P.append(temp2_P[0])
            #print(temp2_P[0])
            #print(temp2_P[2])
            temp3_P=temp2_P[2].split(">")
            #print(temp3_P)
            YoungGen_After_GC_P.append(temp3_P[1])
            #print(temp3_P[1])
            #print(temp2_P[3])
            temp3_P=temp2_P[3].split("(")
            #print(temp3_P)
            YoungGen_allocated_space_P.append(temp3_P[1])
            #print(temp3_P[1])
        if "ParOldGen" in temp1_P and "GC" in temp1_P:
            temp2_P=temp1_P.split(": ")
            temp2_P=temp2_P[1]
            temp2_P = temp2_P.split("K")
            Old_Gen_Before_GC_P.append(temp2_P[0])
            temp3_P = temp2_P[2].split(">")
            Old_Gen_After_GC_P.append(temp3_P[1])
            temp3_P = temp2_P[3].split("(")
            Old_Gen_allocated_space_P.append(temp3_P[1])
        if ("Pause Young" in temp1_P or "Pause Full" in temp1_P) and "ms" in temp1_P:
            temp2_P = temp1_P.split("M) ")
            temp2_P=temp2_P[1].split("m")
            GC_Pause_Time_P.append(temp2_P[0])
        if "User" in temp1_P and "Sys" in temp1_P and "Real" in temp1_P:
            temp2_P=temp1_P.split("=")
            temp3_P=temp2_P[1].split("s ")
            temp4_P=temp3_P[0]
            temp3_P = temp2_P[2].split("s ")
            CPU_Time_P.append(float(temp4_P)+float(temp3_P[0]))
            User_P.append(float(temp4_P))
            Sys_P.append(float(temp3_P[0]))
            temp3_P = temp2_P[3].split("s")
            Real_P.append(temp3_P[0])

    rows_P = []
    Total_GC_Pause_Time_P=0
    Latency_P=0
    #merging as 2D array[[ , ] [, ]]
    for i_P in range(0, len(Real_P)):
        arr_P = []
        arr_P.append(YoungGen_allocated_space_P[i_P])
        arr_P.append(YoungGen_Before_GC_P[i_P])
        arr_P.append(YoungGen_After_GC_P[i_P])
        arr_P.append(Old_Gen_allocated_space_P[i_P])
        arr_P.append(Old_Gen_Before_GC_P[i_P])
        arr_P.append(Old_Gen_After_GC_P[i_P])
        arr_P.append(GC_Pause_Time_P[i_P])
        if Latency_P<float(GC_Pause_Time_P[i_P]):
            Latency_P=float(GC_Pause_Time_P[i_P])
        Total_GC_Pause_Time_P=Total_GC_Pause_Time_P+float(GC_Pause_Time_P[i_P])
        arr_P.append(User_P[i_P])
        arr_P.append(Sys_P[i_P])
        arr_P.append(Real_P[i_P])
        arr_P.append(CPU_Time_P[i_P])
        arr_P.append(GC_FULL_GC_P[i_P])
        rows_P.append(arr_P)
    #print(rows_P)
    stor_P = []
    #application runtime temp1_P
    temp1_P=Lines_P[len(Lines_P)-1]
    temp1_P=temp1_P.split("[")
    temp1_P = temp1_P[1].split("s")
    temp1_P=temp1_P[0]
    Total_GC_Pause_Time_P=Total_GC_Pause_Time_P/1000
    Throughput_P=Total_GC_Pause_Time_P/float(temp1_P)
    Throughput_P=Throughput_P*100
    Throughput_P=100-Throughput_P
    #storing of single logfile values as row into dataset1
    stor_P.append(Throughput_P)
    stor_P.append(Latency_P/1000)
    stor_P.append(temp1_P)
    stor_P.append(fgc_P)
    stor_P.append(gc_P)
    stor_P.append(n_f_P) #Maxheap size
    with open('dataset_P1.csv', 'a') as f_object_P:
        writer_object_P = writer(f_object_P)
        writer_object_P.writerow(stor_P)
        f_object_P.close()
    dataset_name_P = "dataset_P/Xms2m_Xmx"+str(n_f_P)+"m_PGC.csv" # csv file naming of each logfile
    # column names for single logfiles.csv
    fields_P = ['YoungGen (allocated space)(KB)', 'YoungGen (Before GC)(KB)',
                'YoungGen (After GC)(KB)', 'Old Gen(allocated space)(KB)', 'Old Gen (Before GC)(KB)',
                'Old Gen(After GC)(KB)', 'GC Pause Time(ms)', 'User(s)', 'Sys(s)', 'Real Time(s)', 'CPU Time(s)',
                'GC/FULL-GC(1->GC,0->FULL-GC)']
    with open(dataset_name_P, 'w') as csvfile_P:
        csvwriter_P = csv.writer(csvfile_P)
        csvwriter_P.writerow(fields_P)
        csvwriter_P.writerows(rows_P) #storing from 2D matrix
    #incrementing heapsize for file name
    if n_f_P==2:
        n_f_P=n_f_P+98
    else:
        n_f_P=n_f_P+100