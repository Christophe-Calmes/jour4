# Déclaration de variable
array = []

def integration():
        a = input("Entrer un integer ?")
        
        if (a.startswith('-') and a[1:].isdigit()) or (a.isdigit()):
            a = int(a)
            
        else:
            print("Vous n'avez pas taper un integer")
            a = input("Entrer un integer ?")

        return a

#Boucle while pour répéter 5 fois la solution
a = integration()

print("Nombre entrer : "+ str(a))
def factoriel(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        array.append(n - 1)
        return n * factoriel(n - 1)


resultat = factoriel(a)
factor = str(a)+'!='
for i in range(len(array)):
    if i == (len(array) - 1):
        factor = factor + str(array[i])
    else:
        factor = factor + str(array[i]) + '*'

print('Opératoion : ' + factor)
print("Le factoriel de", a, "est", resultat)
