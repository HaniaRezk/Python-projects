import os
#creating a library according to books and authors and quantities

titres=['Les miserables','Le pere Goriot',"Fables","L’amant","La peste","Du contrat social","Le grand Meaulnes","Notre-Dame de Paris","Les mandarins","Les contemplations","L’etranger"]

auteurs=["Victor Hugo","Honore de Balzac ","Jean de la Fontaine","Marguerite Duras ","Albert Camus","Jean-Jacques Rousseau","Alain Fournier","Victor Hugo","Simone de Beauvoir","Victor Hugo","Albert Camus "]

stocks=[5,0,1,2,2,3,0,4,1,0,6]

def ajout(titres,auteurs,stocks): #adding a book to a library
    s=input("quel est le titre du nouveau livre?")
    z=input("quel est l'auteur' du nouveau livre?")
    y=int(input("combien d'exmplaires du nouveau livre?"))
    titres.append(s)
    auteurs.append(z)
    stocks.append(y)
    return(titres, auteurs, stocks)

def stockparlivre(titres,auteurs,stocks, titre): #print how many copies available of a certain book.
    for i in range (len(titres)):
        if titres[i]==titre:
            return(stocks[i])
    return(-1)

def rechparauteurs(titres,auteurs,stocks, auteur): #look for a book according to author.
    l=[]
    for i in range (len(auteurs)):
        if auteurs[i]==auteur:
            if stocks[i]>0:
                l.append(titres[i])
    return(l)

def acheter(titres,auteurs,stocks): #Customer tries to buy a book.
    l=[]
    x=[]
    for i in range (len(auteurs)):
        if stocks[i]==0:
            l.append(titres[i])
            x.append(auteurs[i])
    print("les livres a acheter:")
    for i in range (len(l)):
        print('"', l[i], '"', end='')
        if x[i][0]==("A") or  (x[i][0]=="H"):
            print(" d' ", end="")
        else:
            print(" de ", end='')
        print(x[i], end='\n')

def leplus(auteurs,stocks):
    auteurs2=auteurs[:]
    stocks2=stocks[:]
    i=0
    while i<(len(auteurs2)):
        z=i+1
        while z<len(auteurs2):
            if auteurs2[i]==auteurs2[z]:
                stocks2[i]=stocks2[i]+stocks2[z]
                stocks2.pop(z)
                auteurs2.pop(z)
            else:
                z+=1
        i+=1
    c=-4
    print(stocks2)
    for i in range(len(stocks2)):
        if stocks2[i]>c:
            c=stocks2[i]
            nom=auteurs2[i]
    print("la bibliotheque possede:")
    print(c,"ouvrage(s) de l'auteur", nom)
    auteurs2.remove(nom)
    stocks2.remove(c)
    c=-1
    for i in range(len(auteurs2)):
        if stocks2[i]>c:
            c=stocks2[i]
            nom=auteurs2[i]
    print(c,"ouvrage(s) de l'auteur", nom)
    auteurs2.remove(nom)
    stocks2.remove(c)
    c=-1
    for i in range(len(auteurs2)):
        if stocks2[i]>c:
            c=stocks2[i]
            nom=auteurs2[i]
    print(c,"ouvrage(s) de l'auteur", nom)


#algorithm for when a customer asks for a certain book.
x=int(input("Taper 0 pour arrêter. Tapez 1 pour ajouter un livre. tapez 2 pour rechercher un livre.Tapez 3 pour rechercher un auteur"))
if x==1:
    print(ajout(titres,auteurs,stocks))
elif x==2:
    titre=input("saisir un titre de livre")
    if stockparlivre(titres,auteurs,stocks, titre)==-1:
        print("pas dans la bib")
    elif stockparlivre(titres,auteurs,stocks, titre)==0:
        print("aucun exemplaire dispo")
    else:
        print(stockparlivre(titres,auteurs,stocks, titre))
elif x==3:
    auteur=input("quel est votre auteur")
    print(rechparauteurs(titres,auteurs,stocks, auteur))
acheter(titres,auteurs,stocks)
leplus(auteurs,stocks)

def reponse(titres,auteurs,stocks,l): #create a file with the answers.
    fichier=open("mail.txt",'w')
    i=0
    for i in range (len(l)):
        for z in range (len(titres)):
            if (l[i][0]==titres[z]) and (l[i][1]<=stocks[z]):
                print(stocks[z])
                fichier.write("la demande peut etre satisfaite\n")
                fichier.close()
                return("fichier cree")
            else:
                fichier.write("la demande ne peut etre satisfaite\n")
                if not (l[i][0] in titres):
                    print(i)
                    fichier.write(l[i][0])
                    fichier.write(": non exsitant a la bib\n" )
                elif (l[i][0]==titres[z]) and (stocks[z]==0):
                    fichier.write(l[i][0])
                    fichier.write(" :ne peut etre emprunte actuellement ")
                    print(i)
                elif (l[i][0]==titres[z]) and (stocks[z]<l[i][1]):
                    z=l[i][1]-stocks[z]
                    fichier.write(l[i][0])
                    fichier.write(" peut etre emprunte seulement en ")
                    fichier.write(str(z))
                    fichier.write(" exemplaires\n")
                    print(i)
    fichier.close()

print(os.getcwd())








