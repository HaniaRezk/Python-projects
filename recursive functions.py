        # TP N° 1
import time 

    # FACTORIELLE
def factIt(n):
    x = 1 
    if n<2 : 
        return 1
    while n>1 : 
        x = x*n
        n = n-1
    return x
        
    
def factRec(n): 
    if n<2: 
        return 1
    else : 
        return n*factRec(n-1)
      
    # FIBONACCI
def fibo_rec(n) : 
    if n<2 : 
        return n
    else : 
        return fiboRec(n-1) + fiboRec(n-2)

def fibo_it(n) : 
    if n==0 : 
        return 0
    else : 
        x,y = 0,1
        for i in range (2,n+1):
            temp = y + x
            x = y
            y = temp
        return y
        
def fibo_smart_rec_aux(n) : 
    if n<2 : 
        return (n,n)
    elif n==2 :
        return (1,1)
    else : 
        (x1,x2) = fibo_smart_rec_aux(n-1)
        x = x1 + x2
        return (x,x1)
        
def fibo_smart_rec(n) :
    (x,y) = fibo_smart_rec_aux(n)
    return x
            
a=10

tmps1 = time.perf_counter()
a1 = fibo_it(a)

tmps2 = time.perf_counter()
a2 = fibo_rec(a)

tmps3 = time.perf_counter()
a3 = fibo_smart_rec(a)
#tmps4 = time.perf_counter()

print ("Pour a = ", a, "\nFibo itérative : ",a1, " Temps : ", tmps1, "\nFibo reccursive : ",a2, " Temps : ", tmps2, "\nFibo smart recursive : ",a3, " Temps : ",tmps3)
print("\n\n")

    #PUISSANCES 
m1,m2,m3 = 0,0,0
def puissance_it(n,p) : 
    global m1
    if p==0 : 
        return 1
    if p==1 : 
        return 1
    else : 
        x=1
        for i in range (p) :
            m1+=1 
            x = x*n
        return  x

def puissance_rec(n,p) : 
    global m2
    if p==0 : 
        return 1
    if p==1 : 
        return n
    else : 
        m2+=1
        return n*puissance_rec(n,p-1)
        
def puissance_rec_mieux(n,p) :
    global m3
    if p==0 : 
        return 1
    if p==1 : 
        return n
    if p%2==0 : 
        m3=+1
        return (puissance_rec_mieux(n,p/2))**2
    else : 
        m3+=1
        return n*(puissance_rec_mieux(n,p//2))**2
n,p = 2,9
print(n, "puissance " ,p)
print( "Iterative : ", puissance_it(n,p), "Mult : ", m1)
print( "Recursive : ", puissance_rec(n,p), "Mult : ", m2)
print( "Recursive mieux : ", puissance_rec_mieux(n,p), "Mult : ", m3)

     
