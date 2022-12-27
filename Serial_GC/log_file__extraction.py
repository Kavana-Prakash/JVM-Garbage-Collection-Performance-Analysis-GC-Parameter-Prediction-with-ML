import csv
from csv import writer
fields = ['Throughput(%)','Latency(Max GC pause time)(s)','Application runtime(s)','FULL GC','GC','XMX']
filename = "dataset.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
n_f=2
while n_f<17701:
    f_name="log_file/Xms2m_Xmx"+str(n_f)+"m_SGC.log"
    f = open(f_name)
    Lines = f.readlines()
    c = 1
    j = 0
    k = 0
    l = 0
    fgc = 0
    gc = 0
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
    sys=[]
    user=[]
    for line in Lines:
        if "DefNew" in line.strip():
            if "Phase 1: Mark live" in Lines[j - 7]:
                c = 0
                fgc = fgc + 1
            else:
                c = 1
                gc = gc + 1
            temp1 = line.strip()
            temp2 = ""
            flog = -1
            i = -1
            while (i < len(temp1)):
                if temp1[i - 1] == "[" and flog == -1:
                    flog = 0
                if flog == 0:
                    temp2 = temp2 + str(temp1[i])
                if flog == 0:
                    if temp1[i + 1] == "s":
                        temp2 = ""
                        flog = 1
                if temp1[i - 2] == "]" and temp1[i - 1] == " " and flog == 1:
                    flog = 2
                if flog == 2:
                    temp2 = temp2 + str(temp1[i])
                if flog == 2:
                    if temp1[i] == "C":
                        temp2 = ""
                        flog = 3
                if temp1[i - 3] == "w" and temp1[i - 2] == ":" and temp1[i - 1] == " " and flog == 3:
                    flog = 4
                if flog == 4:
                    temp2 = temp2 + str(temp1[i])
                if flog == 4:
                    if temp1[i + 1] == "K":
                        GC_FULL_GC.append(c)
                        DefNew_Before_GC.append(temp2)
                        temp2 = ""
                        flog = 5
                if temp1[i - 1] == "(" and flog == 5:
                    flog = 6
                if flog == 6:
                    temp2 = temp2 + str(temp1[i])
                if flog == 6:
                    if temp1[i + 1] == "K":
                        temp2 = ""
                        flog = 7
                if temp1[i - 1] == ">" and flog == 7:
                    flog = 8
                if flog == 8:
                    temp2 = temp2 + str(temp1[i])
                if flog == 8:
                    if temp1[i + 1] == "K":
                        DefNew_After_GC.append(temp2)
                        temp2 = ""
                        flog = 9
                if temp1[i - 1] == "(" and flog == 9:
                    flog = 10
                if flog == 10:
                    temp2 = temp2 + str(temp1[i])
                if flog == 10:
                    if temp1[i + 1] == "K":
                        DefNew_allocated_space.append(temp2)
                        temp2 = ""
                        flog = 11
                i = i + 1
        if "Tenured" in line.strip():
            temp1 = line.strip()
            temp2 = ""
            flog = -1
            i = -1
            while (i < len(temp1)):
                if temp1[i - 2] == ":" and flog == -1:
                    flog = 0
                if flog == 0:
                    temp2 = temp2 + str(temp1[i])
                if flog == 0:
                    if temp1[i + 1] == "K":
                        Tenured_Before_GC.append(temp2)
                        temp2 = ""
                        flog = 1
                if temp1[i - 1] == "(" and flog == 1:
                    flog = 2
                if flog == 2:
                    temp2 = temp2 + str(temp1[i])
                if flog == 2:
                    if temp1[i] == "K":
                        temp2 = ""
                        flog = 3
                if temp1[i - 1] == ">" and flog == 3:
                    flog = 4
                if flog == 4:
                    temp2 = temp2 + str(temp1[i])
                if flog == 4:
                    if temp1[i + 1] == "K":
                        Tenured_After_GC.append(temp2)
                        temp2 = ""
                        flog = 5
                if temp1[i - 1] == "(" and flog == 5:
                    flog = 6
                if flog == 6:
                    temp2 = temp2 + str(temp1[i])
                if flog == 6:
                    if temp1[i + 1] == "K":
                        Tenured_allocated_space.append(temp2)
                        temp2 = ""
                        flog = 7
                i = i + 1
        if "gc,cpu      " in line.strip():
            if "Pause Young" in Lines[j - 1] and "Pause Young" in Lines[j - 2]:
                DefNew_allocated_space.append(0)
                DefNew_Before_GC.append(0)
                DefNew_After_GC.append(0)
                Tenured_allocated_space.append(0)
                Tenured_Before_GC.append(0)
                Tenured_After_GC.append(0)
                GC_FULL_GC.append(0)
                fgc = fgc + 1
            if "Pause Young" in Lines[j - 1] and "Promotion failed" in Lines[j - 2]:
                DefNew_allocated_space.append(0)
                DefNew_Before_GC.append(0)
                DefNew_After_GC.append(0)
                Tenured_allocated_space.append(0)
                Tenured_Before_GC.append(0)
                Tenured_After_GC.append(0)
                GC_FULL_GC.append(0)
                fgc = fgc + 1
            temp1 = line.strip()
            temp2 = ""
            flog = -1
            i = -1
            while (i < len(temp1)):
                if temp1[i - 1] == "=" and flog == -1:
                    flog = 0
                if flog == 0:
                    temp2 = temp2 + str(temp1[i])
                if flog == 0:
                    if temp1[i + 1] == "s":
                        temp3 = float(temp2)
                        user.append(temp2)
                        User_Time.append(temp2)
                        temp2 = ""
                        flog = 1
                if temp1[i - 1] == "=" and flog == 1:
                    flog = 2
                if flog == 2:
                    temp2 = temp2 + str(temp1[i])
                if flog == 2:
                    if temp1[i + 1] == "s":
                        temp3 = temp3 + float(temp2)
                        sys.append(temp2)
                        CPU_Time.append(temp3)
                        System_Time.append(temp2)
                        temp2 = ""
                        flog = 3
                if temp1[i - 1] == "=" and flog == 3:
                    flog = 4
                if flog == 4:
                    temp2 = temp2 + str(temp1[i])
                if flog == 4:
                    if temp1[i + 1] == "s":
                        Real_Time.append(temp2)
                        temp2 = ""
                        flog = 5
                i = i + 1
        if "Pause Young" in line.strip():
            if k % 2 == 1:
                temp1 = line.strip()
                temp2 = ""
                flog = -1
                i = -1
                while (i < len(temp1)):
                    if temp1[i - 1] == " " and temp1[i - 3] == "M" and flog == -1:
                        flog = 0
                    if flog == 0:
                        temp2 = temp2 + str(temp1[i])
                    if flog == 0:
                        if temp1[i + 1] == "m":
                            GC_Pause_Time.append(temp2)
                            temp2 = ""
                            flog = 1
                    i = i + 1
            k = k + 1
        if "Pause Full" in line.strip():
            if l % 2 == 1:
                temp1 = line.strip()
                temp2 = ""
                flog = -1
                i = -1
                while (i < len(temp1)):
                    if temp1[i - 1] == " " and temp1[i - 3] == "M" and flog == -1:
                        flog = 0
                    if flog == 0:
                        temp2 = temp2 + str(temp1[i])
                    if flog == 0:
                        if temp1[i + 1] == "m":
                            GC_Pause_Time.append(temp2)
                            temp2 = ""
                            flog = 1
                    i = i + 1
            l = l + 1
        j = j + 1
    fields = ['DefNew (allocated space)(KB)', 'DefNew (Before GC)(KB)',
              'DefNew (After GC)(KB)', 'Tenured (allocated space)(KB)', 'Tenured (Before GC)(KB)',
              'Tenured (After GC)(KB)', 'GC Pause Time(ms)','User(s)','Sys(s)','Real Time(s)', 'CPU Time(s)', 'GC/FULL-GC(1->GC,0->FULL-GC)']
    rows = []
    m = 0
    s = 0
    for i in range(0, len(DefNew_allocated_space)):
        arr = []

        arr.append(DefNew_allocated_space[i])
        arr.append(DefNew_Before_GC[i])
        arr.append(DefNew_After_GC[i])
        arr.append(Tenured_allocated_space[i])
        arr.append(Tenured_Before_GC[i])
        arr.append(Tenured_After_GC[i])
        if float(GC_Pause_Time[i]) > float(m):
            m = GC_Pause_Time[i]
        s = s + float(GC_Pause_Time[i])
        arr.append(GC_Pause_Time[i])
        arr.append(user[i])
        arr.append(sys[i])
        arr.append(Real_Time[i])
        arr.append(CPU_Time[i])
        arr.append(GC_FULL_GC[i])
        rows.append(arr)
    dataset_name = "dataset/Xms2m_Xmx" + str(n_f) + "m_SGC.csv"
    filename = dataset_name
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    temp1 = Lines[len(Lines) - 1]
    temp2 = ""
    flog = -1
    i = -1
    while (i < len(temp1)):
        if temp1[i - 1] == "[" and flog == -1:
            flog = 0
        if flog == 0:
            temp2 = temp2 + str(temp1[i])
        if flog == 0:
            if temp1[i + 1] == "s":
                flog = 1
        i = i + 1
    s = s / 1000
    s = s / float(temp2)
    s = s * 100
    s = 100 - s
    stor = []
    m = float(m) / 1000
    stor.append(s)
    stor.append(m)
    stor.append(temp2)
    stor.append(fgc)
    stor.append(gc - 1)
    stor.append(n_f)
    with open('dataset.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(stor)
        f_object.close()
    if n_f==2:
        n_f=n_f+98
    else:
        n_f=n_f+100