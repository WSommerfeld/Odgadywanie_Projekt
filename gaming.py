import random


'''
inicjalizacja tablicy pozycji na których znajduje
się właściwa cyfra
'''
def initpozycje(n):
    pozycje = [False for i in range(n)]
    return pozycje

'''
inicjalizacja tablicy powtórzeń cyfr
'''

def initliczby():
    liczby = [0 for i in range(10)]
    return liczby


'''
szyfr - właściwy szyfr
traf - próba zgadnięcia
n - długość szyfru
pozycje = tablica bool zawierające na których pozycjach
znalazły się prawidłowe cufry
liczby - tablica dlugosci n, gdzie liczba na i-tej pozycji
to ilość wystąpień liczby j
'''
def check (szyfr, traf, n, pozycje, liczby):
    try:
        for i in range(n):
            if szyfr[i] == traf[i]:
                pozycje[i] = True

        sprawdzone=initpozycje(n)
        for i in range(n):
            for j in range(n):
                if traf[i]==szyfr[j] and pozycje[j]==False and sprawdzone[j]==False:
                    liczby[int(traf[i])]+=1
                    sprawdzone[j]=True
    except IndexError:
        print("indeks poza listą")

'''
zamienia string postaci "1,2,8,...,x<=n"
na tablicę prawidłowo zgadniętych pozycji,
przykładowo, gdy gracz wprowadzi za pomocą 
klawiatury łańcuch "1,3,5", to tablica pozycji
zostanie zmodyfikowana do postaci
[True, False, True, False, True, False, False, ... , False] 
'''
def PVPpozycje(pozycje, pozycjeinput):
    pozycjeinput=pozycjeinput.split(",")
    length = len(pozycjeinput)
    try:
        for i in range(length):
            pozycje[int(pozycjeinput[i])-1] = True
    except IndexError:
        print("indeks poza listą")
    except ValueError:
        x=1

'''
zamienia string postaci "1,1,3,2,...,x<=9"
na tablicę wykorzystanych w szyfrze liczb nie na swoich pozycjach
przykładowo, gdy gracz wprowadzi łańcuch "1,1,3"
to tablica liczb zostanie zmodyfikowana do postaci:
[2,0,3,0,...,0]
jeśli liczba powtórzyła się w kodzie więcej niż jeden raz, należy ją
wpisać tyle razy ile się powtarza
'''
def PVPliczby(liczby, liczbyinput):
    liczbyinput=liczbyinput.split(",")
    length = len(liczbyinput)
    try:
        for i in range(length):
            liczby[int(liczbyinput[i])]+=1
    except IndexError:
        print("indeks poza listą")
    except ValueError:
        x=1

def updateguessed(guessed, pozycje, traf):
     length = len(guessed)
     for i in range(length):
         if pozycje[i] == True:
             guessed[i]=traf[i]





def cmdPVP(n):
    iterations=0
    print("Długość kodu: "+str(n))
    guessed = ["_" for i in range(n)]

    traf="traf"
    pozycje = initpozycje(n)
    liczby = initliczby()
    gaming=True
    count=0
    while gaming:

        print("GRACZ 1")
        if iterations>0:
            print(guessed)
            print("Liczby nie na swoich pozycjach:")
            for i in range(n):
                if liczby[i]!=0:
                    print(str(i)+" występuje jeszcze "+str(liczby[i])+" razy")

        print("Zgaduj:")
        traf=input()

        if len(traf)>n:
            print("za długi!")
            continue

        print("GRACZ 2")
        print("Podaj pozycje na których jest prawidłowa cyfra:")
        PVPpozycje(pozycje, input())

        print("Podaj cyfry występujące w cyfrze, nie na swoim miejscu:")
        PVPliczby(liczby, input())

        updateguessed(guessed, pozycje, traf)

        iterations+=1

        for i in range(n):
            count=0
            if guessed[i]=="_":
                count+=1

        if count == 0:
            gaming = False
            print("WYGRANO")
            print("Prawidłowy kod to " + str(guessed))


def cmdPlayerGuessing(n):
    iterations = 0
    print("Długość kodu: " + str(n))
    guessed = ["_" for i in range(n)]

    traf = "traf"
    pozycje = initpozycje(n)
    liczby = initliczby()
    gaming = True
    count = 0

    correct_code = [str(random.randint(0,9)) for i in range(n)]

    print(correct_code)

    while gaming:


        if iterations > 0:
            print(guessed)
            print("Liczby nie na swoich pozycjach:")
            print(liczby)
            for i in range(10):
                if liczby[i] != 0:
                    print(str(i) + " występuje jeszcze " + str(liczby[i]) + " razy")

        print("Zgaduj:")
        traf = input()

        if len(traf) > n:
            print("za długi!")
            continue

        pozycje = initpozycje(n)
        liczby = initliczby()

        #tu trzeba pozmieniac
        check(correct_code, traf, n, pozycje,liczby)
        updateguessed(guessed, pozycje, traf)

        iterations += 1
        count = 0
        for i in range(n):

            if guessed[i] == "_":
                count =1
                print("lol")
        print("count: "+str(count))
        if count == 0:
            gaming = False
            print("WYGRANO")
            print("Prawidłowy kod to " + str(traf))


def autoguessing(n, correctszyfr):

    correct  = ["_" for i in range(n)]
    for i in range(n):
        correct[i]=correctszyfr[i]

    cyfry = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    liczbydowstawienia = []
    bestszyfr  = ["_" for i in range(n)]
    pozycje = initpozycje(n)
    liczby = initliczby()
    x=0
    while bestszyfr != correct:

        for i in range(9):
            for j in range(int(liczby[i])):
                liczbydowstawienia.append(str(i))

        for i in range(n):
            if pozycje[i] == False:
                if liczbydowstawienia.count(i)!=0:
                    print(liczbydowstawienia)
                    wstaw = random.choice(liczbydowstawienia)
                    liczbydowstawienia.remove(wstaw)
                    bestszyfr[i] = wstaw
                else:
                    bestszyfr[i] = random.choice(cyfry)








        check(correctszyfr,bestszyfr,n,pozycje, liczby)
        x+=1
        print(x,": ",bestszyfr)





