import random
import sys
from tkinter import messagebox

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
Funkcja modyfikująca listy informujące
o pozycjach, na których odgadnięto właściwe
cyfry oraz o cyfrach, które pojawiły się
nie na swoich miejscach
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
        pass

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
        pass
    except ValueError:
        pass

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

    newliczby = initliczby()
    try:
        for i in range(length):
            newliczby[int(liczbyinput[i])]+=1
    except IndexError:
        pass
    except ValueError:
        pass

    for i in range(10):
        if newliczby[i]>liczby[i]:
            liczby[i]=newliczby[i]

'''
Aktualizacja odgadnietych cyfr w szyfrze
'''
def updateguessed(guessed, pozycje, traf):
     length = len(guessed)
     for i in range(length):
         if pozycje[i] == True:
             guessed[i]=traf[i]




'''
Rozgrywka PVP w konsoli
'''
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


'''
Rozgrywka w konsoli, gdzie gracz zgaduje
kod komputera
'''
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

'''
Testowy algorytm zgadywania przez komputer
Algorytm informowany jest o trafionych pozycjach
oraz cyfrach, które pojawiły się w kodzie nie na
swoim miejscu
'''
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
                if len(liczbydowstawienia)!=0:
                    wstaw = random.choice(liczbydowstawienia)
                    liczbydowstawienia.remove(wstaw)
                    bestszyfr[i] = wstaw
                    #odkryto możliwość nieskończonego
                    #zapętlenia się algorytmu
                else:
                    bestszyfr[i] = random.choice(cyfry)


        check(correctszyfr,bestszyfr,n,pozycje, liczby)
        x+=1
        print(x,": ",bestszyfr)




'''
pasuje_do_oceny(kandydat, trafione_miejsca, odgadniecie, trafione_cyfry, odrzucone_cyfry, pewne_cyfry)
Sprawdza, czy podany kandydat spełnia warunki na podstawie poprzednich prób, 
uwzględniając poprawnie odgadnięte cyfry oraz te na złych pozycjach.
'''

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

'''
pobierz_wejscie_liczbowe(prompt) 
Pobiera od użytkownika listę liczb oddzielonych przecinkami i zwraca je jako listę indeksów.
'''

def pobierz_wejscie_liczbowe(prompt):
    try:
        wejscie = input(prompt).strip()
        return [int(x) - 1 for x in wejscie.split(",") if x] if wejscie else []
    except ValueError:
        print("Podano nieprawidłowe dane. Wpisz liczby oddzielone przecinkiem.")
        return pobierz_wejscie_liczbowe(prompt)

'''
aktualizuj_zbiory(odgadniecie, trafione_miejsca, trafione_cyfry, pewne_cyfry, odrzucone_cyfry)
Aktualizuje zbiory cyfr: poprawnie umieszczonych, występujących na złych pozycjach oraz tych,
które można odrzucić.
'''

def aktualizuj_zbiory(odgadniecie, trafione_miejsca, trafione_cyfry, pewne_cyfry, odrzucone_cyfry):
    for pos in trafione_miejsca:
        pewne_cyfry.add(odgadniecie[pos])
    pewne_cyfry.update(trafione_cyfry)
    for cyfra in odgadniecie:
        if cyfra not in pewne_cyfry and cyfra not in trafione_cyfry:
            odrzucone_cyfry.add(cyfra)

'''
filtruj_mozliwosci(mozliwosci, trafione_miejsca, odgadniecie, trafione_cyfry, odrzucone_cyfry, pewne_cyfry)
Przesiewa listę możliwych szyfrów, pozostawiając tylko te,
które spełniają dotychczasowe warunki zgadywania.
'''

def filtruj_mozliwosci(mozliwosci, trafione_miejsca, odgadniecie, trafione_cyfry, odrzucone_cyfry, pewne_cyfry):
    return [mozliwosc for mozliwosc in mozliwosci if
            pasuje_do_oceny(mozliwosc, trafione_miejsca, odgadniecie, trafione_cyfry, odrzucone_cyfry, pewne_cyfry)]

'''
gra_z_komputerem(n)
Gra z komputerem wariant II (prototyp wersji III)
Komputer próbuje odgadnąć szyfr gracza, losując propozycje i otrzymując wskazówki o poprawnych cyfrach oraz ich pozycjach.
Na podstawie tych informacji filtruje możliwe rozwiązania i kontynuuje zgadywanie,
aż znajdzie poprawny kod lub wyczerpią się opcje.
'''

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


'''
Inicjalizacja listy list, informującej
jakie możliwości pozostały na danej
pozycji
'''
def initopcjenapozycji(n):
    opcjenapozycji = [[i for i in range(10)] for j in range(n)]
    return opcjenapozycji


