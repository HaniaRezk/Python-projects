def nbrechiffre(n):
    ch=str(n)
    return(len(ch))
def sommepuissance(n,p):
    ch=str(n)
    i=0
    y=0
    while i< len(ch):
        z=eval(ch[i])
        y+=z**p
        i+=1
    return (y)
def armstrong(n): #amstrong number
    q=0
    y=-1
    while q<n:
         if sommepuissance(n,q)==n:
             y=q
         q=q+1
    if y==-1:
        return (False)
    else:
        return (True)
    print(y)

def narcissique(n): #narcissistique number
    if sommepuissance(n,nbrechiffre(n))==n:
        y=True
    else:
        y=False
    return (y)
x=1000
while x>0:
    if armstrong(x):
        print("le nombre",x,"est un nombred'armstrong'")
        if narcissique(x):
            print("le nombre est aussi narcissique")
    x=x-1
n=500
while n>0:
    if narcissique(n):
        print(n)
    n=n-1
