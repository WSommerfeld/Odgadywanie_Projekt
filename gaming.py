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


def pasuje_do_oceny(kandydat, trafione_miejsca, odgadniecie, trafione_cyfry, odrzucone_cyfry, pewne_cyfry):
    for pos in trafione_miejsca:
        if kandydat[pos] != odgadniecie[pos]:
            return False
    for pos in range(len(kandydat)):
        if pos not in trafione_miejsca and kandydat[pos] == odgadniecie[pos]:
            return False
    for cyfra in trafione_cyfry:
        if cyfra not in kandydat or any(kandydat[pos] == cyfra for pos in trafione_miejsca):
            return False
    if any(cyfra in odrzucone_cyfry for cyfra in kandydat):
        return False
    return True


def pobierz_wejscie_liczbowe(prompt):
    try:
        wejscie = input(prompt).strip()
        return [int(x) - 1 for x in wejscie.split(",") if x] if wejscie else []
    except ValueError:
        print("Podano nieprawidłowe dane. Wpisz liczby oddzielone przecinkiem.")
        return pobierz_wejscie_liczbowe(prompt)


def aktualizuj_zbiory(odgadniecie, trafione_miejsca, trafione_cyfry, pewne_cyfry, odrzucone_cyfry):
    for pos in trafione_miejsca:
        pewne_cyfry.add(odgadniecie[pos])
    pewne_cyfry.update(trafione_cyfry)
    for cyfra in odgadniecie:
        if cyfra not in pewne_cyfry and cyfra not in trafione_cyfry:
            odrzucone_cyfry.add(cyfra)


def filtruj_mozliwosci(mozliwosci, trafione_miejsca, odgadniecie, trafione_cyfry, odrzucone_cyfry, pewne_cyfry):
    return [mozliwosc for mozliwosc in mozliwosci if
            pasuje_do_oceny(mozliwosc, trafione_miejsca, odgadniecie, trafione_cyfry, odrzucone_cyfry, pewne_cyfry)]


def gra_z_komputerem(n):
    print("Długość szyfru:", n)
    input("Wymyśl szyfr i zapamiętaj go! (Nie podawaj go komputerowi!)")

    liczba_prob = 0
    mozliwosci = [[int(digit) for digit in str(i).zfill(n)] for i in range(10 ** n)]
    pewne_cyfry, odrzucone_cyfry = set(), set()

    while mozliwosci:
        liczba_prob += 1
        odgadniecie = random.choice(mozliwosci)
        print(f"Komputer odgaduje: {''.join(str(digit) for digit in odgadniecie)}")

        trafione_miejsca = pobierz_wejscie_liczbowe(
            f"Podaj pozycje (1-{n}), gdzie cyfry są na właściwych miejscach, oddzielone przecinkiem: ")
        trafione_cyfry = pobierz_wejscie_liczbowe(
            "Podaj cyfry, które są w szyfrze, ale na złych miejscach, oddzielone przecinkiem: ")
        trafione_cyfry = [x + 1 for x in trafione_cyfry]

        if len(trafione_miejsca) == n and sorted(trafione_miejsca) == list(range(n)):
            print(f"Komputer odgadł Twój szyfr {''.join(str(digit) for digit in odgadniecie)} w {liczba_prob} próbach!")
            break

        aktualizuj_zbiory(odgadniecie, trafione_miejsca, trafione_cyfry, pewne_cyfry, odrzucone_cyfry)
        print(f"Przed filtrowaniem: pozostało {len(mozliwosci)} możliwości.")
        mozliwosci = filtruj_mozliwosci(mozliwosci, trafione_miejsca, odgadniecie, trafione_cyfry, odrzucone_cyfry,
                                        pewne_cyfry)
        print(f"Po filtrowaniu: pozostało {len(mozliwosci)} możliwości.")

        if not mozliwosci:
            print("Nie udało się odgadnąć szyfru. Sprawdź, czy dane były poprawnie wprowadzone.")
            break
