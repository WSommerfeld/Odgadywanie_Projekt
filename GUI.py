import sys
import tkinter as tk
from tkinter import messagebox
import gaming
from gaming import PVPpozycje, updateguessed, PVPliczby, initpozycje, initliczby


class Menu:
    def __init__(self, arglength, argtype):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.title('Odgadywanie')

        self.arglength = arglength
        self.argtype = argtype

        comp_button = tk.Button(self.root, text="Graj z komputerem", command=self.computer,padx=50,pady=50)
        comp_button.pack(padx=50,pady=50)

        pvp_button = tk.Button(self.root, text="Graj z człowiekiem", command=self.PVP,padx=50,pady=50)
        pvp_button.pack(padx=0,pady=50)

        if self.arglength>0 and (self.argtype=="pvp" or self.argtype=="PVP"):
            self.PVP()

        self.root.mainloop()

    def computer(self):
      #  print("Gra z komputerem")
        self.root.destroy()
        computerGUI()

    def PVP(self):
        print("Gra z człowiekiem")
        self.root.destroy()
        PVPGUI(self.arglength)

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

    def close(self):
        if messagebox.askokcancel("Zakończ grę", "Czy na pewno chcesz zakończyć rozgrywkę?"):
            self.root.destroy()
            sys.exit(0)

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

    def setpozycje(self):
        PVPpozycje(self.pozycje,self.entryp.get())
        updateguessed(self.guessed,self.pozycje,self.traf)
        PVPliczby(self.liczby,self.entryl.get())
        self.iterations+=1

        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.root.quit()

    def correct(self):
        self.gaming=False
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.root.quit()


class computerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.title('Gra z komputerem')

        self.player_guess = tk.Button(self.root, font=('Arial 16'), text="Gracz zgaduje", command=self.playerguess,padx=50,pady=50)
        self.player_guess.pack(pady=10)

        self.computer_guess = tk.Button(self.root, font=('Arial 16'), text="Komputer zgaduje", command=self.computerguess,padx=50,pady=50)
        self.computer_guess.pack(pady=10)

        self.root.mainloop()
    def playerguess(self):
        print("start")

    def computerguess(self):
        print("start")

class rules:
    def __init__(self):
        self.length = 0
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.title('Długość szyfru')

        label = tk.Label(self.root, text="Podaj długość szyfru: ",font=('Arial 24'))
        label.pack(pady = 20)

        self.entry = tk.Entry(self.root,width=20, font=('Arial 28'))
        self.entry.pack(pady=20)

        self.set_button = tk.Button(self.root, font=('Arial 24'), text="Zatwierdź", command=self.start,padx=50,pady=50)
        self.set_button.pack(pady=10)

        self.root.mainloop()


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
