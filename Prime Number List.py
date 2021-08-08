n = 100
prime_num = []
for i in range(1, n) :  
   if i > 1:  
       for ii in range(2,i):  
           if (i % ii) == 0:  
               break  
       else:
         prime_num.append(i)
print(prime_num)  