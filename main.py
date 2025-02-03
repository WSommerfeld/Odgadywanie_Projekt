import sys
import GUI
import gaming
def main():

    '''
    --help ;)
    '''

    try:
        entry = sys.argv[1]

        if entry == '--help':
            print('python main.py codelength gamemode')
            print('Argumenty')
            print('codelength   :długość kodu w rozgrywce; liczba całkowita')
            print('gamemode     :rodzaj rozgrywki: ')
            print('              pvp     :gra gracz vs gracz')
            print('              pvc     :gra gracz vs komputer; gracz zgaduje')
            print('              cvp     :gra gracz vs komputer; komputer zgaduje')
            print('Przy braku argumentów, program uruchomi się w menu pocztkowym')

            return
    except:
        pass

    '''
    obsługa linii komend
    python main.py dlugość_szyfru rodzaj_rozgrywki
    rodzaj_rozgrywki € {"pvp", "PVP"}
    '''
    try:
        code_length=int(sys.argv[1])
        type = sys.argv[2]

    except:
        code_length=-1
        type = "x"

    try:
        name=sys.argv[3]
    except:
        name="-1"


    '''
    Uruchomienie menu w interfejsie graficznym programu
    '''
    GUI.Menu(code_length, type, name)


if __name__ == '__main__':
    main()