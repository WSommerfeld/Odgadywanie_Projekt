import GUI
import gaming
def main():

    #rozgrywka w GUI
    GUI.Menu()

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