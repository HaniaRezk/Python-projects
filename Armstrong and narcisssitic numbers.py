def miniscules():
    return"abcdefghijklmnopqrstuvwxyz"
def majusscules():
    return"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def nblettresmin(ch):
    i=0
    j=0
    ch2=miniscules()
    while i<len(ch):
        if ch[i] in ch2:
            j=j+1
        i=i+1
    return(j)
def nbrecarac(ch):
    z=0
    i=0
    ch1=miniscules()
    ch2=majusscules()
    while i<len(ch):
        if ch1.count(ch[i])==0:
            if ch2.count(ch[i])==0:
                z=z+1
        i=i+1
    return(z)
def nblettresmaj(ch):
    i=0
    y=0
    ch2=majusscules()
    while i<len(ch):
        if ch[i] in ch2:
            y=y+1
        i=i+1
    return(y)
def bonus(ch):
    bons=len(ch)*4
    if nblettresmin(ch)>0:
        bons+=(len(ch)-nblettresmin(ch))*3
    if nblettresmaj(ch)>0:
        bons+=(len(ch)-nblettresmaj(ch))*2
    if nbrecarac(ch)>0:
        bons+=nbrecarac(ch)*5
    return(bons)
def pluslonguemin(ch):
    ch1=miniscules()
    i=0
    z=0
    while i<len(ch):
        if ch[i] in ch1:
            z=z+1
        else:
            z=0
        i=i+1
    return(z)
def pluslonguemax(ch):
    ch1=majusscules()
    i=0
    z=0
    while i<len(ch):
        if ch[i] in ch1:
            z=z+1
        else:
            z=0
        i=i+1
    return(z)
def malus(ch):
    mal=pluslonguemax(ch)*3+pluslonguemin(ch)*2
    return(mal)
ch=input('saisir une chaine de caractere')
x=bonus(ch)-malus(ch)
if x>=80:
    print('tres fort')
elif x>=40:
    print('fort')
elif x>=20:
    print('faible')
else:
    print('tres faible')