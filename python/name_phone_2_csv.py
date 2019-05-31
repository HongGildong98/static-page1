#Copyright 2019 돈키호테 
import csv

def read_names(fname):
    name_phone ={}
    with open(fname,"r") as f:
        for line in f:
            #print(line)
            line = line.strip().split(":")
            #print(line)
            name_phone[line[0].strip()] = line[1].strip()
 
        return name_phone

def write_csv(dic,fname):
    with open (fname+"_sort_by_name.csv",'w') as f:
        for i in range(len(dic)):
            name  = dic[i][0]
            phone  = str(dic[i][1])
            f.write(name+','+phone+'\n')

#main code block
file = read_names("name_phone.txt")
#print(file)
f_sort_by_name = sorted(file.items())
print(f_sort_by_name)
write_csv(f_sort_by_name,"name_phone")


 







































"""
           
def write_csv(dic,sort_type,fname,mode):
    if(sort_type==1):            #sort by name
        with open (fname+"sort_by_name.csv",mode) as f:
            for i in range(len(dic)):
                name  = dic[i][0]
                point  = str(dic[i][1])
                f.write(name+','+point+'\n')
                
    elif(sort_type==2):            #sort by name
        with open (fname+"sort_by_score.csv",mode) as f:
            for i in range(len(dic)):
                name  = dic[i][0]
                point  = str(dic[i][1])
                f.write(name+','+point+'\n')            
        
        
#main
ROTC = read_names("name_phone.txt")

f = read_points("ROTC.txt",ROTC)  
f_sort_by_name = sorted(f.items())
f_sort_by_point = sorted(f.items(),key = lambda t : t[1],reverse=True)
write_csv(f_sort_by_name,1,"ROTC","w")
write_csv(f_sort_by_point,2,"ROTC","w")
"""
