import tkinter as tk

class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.title('Odgadywanie')

        comp_button = tk.Button(self.root, text="Graj z komputerem", command=self.computer,padx=50,pady=50)
        comp_button.pack(padx=50,pady=50)

        pvp_button = tk.Button(self.root, text="Graj z człowiekiem", command=self.PVP,padx=50,pady=50)
        pvp_button.pack(padx=0,pady=50)


        self.root.mainloop()

    def computer(self):
        print("Gra z komputerem")
        self.root.destroy()
        computerGUI()

    def PVP(self):
        print("Gra z człowiekiem")
        self.root.destroy()
        PVPGUI()

class PVPGUI:
    def __init__(self):
        self.length=0
        self.length = rules().length
        if self.length==0 or self.length=="":
            return

        print(self.length)
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.title('Odgadywanie')
        label = tk.Label(self.root, text="Zgadywanie")
        label.pack()

        self.root.mainloop()

class computerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.title('Odgadywanie')

        self.root.mainloop()

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
        self.root.destroy()
        return self.length
