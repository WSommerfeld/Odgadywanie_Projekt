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
    GUI.Menu(code_length, type)

    #gaming.cmdPlayerGuessing(4)

    #gaming.autoguessing(5,"21371")

    #rozgrywka w konsoli456
    # gaming.cmdPVP(4)
    '''
    #test string-->pozycje
    pozycje=gaming.initpozycje(5)
    print(pozycje)
    gaming.PVPpozycje(pozycje,"1,2")
    print(pozycje)
    '''

    '''
    #test string-->liczby
    liczby = gaming.initliczby(5)
    print(liczby)
    gaming.PVPliczby(liczby,"1,1,1,1,3,1,1,1")
    print(liczby)
    '''


if __name__ == '__main__':
    main()
