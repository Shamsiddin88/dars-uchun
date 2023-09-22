right_join=input("So'zlarni kiriting: ").split(' ')



for i in range (len(right_join)):
    if 'left' in right_join[i]:
        right_join[i] ='right'
        
def print_l(matn):
    print(matn)        
        
print_l(right_join)
