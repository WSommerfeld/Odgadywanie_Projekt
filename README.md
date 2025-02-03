# Odgadywanie
Michał Kasjaniuk 287392  
Maja Kołakowska 287360  
Marcin Lasak 272886  
Filip Urbański 287355 

## Opis działania programu 
Program ma umożliwiać grę w odgadywanie. Zasady gry są następujące: 
- Gracz nr 2 wymyśla szyfr
- Gracz nr 1 próbuje odgadnąć szyfr
- Gracz nr 2 podaje, na których pozycjach szyfr podany przez gracza nr 1 zgadza się z jego szyfrem oraz jakie cyfry wystąpiły w szyfrze podanym przez gracza nr 1, na niewłaściwych pozycjach w szyfrze gracza nr 2
- Rozgrywka jest kontynuowana, dopóki gracz 1 nie odgadnie szyfru gracza nr 2

 Program umożliwia rozgrywkę PVP, oraz wymianę jednego z graczy na komputer.
## Opis wykonania programu 
### Algorytm zgadywania przez komputer 
W kodzie programu znajduje się kilka algorytmów zgadywania. W finalnej wersji, wybrano ten działający najlepiej (wersja III). Algorytm ten pamięta na których pozycjach trafił prawidłową cyfrę, jakie cyfry pojawiły się w złych miejscach oraz jakie pozostały możliwości na zadanej pozycji. Stąd teoretycznie jego złożoność obliczeniowa powinna wynosić O(1) (maksymalnie 10 prób). Podczas testów, zazwyczaj komputer zgadywał kod w 6-7 próbach. W razie oszustwa gracza (wyczerpania możliwości na danej pozycji), komputer poinformuje o tym i odmówi dalszej rozgrywki.
### Interfejs graficzny 
Interfejs graficzny został wykonany przy pomocy biblioteki tkinter umożliwiającej szybkie i proste tworzenie GUI. Program posiada menu główne, w którym mamy do wyboru rozgrywkę z komputerem lub drugim graczem lub wyświetlenie tablicy wyników. Po wybraniu opcji rozgrywki z komputerem zostaniemy zapytani o to kto ma zgadywać, a kto wymyślać szyfr. Po wybraniu rodzaju rozgrywki program zapyta nas o długość szyfru, a następnie uruchomi stosowną rozgrywkę.
### Tablica wyników 
Program zawiera w sobie funkcjonalność zapisywania wyników w rozgrywce, gdzie gracz zgaduje szyfr komputera. Stąd program pyta o imię przed uruchomieniem. Niewpisanie imienia skutkuje nadaniem nazwy "Bezimienny". Do zapisywania wyników wykorzystano relacyjną bazę danych SQLite. Zdecydowano się na nią, ze względu na mały rozmiar, brak potrzeby posiadania dodatkowego DBMS oraz ze względu na fakt, że przechowywana jest w jednym pliku z rozszerzeniem .db. Plik bazy utworzono przy pomocy programu DB Browser, a jej obsługe implementowano poprzez zapewnione dla Pythona API (paczka sqlite3).
### Wywoływanie w linii komend 
Program umożliwia wywoływanie go z linii komend z określonymi parametrami. Aby dowiedzieć się więcej na ten temat, należy wykonać polecenie `python main.py --help`. 
### Instalacja środowiska wirtualnego 
W plikach projektu znajduje się skrypt umożliwiający automatyczną instalację środowiska wirtualnego venv. Wystarczy uruchomić skrypt `windowsinstalacja.bat`. Po stosownej inicjalizacji środowiska i pobraniu niezbędnych paczek, można przejść do uruchomienia programu. Plik `requirements.txt` został wygenerowany przy pomocy narzędzia pipreqs.
### Plik wykonywalny 
Dodatkowo przy pomocy narzędzia pipinstaller wygenerowano plik wykonywalny main.exe, który umożliwia bezpośrednie uruchomienie programu.



