import GUI
import random
import gaming
import testymaja
from gaming import PVPliczby


def main():

    #rozgrywka w GUI#
    #GUI.Menu()
    #rozgrywka w konsoli456
    #gaming.cmdPVP(4)

    gaming.gra_z_komputerem(4)

    '''
    pozycje=gaming.initpozycje(4)
    print(pozycje)

    print("wpisz pozycje po przecinku")
    gaming.PVPpozycje(pozycje,input())

    print(pozycje)
    '''

    '''
    liczby = gaming.initliczby()
    print(liczby)

    print("Wpisz po przecinku, cyfry które wystąpiły w kodzie")
    PVPliczby(liczby,input())

    print(liczby)

    ''''''
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