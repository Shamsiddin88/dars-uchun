# # with open ("alifbo.txt", "w") as alpha:
# #     for i in range(0, 26):
# #         alpha.write (chr (i+65) + chr (i+97)+" ")

# with open ("karta.txt", "r") as file:
#     sanoq=0
#     for i in file.readlines():
#         if 'Ruble' in i:
#             sanoq+=1
# print(sanoq)



# with open ("fayl.txt", "r") as file:
#     ls=file.read().split(" ")

#     toq=open("toq.txt", "w")
#     juft=open("juft.txt", "w")
#     for i in ls:
#         if i:
#             if  int(i) % 2==0:
#                 juft.write(i+' ')
#             else:
#                 toq.write(i+' ')
            
        

# with open ("fayl.txt", "r") as file:
#     ls=file.read().split(" ")

#     toq=open("toq.txt", "w")
#     juft=open("juft.txt", "w")
#     for i in ls:
#         if i:
#             if  len(i)%2==1 and i[0].isupper():
#                 toq.write(i+' ')
#             elif len(i)%2==0 and i[0].islower():
#                 juft.write(i+' ')
            
# juft.close()
# toq.close()


# with open ("fayl.txt", "r") as file:
#         for i in file.readlines():
#             i=i.replace("\n", " ").split(',')
#             email=i[3].split('.')
#             print("e-mail=> ", i[3], "domen=>", email[1])




# with open ("raqamlar.txt", "r") as file:
#     number=[]
#     for i in file.readlines():
#             i=i.replace("\n", " ").split(' ')
#             number.append(i[2]+i[3]+i[4])
#             print(i[1])

#     for i in range (len(number)):
#             for j in range (len(number)):
#                 if not number[int(i)]==number[int(j)]:
#                     print(number[j])
            
            
# res={}            
# davlat=set()
# lssort=set()
# son='0123456789'
                                                                                            
# file=open ("karta.txt", "r")
# ls=file.readlines()
# for i in ls:
#     i=i.replace("\n", "").split(',')
#     davlat.add(i[-1])
#     if i[1]=='visa':
#         lssort.add(i[-1])
# country=list(davlat)
# lssort=list(lssort)
# lssort.sort()
    
# for i in country:
#     file.seek(0)
#     res[i]=file.read().count(i)
# print("\n1-topshiriq=>\n", res)
# print("\n2-topshiriq=>\n",lssort)
    
# for i in ls:
#     i=i.replace("\n", "").split(',')
#     h=0
#     for j in son:
#         if j in i[0]:
#             h+=1
#         if h==10:
#             print(i[0], i[-1], i[-4], i[-2])







# file.close()


# p={}
# davn=set()
# file = open("karta.txt", "r")
# ar=file.readlines()
# for i in ar:
#     i= i.replace("\n", "").split(",")
#     davn.add(i[-1])
# tot=list(davn)
# for i in tot:
#     file.seek(0)
#     p[i]=file.read().count(i)
# print(p)
# file.close()
                   


# try:
#     number = set()
#     with open ("raqamlar.txt", "r") as file:
#         ls=file.readline()
#         for i in ls:
#             i=i.replace("\n", "").split(" ")
#             if not ls[1] in number:
#                 print(ls)
#                 number.add(ls[1])
           
       
# except Exception as f:
#     print(f)


# try:
    
#     with open ("masala.txt","r") as file:
#         ls=file.readlines()
#         for i in ls:
#             i=i.replace("\n", "").split(",")
#             sana=i[4].split(".")
#             print(sana[1])
            
        

# except Exception as f:
#     print(f)


# soz=input ("Soz kiriting: ").upper()
# morze_alifbosi = {
#         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
#         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
#         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
#         '9': '----.', '0': '-----',
#         '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
#         ')': '-.--.-', '&': '.-...',
#         ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
#         '$': '...-..-', '@': '.--.-.',
#         ' ': '/'
#     }
# tekst=''
# for i in soz:
#     tekst+=morze_alifbosi.get(i)
# print (tekst)



     
# car=set()
# mashina={}                     
# with open ("mashina.txt", "r") as file:
#         ls=file.readlines()
#         for i in ls:
#             i=i.replace("\n", "").split(',')
#             car.add(i[4])
#             cars=list(car)
         
#         for i in cars:
#             file.seek(0)
#             mashina[i]=file.read().count(i)
# print(mashina)   
# max_brand = max(mashina, key=mashina.get)         
# print(max_brand, max(mashina.values()))       

# print(dir(str))


