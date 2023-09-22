
car=set()
mashina={}                     
with open ("mashina.txt", "r") as file:
        ls=file.readlines()
        for i in ls:
            i=i.replace("\n", "").split(',')
            car.add(i[4])
            cars=list(car)
         
        for i in cars:
            file.seek(0)
            mashina[i]=file.read().count(i)
print(mashina)   
        
print(max(mashina.values()))       
max_brand = max(mashina, key=mashina.get) 
print(max_brand)