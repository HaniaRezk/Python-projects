import time
def liste(n):
    l=[]
    while n>0:
        l.append(n%10)
        n=n//10
    return l

def multiplication_naive(n,p): #simple multiplication
    compteur=0
    l=liste(n)
    z=liste(p)
    fl=1
    fz=1
    resultat=0
    for i in l:
        i=i*fl
        for e in z:
            e=e*fz
            resultat+=i*e
            fz=fz*10
            compteur+=3
        fl=fl*10
        compteur+=2
        fz=1
    return resultat, compteur

compteur=0

def Karatsuba(x,y): #karatsuba algorithm
    minimum=min(x,y)
    global compteur
    n=len(liste(minimum))
    k=n//2
    if k==0:
        return x*y
    a=x//(10**k)
    b=x%(10**k)
    c=y//(10**k)
    d=y%(10**k)

    ac=Karatsuba(a,c)
    bd=Karatsuba(b,d)
    membre3=(-Karatsuba(a-b,c-d))+ac+bd
    compteur+=3

    return ac*(10**(k*2))+bd+membre3*(10**k)

s1=time.time()
multiplication_naive(500,400)
e1=time.time()
s2=time.time()
Karatsuba(500,400)
e2=time.time()

print("le temps pris pas la multiplication naive est", e1-s1, "et celui prit par karasuba est", e2-s2,"\n")
z,o1=multiplication_naive(500,400)
print("le nbre d'operation par mulriplication naive est", o1, "celui par karasuba est", compteur)

#cet algo multiplie a et b
def algo(a,b) :
    c = 0
    while b>0 :
        if b%2!=0 :
            c = c+a
            print("c=",c)

        a = 2*a
        b = b//2
        print("b=",b, "a=", a)
    return c



def virus(tab): #propagation of virus in a square
    v, h = 0, 0
    new = []
    for i in range(len(tab)):
            new.append(tab[i])
    for i in range (len(tab)):
        for j in range(len(tab[i])):

            if i==0 :
                if j==0 :
                    if tab[0][1] == 1 : h +=1
                    if tab[1][0] == 1 : v +=1
                elif j==len(tab[i])-1 :
                    if tab[0][j-1] == 1 : h +=1
                    if tab[1][j]   == 1 : v +=1
                else :
                    if tab[i][j+1] == 1 : h +=1
                    if tab[i][j-1] == 1 : h +=1
                    if tab[i+1][j] == 1 : v +=1

            elif i==len(tab)-1 :
                if j==0 :
                    if tab[i][1]   == 1 : h +=1
                    if tab[i-1][0] == 1 : v +=1
                elif j==len(tab[i])-1 :
                    if tab[i][j-1] == 1 : h +=1
                    if tab[i-1][j] == 1 : v +=1
                else :
                    if tab[i][j+1] == 1 : h +=1
                    if tab[i][j-1] == 1 : h +=1
                    if tab[i-1][j] == 1 : v +=1
            else :
                if j==0 :
                    if tab[i][1]   == 1 : h +=1
                    if tab[i-1][0] == 1 : v +=1
                elif j==len(tab[i])-1 :
                    if tab[i][j-1] == 1 : h +=1
                    if tab[i-1][j] == 1 : v +=1
                else :
                    if tab[i][j+1] == 1 : h +=1
                    if tab[i][j-1] == 1 : h +=1
                    if tab[i-1][j] == 1 : v +=1
                    if tab[i+1][j] == 1 : v +=1
            if h + v > 1 : new[i][j] = 1
            h, v = 0, 0
    return new



