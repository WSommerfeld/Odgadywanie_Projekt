import random
import sys
import tkinter as tk
from tkinter import messagebox, END
import gaming
from gaming import PVPpozycje, updateguessed, PVPliczby, initpozycje, initliczby, initopcjenapozycji, updateinfo, onetimeguess

import sqlite3

'''
Klasa odpowiadająca za Menu główne
w którym wybieramy rozgrywkę PVP, z komputerem
lub wyświetlamy tablicę wyników
'''
class Menu:
    def __init__(self, arglength, argtype, name):
        from tkinter.simpledialog import askstring
        from tkinter.messagebox import showinfo
        if name=="-1":

            self.name = askstring('Imie', 'Jak się nazywasz?')
            if self.name==None or self.name=="":
                self.name = "Bezimienny"
            showinfo('Witaj!', 'Hej {}'.format(self.name))
        else:
            self.name = name

        self.arglength = arglength
        self.argtype = argtype

        if self.arglength>0 and (self.argtype=="pvp" or self.argtype=="PVP"):
            self.PVP()

        if self.arglength>0 and (self.argtype=="pvc" or self.argtype=="PVC"):
            self.PVC()

        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.iconbitmap("icon.ico")
        self.root.resizable(False, False)
        self.root.title('Odgadywanie')

        comp_button = tk.Button(self.root, text="Graj z komputerem", command=self.computer,padx=40,pady=40)
        comp_button.pack(padx=0,pady=10)

        pvp_button = tk.Button(self.root, text="Graj z człowiekiem", command=self.PVP,padx=40,pady=40)
        pvp_button.pack(padx=0,pady=50)

        score_button = tk.Button(self.root, text="Tablica wyników", command=self.score,padx=40,pady=40)
        score_button.pack(padx=0, pady=10)

        self.root.mainloop()

    '''
    Przejście do GUI odpowiedzialnego
    za wybór typu rozgrywki z komputerem
    '''
    def computer(self):
      #  print("Gra z komputerem")
        self.root.destroy()
        computerGUI(self.arglength,self.name)

    '''
    Przejście do GUI odpowiedzialnego
    za rozgrywkę PVP
    '''
    def PVP(self):
        print("Gra z człowiekiem")
        self.root.destroy()
        PVPGUI(self.arglength)

    '''
    Przejście do GUI odpowiedzialnego
    za rozgrywkę w której gracz zgaduje
    '''
    def PVC(self):
        self.root.destroy()
        PlayerGuess(self.arglength, self.name)

    '''
    Otworzenie okna z tablicą
    wyników pobieraną z bazy sqlite
    '''
    def score(self):
        conn = sqlite3.connect('wyniki.db')
        cursor = conn.cursor()
        tablica = cursor.execute("SELECT name as 'Nazwa', score as 'Wynik' FROM wyniki ORDER BY score desc").fetchall()
        conn.close()

        total_rows = len(tablica)

        newroot = tk.Tk()
        newroot.title('Tablica wyników (gracz vs komputer)')
        newroot.geometry('500x500')
        newroot.iconbitmap("icon.ico")
        newroot.resizable(False, True)

        for i in range(total_rows):
            for j in range(2):
                e = tk.Entry(newroot, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                e.grid(row=i+1, column=j)
                e.insert(END, tablica[i][j])


'''
Klasa odpowiedzialna za interfejs graficzny rozgrywki
pomiędzy dwoma graczami
'''
class PVPGUI:

    def __init__(self, arglength):
        self.length=0
        self.arglength = arglength
        if self.arglength>0:
            self.length = self.arglength
        else:
            self.length = rules().length
            if self.length == 0 or self.length == "" or int(self.length) <= 0:
                return

        self.iterations=0
        self.guessed=["_" for i in range(int(self.length))]
        self.traf = "traf"
        self.pozycje = gaming.initpozycje(int(self.length))
        self.liczby = gaming.initliczby()
        self.gaming = True
        self.count = 0

        #print(self.length)
        self.root = tk.Tk()
        self.root.iconbitmap("icon.ico")
        self.root.geometry('500x600')
        self.root.resizable(False, False)

        self.root.protocol("WM_DELETE_WINDOW", self.close)

        while(self.gaming):
            self.gracz1()
            self.gracz2()
            count = 0
            for i in range(int(self.length)):

                if self.guessed[i] == "_":
                    count += 1

            if count == 0:
                self.gaming = False

        messagebox.showinfo("Wygrana!", "Brawo! Zgadłeś szyfr gracza nr 2.")
        self.root.destroy()
        Menu(-1,"x")

    '''
    Obsługa zamknięcia okna
    '''
    def close(self):
        if messagebox.askokcancel("Zakończ grę", "Czy na pewno chcesz zakończyć rozgrywkę?"):
            self.root.destroy()
            sys.exit(0)

    '''
    Zmiana okna dla gracza zgadującego
    '''
    def gracz1(self):
        self.root.title("Zgaduj!")

        guessed_var = tk.StringVar()
        guessed_var.set(str(self.guessed))
        lista = " "
        liczbyvar = tk.StringVar()
        for i in range(10):
            if self.liczby[i] != 0:
                lista = lista + str(i) + " wystąpiło " + str(self.liczby[i]) +" razy, "
        liczbyvar.set(lista)
        #print(lista)
        if self.iterations>0:
            tk.Label(self.root, textvariable=guessed_var,
            font=("Arial", 24, "bold")).pack(pady=10)
            tk.Label(self.root, textvariable=liczbyvar,wraplength=400,
                     font=("Arial", 12, "bold")).pack(pady=10)

        text_var = tk.StringVar()
        text_var.set("Wpisz kod o długości "+str(self.length))
        tk.Label(self.root,textvariable=text_var,
        font=("Arial", 16, "bold")).pack(pady=10)

        self.entry = tk.Entry(self.root, width=20, font=('Arial 16'))
        self.entry.pack(pady=20)

        self.set_button = tk.Button(self.root, font=('Arial 16'), text="Zatwierdź",
                                    command=self.guess,padx=50,pady=50)
        self.set_button.pack(pady=10)

        self.root.mainloop()

    '''
    Wykonanie próby zgadnięcia kodu
    '''
    def guess(self):
        self.traf = self.entry.get()
        try:
            x = int(self.traf)
        except ValueError:
            messagebox.showerror("Format szyfru", "Szyfr powinien składać się z cyfr!")
            return

        if self.traf==None or len(self.traf)<0 or len(self.traf)!=int(self.length):
            messagebox.showerror("Długość szyfru", "Proszę podać szyfr o prawidłowej długości")
            return
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.root.quit()



    '''
    Zmiana okna dla gracza wymyślającego kod
    '''
    def gracz2(self):
        self.root.title("Sprawdź!")

        self.pozycje=initpozycje(int(self.length))
        self.liczby=initliczby()


        text_var = tk.StringVar()
        text_var.set(self.traf)
        tk.Label(self.root,textvariable=text_var,
        font=("Arial", 16, "bold")).pack(pady=10)


        text_var1 = tk.StringVar()
        text_var1.set("Na których pozycjach ")
        tk.Label(self.root,textvariable=text_var1,
        font=("Arial", 16, "bold")).pack(pady=5)

        text_var2 = tk.StringVar()
        text_var2.set("znajdują się prawidłowe cyfry?")
        tk.Label(self.root, textvariable=text_var2,
                 font=("Arial", 16, "bold")).pack(pady=10)



        self.entryp = tk.Entry(self.root, width=20, font=('Arial 16'))
        self.entryp.pack(pady=20)

        text_var3 = tk.StringVar()
        text_var3.set("Jakie cyfry wystąpiły")
        tk.Label(self.root, textvariable=text_var3,
                 font=("Arial", 16, "bold")).pack(pady=5)

        text_var4 = tk.StringVar()
        text_var4.set("na nieprawidłowych pozycjach?")
        tk.Label(self.root, textvariable=text_var4,
                 font=("Arial", 16, "bold")).pack(pady=10)

        self.entryl = tk.Entry(self.root, width=20, font=('Arial 16'))
        self.entryl.pack(pady=20)

        self.setp_button = tk.Button(self.root, font=('Arial 16'), text="Zatwierdź",
                                    command=self.setpozycje,padx=50,pady=50)
        self.setp_button.pack(pady=10)

        self.correctbutton = tk.Button(self.root, font=('Arial 12'), text="Gracz 1 zgadł mój szyfr",
                                    command=self.correct,padx=10,pady=10)
        self.correctbutton.pack(pady=10)

        self.root.mainloop()

    '''
    Zmiana tablicy pozycje zgodnie
    z inputem gracza 2
    '''
    def setpozycje(self):
        PVPpozycje(self.pozycje,self.entryp.get())
        updateguessed(self.guessed,self.pozycje,self.traf)
        PVPliczby(self.liczby,self.entryl.get())
        self.iterations+=1

        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.root.quit()

    '''
    Opcja dla gracza nr 2, w której informuje,
    że jego szyfr został odgadnięty
    '''
    def correct(self):
        self.gaming=False
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.root.quit()

'''
GUI służące do wyboru rodzaju rozgrywki z komputerem
'''
class computerGUI:
    def __init__(self,arglength, name):
        self.name = name
        self.root = tk.Tk()
        self.arglength = arglength
        self.root.geometry('500x500')
        self.root.iconbitmap("icon.ico")
        self.root.resizable(False, False)
        self.root.title('Gra z komputerem')

        self.player_guess = tk.Button(self.root, font=('Arial 16'), text="Gracz zgaduje", command=self.playerguess,padx=50,pady=50)
        self.player_guess.pack(pady=10)

        self.computer_guess = tk.Button(self.root, font=('Arial 16'), text="Komputer zgaduje", command=self.computerguess,padx=50,pady=50)
        self.computer_guess.pack(pady=10)

        self.root.mainloop()

    '''
    Przejście do GUI rozgrywki, w której
    gracz zgaduje szyfr komputera
    '''
    def playerguess(self):
        self.root.destroy()
        PlayerGuess(self.arglength, self.name)

    '''
    Przejście do GUI rozgrywki, w której
    komputer zgaduje szyfr gracza
    '''
    def computerguess(self):
        self.root.destroy()
        ComputerGuess(self.arglength, self.name)

    '''
    Klasa odpowiedzialna za okno, w którym
    ustalana jest długość szyfru
    '''
class rules:
    def __init__(self):
        self.length = 0
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.iconbitmap("icon.ico")
        self.root.resizable(False, False)
        self.root.title('Długość szyfru')

        label = tk.Label(self.root, text="Podaj długość szyfru: ",font=('Arial 24'))
        label.pack(pady = 20)

        self.entry = tk.Entry(self.root,width=20, font=('Arial 28'))
        self.entry.pack(pady=20)

        self.set_button = tk.Button(self.root, font=('Arial 24'), text="Zatwierdź", command=self.start,padx=50,pady=50)
        self.set_button.pack(pady=10)

        self.root.mainloop()

    '''
    Wyjście z okna rules, ze zwróceniem
    wprowadzonej wartości
    '''
    def start(self):
        self.length =self.entry.get()

        try:

            if self.length==0 or self.length=="" or int(self.length)<=0:
                messagebox.showerror("Błąd podania długości", "Proszę podać prawidłową długość szyfru!")
                return
        except ValueError:
            messagebox.showerror("Błąd podania długości", "Proszę podać prawidłową długość szyfru!")
            return
        self.root.destroy()
        return self.length

'''
Klasa odpowiedzialna za GUI rozgrywki z komputerem,
w której gracz odgaduje szyfr komputera
'''

class PlayerGuess:
    def __init__(self,arglength, name):
        self.name = name
        self.length = 0
        self.arglength = arglength
        if self.arglength > 0:
            self.length = self.arglength
        else:
            self.length = rules().length
            if self.length == 0 or self.length == "" or int(self.length) <= 0:
                return


        self.szyfr = [str(random.randint(0,9)) for i in range(int(self.length))]
        self.iterations = 0
        self.guessed = ["_" for i in range(int(self.length))]
        self.traf = "traf"
        self.pozycje = gaming.initpozycje(int(self.length))
        self.liczby = gaming.initliczby()
        self.gaming = True
        self.count = 0

        # print(self.length)
        self.root = tk.Tk()
        self.root.iconbitmap("icon.ico")
        self.root.title('Zgaduj!')
        self.root.geometry('500x600')
        self.root.resizable(False, False)

        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.iterations =0
        while(self.gaming):
            self.iterations +=1
            self.guess()

            count = 0
            for i in range(int(self.length)):

                if self.guessed[i] == "_":
                    count += 1

            if count == 0:
                self.gaming = False

        messagebox.showinfo("Wygrana!", "Brawo! Zgadłeś szyfr komputera! Było to: "+str(self.szyfr))

        if self.name!="-1":



            conn = sqlite3.connect("wyniki.db")
            c = conn.cursor()

            id = c.execute("SELECT COUNT(ID) FROM WYNIKI").fetchone()[0] + 1

            score = (1/(self.iterations-1))*1000
            inscore = int(score)

            c.execute("INSERT INTO WYNIKI (ID,NAME,SCORE) VALUES (?,?,?)", (id,self.name,inscore))
            c.execute("UPDATE wyniki SET name='User' WHERE name IS NULL")

            conn.commit()
            conn.close()



        self.root.destroy()
        Menu(-1,"x", self.name)

    '''
    Kolejna iteracja zgadywania przez gracza kodu komputera
    '''
    def guess(self):
        self.root.title("Zgaduj!")

        guessed_var = tk.StringVar()
        guessed_var.set(str(self.guessed))
        lista = " "
        liczbyvar = tk.StringVar()
        for i in range(10):
            if self.liczby[i] != 0:
                lista = lista + str(i) + " wystąpiło " + str(self.liczby[i]) + " razy, "
        liczbyvar.set(lista)
        # print(lista)
        if self.iterations > 0:
            tk.Label(self.root, textvariable=guessed_var,
                     font=("Arial", 24, "bold")).pack(pady=10)
            tk.Label(self.root, textvariable=liczbyvar, wraplength=400,
                     font=("Arial", 12, "bold")).pack(pady=10)

        text_var = tk.StringVar()
        text_var.set("Wpisz kod o długości " + str(self.length))
        tk.Label(self.root, textvariable=text_var,
                 font=("Arial", 16, "bold")).pack(pady=10)

        self.entry = tk.Entry(self.root, width=20, font=('Arial 16'))
        self.entry.pack(pady=20)

        self.set_button = tk.Button(self.root, font=('Arial 16'), text="Zatwierdź",
                                    command=self.guesstry, padx=50, pady=50)
        self.set_button.pack(pady=10)

        self.root.mainloop()

    '''
    Obsługa zamknięcia okna
    '''
    def close(self):
        if messagebox.askokcancel("Zakończ grę", "Czy na pewno chcesz zakończyć rozgrywkę?"):
            self.root.destroy()
            sys.exit(0)
    '''
    Sprawdzenie podanego przez gracza szyfru
    '''
    def guesstry(self):
        self.pozycje = initpozycje(int(self.length))
        self.liczby = initliczby()
        self.traf = self.entry.get()
        try:
            x = int(self.traf)
        except ValueError:
            messagebox.showerror("Format szyfru", "Szyfr powinien składać się z cyfr!")
            return

        if self.traf==None or len(self.traf)<0 or len(self.traf)!=int(self.length):
            messagebox.showerror("Długość szyfru", "Proszę podać szyfr o prawidłowej długości")
            return
        for widget in self.root.winfo_children():
            widget.pack_forget()


        gaming.check(self.szyfr, self.traf, int(self.length),self.pozycje,self.liczby)
        updateguessed(self.guessed,self.pozycje,self.traf)

        self.iterations+=1

        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.root.quit()

class ComputerGuess:
    def __init__(self, arglength, name):
        self.name = name
        self.length = 0
        self.arglength = arglength
        if self.arglength > 0:
            self.length = self.arglength
        else:
            self.length = rules().length
            if self.length == 0 or self.length == "" or int(self.length) <= 0:
                return

        self.iterations = 0
        self.liczby = initliczby()
        self.opcjenapozycji = initopcjenapozycji(int(self.length))
        self.traf = [random.randint(0,9)  for i in range(int(self.length))]
        self.guessed = guessed = ["_" for i in range(int(self.length))]
        self.gaming = True

        self.root = tk.Tk()
        self.root.iconbitmap("icon.ico")
        self.root.title('Czy komputer zgadł?')
        self.root.geometry('500x600')
        self.root.resizable(False, False)

        self.root.protocol("WM_DELETE_WINDOW", self.close)



        while self.gaming:
            self.guess()






    def guess(self):
        self.pozycje = initpozycje(int(self.length))
        self.root.title("Czy komputer zgadł?")

        text_var = tk.StringVar()
        text_var.set(self.traf)
        tk.Label(self.root, textvariable=text_var,
                 font=("Arial", 16, "bold")).pack(pady=10)

        text_var1 = tk.StringVar()
        text_var1.set("Na których pozycjach ")
        tk.Label(self.root, textvariable=text_var1,
                 font=("Arial", 16, "bold")).pack(pady=5)

        text_var2 = tk.StringVar()
        text_var2.set("znajdują się prawidłowe cyfry?")
        tk.Label(self.root, textvariable=text_var2,
                 font=("Arial", 16, "bold")).pack(pady=10)

        self.entryp = tk.Entry(self.root, width=20, font=('Arial 16'))
        self.entryp.pack(pady=20)

        text_var3 = tk.StringVar()
        text_var3.set("Jakie cyfry wystąpiły")
        tk.Label(self.root, textvariable=text_var3,
                 font=("Arial", 16, "bold")).pack(pady=5)

        text_var4 = tk.StringVar()
        text_var4.set("na nieprawidłowych pozycjach?")
        tk.Label(self.root, textvariable=text_var4,
                 font=("Arial", 16, "bold")).pack(pady=10)

        self.entryl = tk.Entry(self.root, width=20, font=('Arial 16'))
        self.entryl.pack(pady=20)

        self.setp_button = tk.Button(self.root, font=('Arial 16'), text="Zatwierdź",
                                     command=self.input, padx=50, pady=50)
        self.setp_button.pack(pady=10)

        self.correctbutton = tk.Button(self.root, font=('Arial 12'), text="Komputer zgadł mój szyfr",
                                       command=self.correct, padx=10, pady=10)
        self.correctbutton.pack(pady=10)

        self.root.mainloop()

    '''
    Przyjęcie danych od gracza
    '''
    def input(self):
        pozycjeinput = self.entryp.get()
        liczbyinput = self.entryl.get()
        updateinfo(self.guessed, self.traf, self.pozycje, self.liczby, self.opcjenapozycji, int(self.length),
                   pozycjeinput, liczbyinput)

        self.traf = onetimeguess(self.guessed, self.liczby, self.opcjenapozycji, int(self.length))

        count = 0
        for i in range(int(self.length)):
            if self.guessed[i] == "_":
                count += 1
        if count == 0:
            self.gaming = False

        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.root.quit()

    '''
    Obsługa zamknięcia okna
    '''
    def close(self):
        if messagebox.askokcancel("Zakończ grę", "Czy na pewno chcesz zakończyć rozgrywkę?"):
            self.root.destroy()
            sys.exit(0)

    '''
    Komputer odgadł szyfr gracza
    '''
    def correct(self):
        self.gaming=False
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.root.quit()