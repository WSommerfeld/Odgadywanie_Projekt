#Gracz wprowadza szyfr - komputer 'odgaduje'
import random
# Wprowadzamy liczbe n (dlugosc szyfru) a potem szyfr zlozony z n cyfr #
Gracz=[]
#--------------------------------------------------------#
while True:
    try:
        n = int(input("Podaj dodatnią liczbę całkowitą: "))
        if (n > 0):
            break  # Wyjście z pętli, gdy liczba jest dodatnia #
        else:
            print("///Błąd - Liczba musi być dodatnia calkowita///")
    except ValueError:
        print("///Błąd - Wprowadź poprawną wartość///")

#--------------------------------------------------------#
j=1
print("///Wprowadz cyfry do szyfru",n,"-elementowego///")
while(j<=n):
    cyfra = int(input())
    Gracz.append(cyfra)
    j=j+1
print(Gracz)
#--------------------------------------------------------#
# Na samym poczatku jest losowo generowana lista zlozona z n cyfr #
Komputer=[random.randint(0,9) for _ in range(n)]
#print(Komputer)
#--------------------------------------------------------#
trafione=[]
# Jest wprowadzana pomocnicza n-elem. lista wypelniona 'X' #
for i in range(n):
    trafione.append('X')
print(trafione)
#--------------------------------------------------------#
while(Komputer != Gracz):
    i=0
    while(i <= n-1):
        if(trafione[i] == 'X'): # Jesli w liscie 'trafione' w danym miejscu i nadal jest 'X', generowana jest losowa cyfra w liscie 'Komputer' w tym samym miejscu i #
            Komputer[i]=random.randint(0,9)
            #print("Komputer zgaduje:",Komputer)
            # Na biezaco sprawdzane jest czy mamy juz trafiona cyfre, jezeli tak to zamieniamy 'X' na ta cyfre #
            if(Komputer[i] == Gracz[i]):
                print("Komputer zgadl liczbe:",Gracz[i],"na pozycji:",i)
                trafione[i]=Komputer[i]
                print(trafione)
        i=i+1
print("Gratulacje komputerze - udalo ci sie odgadnac szyfr")
