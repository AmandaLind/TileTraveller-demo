#Algorithmi:
#Skilgreinum eina tölu, hún hefur gildið 1.1 í upphafi
#Búum til fall fyrir hvern og einn reit nema þann síðasta (3,1), hvert og eitt fall segir til um hvað á sér stað þegar leikmaður er í ákveðnum reit.
#Þegar við köllum á föllin og leikmaður velur "réttar áttir" þá breytist gildið á tölunni, þar sem leikmaður hefur nú færst um reit.
#Notum if-setningar til þess að kalla á viðeigandi föll
#Setjum while lykkju í kringum þær if-setningar svo að hægt sé að hreyfa sig að vild, þar til leikmaður kemst í reit 3,1

def reitur_1_1(reitur):
    print("You can travel: (N)orth.")
    Direct=input("Direction: ")

    if Direct == 'N' or Direct=='n':
        reitur=1.2
        return reitur
    else:
        print("Not a valid direction!") ##Laga þetta
        return


def reitur_1_2(reitur):
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    Direct=input("Direction: ")

    if Direct == 'S' or Direct =='s':
        reitur=1.1
        return reitur
    elif Direct == 'E' or Direct == 'e':
        reitur=2.2
        return reitur
    elif Direct =='N' or Direct == 'n':
        reitur=1.3
        return reitur
    else: 
        print("Not a valid direction!") ##LAga þetta
        return 

def reitur_1_3(reitur):
    print("You can travel: (E)ast or (S)outh.")
    Direct=input("Direction: ")

    if Direct == 'S' or Direct =='s':
        reitur=1.2
        return reitur
    elif Direct == 'E' or Direct == 'e':
        reitur=2.3
        return reitur
    else: 
        print("Not a valid direction!") ##LAga þetta
        return 



def reitur_2_3(reitur):
    print("You can travel: (E)ast or (W)est.")
    Direct=input("Direction: ")

    if Direct == 'W' or Direct =='w':
        reitur=1.3
        return reitur
    elif Direct == 'E' or Direct == 'e':
        reitur=3.3
        return reitur
    else: 
        print("Not a valid direction!") ##LAga þetta
        return


def reitur_3_3(reitur):
    print("You can travel: (S)outh or (W)est.")
    Direct=input("Direction: ")

    if Direct == 'S' or Direct == 's':
        reitur=3.2
        return reitur
    elif Direct == 'W' or Direct =='w':
        reitur=2.3
        return reitur
    else:
        print("Not a valid direction!") ##LAga þetta
        return


def reitur_3_2(reitur):
    print("You can travel: (N)orth or (S)outh.")
    Direct=input("Direction: ")
    sigurvegari=0

    if Direct == 'S' or Direct == 's':
        reitur=3.1
        return reitur
        

    elif Direct == 'N' or Direct =='n':
        reitur=3.3
        return reitur
    else:
        print("Not a valid direction!") ##LAga þetta
        return


def reitur_2_2(reitur):
    print("You can travel: (S)outh or (W)est.")
    Direct=input("Direction: ")

    if Direct == 'S' or Direct == 's':
        reitur=2.1
        return reitur

    elif Direct == 'W' or Direct =='w':
        reitur=1.2
        return reitur
    else:
        print("Not a valid direction!") ##LAga þetta
        return


def reitur_2_1(reitur):
    print("You can travel: (N)orth.")
    Direct=input("Direction: ")

    if Direct == 'N' or Direct == 'n':
        reitur=2.2
        return reitur
    else:
        print("Not a valid direction!") ##LAga þetta
        return






reitur=1.1
sigurvegari=0

while sigurvegari<1:
    if reitur==1.1:
        reitur=reitur_1_1(reitur)
        while reitur == None:
            reitur=reitur_1_1(reitur)

    if  reitur==1.2:
        reitur=reitur_1_2(reitur)
        while reitur == None:
            reitur=reitur_1_2(reitur)

    if reitur==1.3:
        reitur=reitur_1_3(reitur)
        while reitur == None:
            reitur=reitur_1_3(reitur)

    if reitur==2.2:
        reitur=reitur_2_2(reitur)
        while reitur == None:
            reitur=reitur_2_2(reitur)

    if reitur==2.1:
        reitur=reitur_2_1(reitur)
        while reitur == None:
            reitur=reitur_2_1(reitur)

    if reitur==2.3:
        reitur=reitur_2_3(reitur)
        while reitur == None:
            reitur=reitur_2_3(reitur)

    if reitur==3.3:
        reitur=reitur_3_3(reitur)
        while reitur == None:
            reitur=reitur_3_3(reitur)

    if reitur==3.2:
        reitur=reitur_3_2(reitur)
        while reitur == None:
            reitur=reitur_3_2(reitur)

    if reitur==3.1:
        print("Victory!") #SIGURVEGARI :)
        sigurvegari+=1