'''
Uaktualnienie informacji posiadanych przez
algorytm
'''
def updateinfo(guessed, traf, pozycje, liczby, opcjenapozycji, n, pozycjeinput, liczbyinput):

    PVPpozycje(pozycje, pozycjeinput) #aktualizacja trafionych pozycji
    PVPliczby(liczby, liczbyinput)#aktualizacja cyfr, które wystąpiły w szyfrze nie na swoim miejscu

    for i in range(n):
        if pozycje[i] == True:
            guessed[i] = traf[i] #aktualizacja pozycji w szyfrze
            if liczby[traf[i]] != 0:
                liczby[traf[i]] = liczby[traf[i]]-1 #aktualizacja pozostałych cyfr

        if pozycje[i] == False:
            try:
                opcjenapozycji[i].remove(traf[i]) #usunięcie możliwości z danej pozycji
            except:
                pass




'''
Algorytm odgadywania na podstawie posiadanych informacji
'''
def onetimeguess(guessed, liczby, opcjenapozycji, n):
    traf=[guessed[i] for i in range(n)]
    cyfrydowstawienia = []

    for i in range(10):
        for j in range(int(liczby[i])):
            cyfrydowstawienia.append(i)

    #wstawianie z listy liczby
    for i in range(n):
        if traf[i] == "_":
            if len(cyfrydowstawienia)>0:
                for j in range(len(cyfrydowstawienia)):
                    wstaw=cyfrydowstawienia[j]
                    git = False
                    for k in range(len(opcjenapozycji[i])):


                        if opcjenapozycji[i][k] == wstaw:
                            git = True
                            break

                    if git:
                        traf[i]=wstaw
                        cyfrydowstawienia.remove(wstaw)
                        break

    #wstawianie losowe
    for i in range(n):
        if traf[i] == "_":
            opcjei = opcjenapozycji[i]
            try:
                traf[i]=random.choice(opcjei)
            except IndexError:
                messagebox.showerror("Oszust!","Nie gram z oszustami!")
                sys.exit(0)

    return traf


'''
Rozgrywka w konsoli wariant III
Algorytm pamięta które cyfry są trafione,
które znalazły się w cyfrze nie na swoich
miejscach i na bieżąco aktializuje ich listę,
które cyfry mogą się jeszcze pojawić
na danej pozycji
'''
def autoguessingv2(n):
    liczby = initliczby()
    opcjenapozycji = initopcjenapozycji(n)
    guessed = ["_" for i in range(n)]
    traf = [random.randint(0,9)  for i in range(n)]


    #dodac sprawdzanie ile opcji na pozycji
    while(True):
        pozycje = initpozycje(n)
        print(guessed)
        print("Traf ",traf)
        print("Pozycje")
        pozycjeinput = input()
        print("Liczby")
        liczbyinput = input()
        updateinfo(guessed, traf, pozycje, liczby, opcjenapozycji, n, pozycjeinput, liczbyinput)

        traf=onetimeguess(guessed, liczby, opcjenapozycji, n)



        count=0
        for i in range(n):
            if guessed[i] == "_":
                count+=1
        if count == 0:
            break








'''
Rozgrywka w konsoli wariant I
Algorytm jest informowany o "trafionych"
pozycjach w szyfrze gracza
'''
# Wprowadzamy liczbe n (dlugosc szyfru) a potem szyfr zlozony z n cyfr #
#--------------------------------------------------------#
#while True:
    #try:
        #n = int(input("Podaj dodatnią liczbę całkowitą: "))
        #if (n > 0):
            #break  # Wyjście z pętli, gdy liczba jest dodatnia #
        #else:
            #print("///Błąd - Liczba musi być dodatnia calkowita///")
    #except ValueError:
        #print("///Błąd - Wprowadź poprawną wartość///")

#--------------------------------------------------------#
def first_player(n):
    Gracz=[]
    j=1
    print("///Wprowadz cyfry do szyfru",n,"-elementowego///")
    while(j<=n):
        cyfra = int(input())
        Gracz.append(cyfra)
        j=j+1
    return(Gracz)
#--------------------------------------------------------#

#--------------------------------------------------------#
def guess_game(n,Gracz):
    # Na samym poczatku jest losowo generowana lista zlozona z n cyfr #
    Komputer=[random.randint(0,9) for _ in range(n)]
    trafione=[]
    # Jest wprowadzana pomocnicza n-elem. lista 'trafione' wypelniona 'X' #
    for i in range(n):
        trafione.append('X')
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
