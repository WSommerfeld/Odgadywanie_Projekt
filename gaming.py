import random
'''
inicjalizacja tablicy pozycji na których znajduje
się właściwa cyfra
'''



def initpozycje(n):
    pozycje = [False for i in range(n)]
    return pozycje

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

        for i in range(n):
            if pozycje[i] == False:
                for j in range(n):
                    if traf[i]==szyfr[j]:
                        liczby[i]+=1
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





def pasuje_do_oceny(mozliwosci, trafione_miejsca, n, odgadniecie, trafione_cyfry, odrzucone_cyfry, pewne_cyfry):

    for kandydat in mozliwosci:
        # sprawdzenie trafionych miejsc
        for pos in range(n):
            if pos in trafione_miejsca and kandydat[pos] != odgadniecie[pos]:
                return False
            if pos not in trafione_miejsca and kandydat[pos] == odgadniecie[pos]:
                return False

    # sprawdzenie, czy trafione cyfry są obecne, ale nie na złych miejscach
        for cyfra in trafione_cyfry:
            if cyfra not in kandydat:
                return False
            if cyfra in [kandydat[pos] for pos in trafione_miejsca]:
                return False

    # wykluczenie cyfr, które na pewno nie występują
        if any(cyfra in odrzucone_cyfry for cyfra in kandydat):
            return False

    # sprawdzenie, czy kandydat zawiera wszystkie cyfry w `pewne_cyfry`
        if not all(cyfra in kandydat for cyfra in pewne_cyfry):
            return False

        return True


'''
1. podział na osobne funkcje
2. wpisywanie po przecinku (split)
'''
def gra_z_komputerem(n):
    #n = 4  # długość szyfru
    print("Długość szyfru:", n)
    input("Wymyśl szyfr i zapamiętaj go! (Nie podawaj go komputerowi!)")

    liczba_prob = 0
    mozliwosci = [list(map(int, str(i).zfill(n))) for i in range(10**n)]
    pewne_cyfry = set()  # cyfry, które na pewno występują
    odrzucone_cyfry = set()  # cyfry, które na pewno nie występują

    while mozliwosci:
        liczba_prob += 1
        odgadniecie = random.choice(mozliwosci)
        print(f"Komputer odgaduje: {''.join(map(str, odgadniecie))}")

        try:
            trafione_miejsca = input("Podaj pozycje (1-4), gdzie cyfry są na właściwych miejscach (np. 1 3): ")
            trafione_cyfry = input("Podaj cyfry, które są w szyfrze, ale na złych miejscach (np. 4 6): ")

            # zamiana wprowadzeń na listy
            trafione_miejsca = [int(pos) - 1 for pos in trafione_miejsca.split()] if trafione_miejsca.strip() else []
            trafione_cyfry = [int(cyfra) for cyfra in trafione_cyfry.split()] if trafione_cyfry.strip() else []

            # sprawdzenie czy wprowadzone dane są prawidłowe
            if any(pos < 0 or pos >= n for pos in trafione_miejsca):
                print("Podano nieprawidłowe pozycje. Spróbuj jeszcze raz.")
                continue
        except ValueError:
            print("Podano nieprawidłowe dane. Wpisz liczby oddzielone spacją.")
            continue

        # jeśli komputer odgadł wszystkie pozycje
        if len(trafione_miejsca) == n and sorted(trafione_miejsca) == list(range(n)):
            print(f"Komputer odgadł Twój szyfr {''.join(map(str, odgadniecie))} w {liczba_prob} próbach!")
            break

        # aktualizacja zbiorów cyfr
        pewne_cyfry.update(odgadniecie[pos] for pos in trafione_miejsca)  # cyfry na dobrych miejscach
        pewne_cyfry.update(trafione_cyfry)  # cyfry poprawne na złych miejscach
        odrzucone_cyfry.update(cyfra for cyfra in odgadniecie if cyfra not in pewne_cyfry)

        # filtrowanie możliwych szyfrów
        pasuje_do_oceny( mozliwosci,trafione_miejsca, n, odgadniecie, trafione_cyfry, odrzucone_cyfry, pewne_cyfry)

        # pokaż możliwości przed filtrowaniem
        print(f"Przed filtrowaniem: pozostało {len(mozliwosci)} możliwości.")

        mozliwosci = [mozliwosc for mozliwosc in mozliwosci if pasuje_do_oceny(mozliwosci, trafione_miejsca, n, odgadniecie, trafione_cyfry, odrzucone_cyfry, pewne_cyfry)]

        # pokaż po filtrowaniu
        print(f"Po filtrowaniu: pozostało {len(mozliwosci)} możliwości.")

        if not mozliwosci:
            print("Nie udało się odgadnąć szyfru. Sprawdź, czy dane były poprawnie wprowadzone.")
            break




