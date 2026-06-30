import tkinter as tk
from tkinter import messagebox

# -------------------------------------------------
# DATE DIN TABELUL 4.2 – TOLERANTE GEOMETRICE
# -------------------------------------------------
clase_precizie = [
    "I", "II", "III", "IV", "V", "VI",
    "VII", "VIII", "IX", "X", "XI", "XII"
]

date_tabel = {
    25:  [0.6, 1, 1.6, 2.5, 4, 6, 10, 16, 25, 40, 60, 100],
    40:  [0.8, 1.2, 2, 3, 5, 8, 12, 20, 30, 50, 80, 120],
    63:  [1, 1.6, 2.5, 4, 6, 10, 16, 25, 40, 60, 100, 160]
}

# -------------------------------------------------
# FUNCTIE CALCUL
# -------------------------------------------------
def calculeaza():
    try:
        dim = float(entry_dim.get())
        if dim < 20 or dim > 50:
            raise ValueError

        
        if dim <= 25:
            valori = date_tabel[25]
            interval = "Peste 16 pana la 25 mm"
        elif dim <= 40:
            valori = date_tabel[40]
            interval = "Peste 25 pana la 40 mm"
        else:
            valori = date_tabel[63]
            interval = "Peste 40 pana la 63 mm"

        rezultat = f"Interval selectat: {interval}\n"

        # -------------------------------------------------
        # OPTIUNEA 1: STIU CLASA
        # -------------------------------------------------
        if optiune.get() == 1:
            if entry_tol.get().strip() != "":
                messagebox.showerror(
                    "Eroare",
                    "Pentru aceasta optiune nu completati toleranta!"
                )
                return

            clasa = entry_clasa.get().upper().strip()
            if clasa not in clase_precizie:
                messagebox.showerror(
                    "Eroare",
                    "Clasa de precizie invalida! (I – XII)"
                )
                return

            index = clase_precizie.index(clasa)
            tol = valori[index]

            rezultat += (
                f"Clasa de precizie: {clasa}\n"
                f"Toleranta de forma: {tol} μm"
            )

        # -------------------------------------------------
        # OPTIUNEA 2: STIU TOLERANTA
        # -------------------------------------------------
        else:
            if entry_clasa.get().strip() != "":
                messagebox.showerror(
                    "Eroare",
                    "Pentru aceasta optiune nu completati clasa de precizie!"
                )
                return

            tol_introdusa = float(entry_tol.get())
            tol_std = min(valori, key=lambda x: abs(x - tol_introdusa))
            index = valori.index(tol_std)
            clasa = clase_precizie[index]

            rezultat += (
                f"Toleranta introdusa: {tol_introdusa} μm\n"
                f"Toleranta standardizata: {tol_std} μm\n"
                f"Clasa de precizie determinata: {clasa}"
            )

        label_rezultat.config(text=rezultat)

    except ValueError:
        messagebox.showerror("Eroare", "Date introduse incorect!")


# -------------------------------------------------
# FUNCTIE RESET
# -------------------------------------------------
def reset():
    entry_dim.delete(0, tk.END)
    entry_clasa.delete(0, tk.END)
    entry_tol.delete(0, tk.END)
    label_rezultat.config(text="")
    optiune.set(1)

# -------------------------------------------------
# INTERFATA GRAFICA
# -------------------------------------------------
root = tk.Tk()
root.title("Calcul Tolerante Geometrice - Suprafata Cilindrica")
root.geometry("520x450")
root.resizable(False, False)

tk.Label(root, text="Dimensiune nominala [20 – 50 mm]").pack(pady=3)
entry_dim = tk.Entry(root)
entry_dim.pack()

optiune = tk.IntVar(value=1)

tk.Radiobutton(
    root, text="Stiu clasa de precizie",
    variable=optiune, value=1
).pack()

tk.Radiobutton(
    root, text="Stiu toleranta",
    variable=optiune, value=2
).pack()

tk.Label(root, text="Clasa de precizie (I – XII)").pack(pady=3)
entry_clasa = tk.Entry(root)
entry_clasa.pack()

tk.Label(root, text="Toleranta de forma (μm)").pack(pady=(20, 10))
entry_tol = tk.Entry(root)
entry_tol.pack()

tk.Button(
    root, text="Calculeaza",
    command=calculeaza,
    bg="lightgreen"
).pack(pady=(3))   


tk.Button(
    root, text="Reset",
    command=reset,
    bg="lightyellow"
).pack(pady=5)

tk.Button(
    root, text="Iesire",
    command=root.destroy,
    bg="lightcoral"
).pack(pady=10)

label_rezultat = tk.Label(
    root, text="",
    fg="blue",
    justify="left"
)
label_rezultat.pack(pady=10)

root.mainloop()
