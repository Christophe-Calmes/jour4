line = ''
def integration():
        a = input("Entrer un integer qui sera le coté du carré?")
        
        if (a.startswith('-') and a[1:].isdigit()) or (a.isdigit()):
            a = int(a)
            
        else:
            print("Vous n'avez pas taper un integer")
            a = input("Entrer un integer ?")
        return a

def creatLine(n, line):
    for a in range(n):
        line = '|__|'+line
    return line

n = integration()
line = creatLine(n, line)

for i in range(n):
    print(line)