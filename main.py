import sys
import GUI
import gaming
def main():


    '''
    obsługa linii komend
    python main.py dlugość_szyfru rodzaj_rozgrywki
    rodzaj_rozgrywki € {"pvp", "PVP"}
    '''
    code_length=-1
    type = "x"
    try:
        code_length=int(sys.argv[1])
        type = sys.argv[2]
    except:
        code_length=-1
        type = "x"


    # rozgrywka w GUI
    #GUI.Menu(code_length, type)

    n=4
    guessed = ["_" for i in range(n)]
    pozycje = gaming.initpozycje(n)
    liczby=gaming.initliczby()
    opcjenapozycji = gaming.initopcjenapozycji(n)

    gaming.onetimeguess(guessed,  liczby,opcjenapozycji, n)


if __name__ == '__main__':
    main()