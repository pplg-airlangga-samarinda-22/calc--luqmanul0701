import tkinter as tk
from tkinter import messagebox


# Fungsi untuk melakukan perhitungan
def hitung(operasi):
    try:
        angka1 = float(entry1.get())
        angka2 = float(entry2.get())

        if operasi == '+':
            hasil = angka1 + angka2
        elif operasi == '-':
            hasil = angka1 - angka2
        elif operasi == '*':
            hasil = angka1 * angka2
        elif operasi == '/':
            if angka2 == 0:
                messagebox.showerror("Error", "Tidak bisa membagi dengan nol!")
                return
            hasil = angka1 / angka2

        label_hasil.config(text=f"Hasil: {hasil}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")


# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("400x450")

# Label dan Entry untuk angka pertama
tk.Label(root, text="Angka 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

# Label dan Entry untuk angka kedua
tk.Label(root, text="Angka 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Tombol operasi
frame = tk.Frame(root)
frame.pack()

# button_style = {"bg": "#B82132", "fg :" "black", "width": 5, "height": 2}

tk.Button(frame, text="+", command=lambda: hitung('+')).grid(row=0, column=0)
tk.Button(frame, text="-", command=lambda: hitung('-')).grid(row=0, column=1)
tk.Button(frame, text="", command=lambda: hitung('')).grid(row=1, column=0)
tk.Button(frame, text="/", command=lambda: hitung('/')).grid(row=1, column=1)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="Hasil: ")
label_hasil.pack()

# Menjalankan aplikasi
root.mainloop()