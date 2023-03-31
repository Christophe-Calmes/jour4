#Tirage d'un nombre aléatoire entre 1 et 100
import random
x = random.randint(1,100)

print("Nous allons calculer la puissance de", x,'.')
def integration():
        a = input("Entrer un integer qui sera une puissance ?")
        
        if (a.startswith('-') and a[1:].isdigit()) or (a.isdigit()):
            a = int(a)
            
        else:
            print("Vous n'avez pas taper un integer")
            a = input("Entrer un integer ?")
        return a

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        result = power(base, exponent/2)
        return result * result
    else:
        result = power(base, (exponent-1)/2)
        return base * result * result

a = integration()
print('Vous avez selectionné une opération : ',x, '^',a )

result = power(x, a)
print('Les résultats = ',result)

