import random
#simulation of a vote.
def donneesVote(l):
    y=0
    for i in range(len(l)):
        y+=l[i]
    if y%2==0:
        z=(y/2)+1
    else:
        z=(y+1)/2
    return (y,z)

def gagnantMajAbsolue(l,c): #highest number of votes
    p=c-1
    y,z=donneesVote(l)
    if l[p]> =z:
        return True
    else:
        return False

def eluTour1(l): #first round results
    for i in range(len(l)):
        if gagnantMajAbsolue(l,(i+1)):
            return (i+1)
    return 0

def candidats2ndtour(l): #candidates moving on to second round
    c=l.index(max(l))
    c+=1
    l2=l[:]
    l2.remove(max(l))
    y=l2.index(max(l2))
    y+=1
    return (c,y)

def generationVote(nbC,nbV):
    y=nbV
    l=list(range(nbC))
    for i in range (len(l)-1):
        l[i]=random.randint(0,y)
        y-=l[i]
    l[len(l)-1]=y
    return l
def testVote(l):
    l2=l[:]
    l2.remove(max(l))
    if (l.count(max(l))>1) or (l.count(max(l2))>1):
        return False
    else:
        return True
        
#simulation of vote
nbC=int(input("saisir nombre total de candidats"))
nbV=int(input("saisir nombre total de votes"))
l=generationVote(nbC,nbV)
print("votes du premier tour")
for i in range (len(l)):
    print("candidats", i+1,":", l[i] ,end="\n")
if eluTour1(l)!=0:
    print("le candidat elu au 1 er tour de l'election est le numero", eluTour1(l))
else:
    c,d=candidats2ndtour(l)
    print("Candidats pouvant se presenter au 2 nd tour :", c, d)
    print("votes du second tour:")
    l2=generationVote(2,nbV)
    print("candidat", c ,":", l[0] ,end="\n")
    print("candidat", d ,":", l[1] ,end="\n")
    if l2[0]>l2[1]:
        print("le candidat elu au second tour est le numero",c)
    else:
        print("le candidat elu au second tour est le numero",d)
def lecture(fichier):
    dic={}
    v=open("fichier","r")
    z=v.readlines()
    v.close()
    for i in range (len(z)):
        z2=z[i].split(" ")
        if z2[4] in [0,1,2,3,4,5,6,7,8,9]:
            dic[z2[2]]=z2[4:]
        else:
            dic[z2[2]+z2[3]]=z2[5:]
    return dic

def creerliste(dic):
    l1=[]
    l2=list(dic)
    for e in l2:
        l1.append(dic[e])

dic1=lecture("electionTour1.txt")
dic2=lecture("electionTour2.txt")








