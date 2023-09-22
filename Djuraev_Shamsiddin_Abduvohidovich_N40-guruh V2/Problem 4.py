
with open ('Tovarlar.txt', 'r') as file, open ('Aharfli.txt', 'w') as afile, open ('Kharfli.txt', 'w') as kfile :
    ls = file.readlines()
 
    arr=[]
    for i in range(len(ls)):
        arr=ls[i].split(' ')
        
    for i in arr:
        if 'a' or 'A' in i:
            afile.write(i)
        elif 'k' or 'K' in i:
            kfile.write(i)
        

    




