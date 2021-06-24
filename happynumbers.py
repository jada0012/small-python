
def happynum(num):
    total = []
    
    
    for i in num:
        total.append(int(i) ** 2)
    if sum(total) != 1:
        try:

            return happynum(str(sum(total)))
        except RecursionError:
           return 'not happy'
            
    else:
        
        return 'happy'
    

    
    
for i in range(100):
    print(i, happynum(str(i)))
#todo figure out how to return only happy numbers

