import gaming
import random

def gra_z_komputerem():
    n = 4  # długość szyfru
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
        def pasuje_do_oceny(kandydat):
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

        # pokaż możliwości przed filtrowaniem
        print(f"Przed filtrowaniem: pozostało {len(mozliwosci)} możliwości.")

        mozliwosci = [mozliwosc for mozliwosc in mozliwosci if pasuje_do_oceny(mozliwosc)]

        # pokaż po filtrowaniu
        print(f"Po filtrowaniu: pozostało {len(mozliwosci)} możliwości.")

        if not mozliwosci:
            print("Nie udało się odgadnąć szyfru. Sprawdź, czy dane były poprawnie wprowadzone.")
            break












