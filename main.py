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
    name="-1"
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


    # rozgrywka w GUI
    GUI.Menu(code_length, type, name)




if __name__ == '__main__':
    main()