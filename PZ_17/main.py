import tkinter as tk
from tkinter import ttk

def clean():
    pole_imya.delete(0, tk.END)
    pole_familiya.delete(0, tk.END)
    pole_nik.delete(0, tk.END)
    pole_den.delete(0, tk.END)
    pole_mes.delete(0, tk.END)
    pole_god.delete(0, tk.END)
    pole_pol.set(0)
    pole_strana.set("USA")
    pole_email.delete(0, tk.END)
    pole_telefon.delete(0, tk.END)
    pole_parol.delete(0, tk.END)
    pole_podtverdit.delete(0, tk.END)
    check_soglasie.set(0)

def zakrit():
    okno.destroy()

okno = tk.Tk()
okno.title("Sign Up")
okno.configure(bg="#1A252F")

ramka = tk.Frame(okno, bg="#1A252F")
ramka.pack(pady=10)

nadpis = tk.Label(ramka, text="Sign Up", font=("Arial", 14), fg="white", bg="#D4A017")
nadpis.pack()

pole_imya_label = tk.Label(ramka, text="First Name", fg="#D4A017", bg="#1A252F")
pole_imya_label.pack()
pole_imya = tk.Entry(ramka, bg="white", fg="black", insertbackground="black")
pole_imya.pack()

pole_familiya_label = tk.Label(ramka, text="Last Name", fg="#D4A017", bg="#1A252F")
pole_familiya_label.pack()
pole_familiya = tk.Entry(ramka, bg="white", fg="black", insertbackground="black")
pole_familiya.pack()

pole_nik_label = tk.Label(ramka, text="Screen Name", fg="#D4A017", bg="#1A252F")
pole_nik_label.pack()
pole_nik = tk.Entry(ramka, bg="white", fg="black", insertbackground="black")
pole_nik.pack()

pole_den_label = tk.Label(ramka, text="Date of Birth", fg="#D4A017", bg="#1A252F")
pole_den_label.pack()
frame_data = tk.Frame(ramka, bg="#1A252F")
frame_data.pack()
pole_mes = ttk.Combobox(frame_data, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state="readonly")
pole_mes.set("May")
pole_mes.pack(side=tk.LEFT)
pole_den = ttk.Combobox(frame_data, values=[str(i) for i in range(1, 32)], state="readonly")
pole_den.set("5")
pole_den.pack(side=tk.LEFT)
pole_god = ttk.Combobox(frame_data, values=[str(i) for i in range(1900, 2026)], state="readonly")
pole_god.set("1985")
pole_god.pack(side=tk.LEFT)

pole_pol_label = tk.Label(ramka, text="Gender", fg="#D4A017", bg="#1A252F")
pole_pol_label.pack()
pole_pol = tk.IntVar()
tk.Radiobutton(ramka, text="Male", variable=pole_pol, value=1, bg="#1A252F", fg="white", selectcolor="#1A252F", activebackground="#1A252F").pack(side=tk.LEFT)
tk.Radiobutton(ramka, text="Female", variable=pole_pol, value=2, bg="#1A252F", fg="white", selectcolor="#1A252F", activebackground="#1A252F").pack(side=tk.LEFT)

pole_strana_label = tk.Label(ramka, text="Country", fg="#D4A017", bg="#1A252F")
pole_strana_label.pack()
pole_strana = ttk.Combobox(ramka, values=["USA", "Canada", "UK"], state="readonly")
pole_strana.set("USA")
pole_strana.pack()

pole_email_label = tk.Label(ramka, text="E-mail", fg="#D4A017", bg="#1A252F")
pole_email_label.pack()
pole_email = tk.Entry(ramka, bg="white", fg="black", insertbackground="black")
pole_email.pack()

pole_telefon_label = tk.Label(ramka, text="Phone", fg="#D4A017", bg="#1A252F")
pole_telefon_label.pack()
pole_telefon = tk.Entry(ramka, bg="white", fg="black", insertbackground="black")
pole_telefon.pack()

pole_parol_label = tk.Label(ramka, text="Password", fg="#D4A017", bg="#1A252F")
pole_parol_label.pack()
pole_parol = tk.Entry(ramka, show="*", bg="white", fg="black", insertbackground="black")
pole_parol.pack()

pole_podtverdit_label = tk.Label(ramka, text="Confirm Password", fg="#D4A017", bg="#1A252F")
pole_podtverdit_label.pack()
pole_podtverdit = tk.Entry(ramka, show="*", bg="white", fg="black", insertbackground="black")
pole_podtverdit.pack()

check_soglasie = tk.IntVar()
check = tk.Checkbutton(ramka, text="I agree to the Terms of Use", variable=check_soglasie, bg="#1A252F", fg="white", selectcolor="#1A252F", activebackground="#1A252F")
check.pack()

knopka_frame = tk.Frame(okno, bg="#D4A017")
knopka_frame.pack(fill=tk.X, pady=10)

knopka_submit = tk.Button(knopka_frame, text="submit", command=clean, bg="#90EE90", fg="black")
knopka_submit.pack(side=tk.RIGHT, padx=5)

knopka_cancel = tk.Button(knopka_frame, text="Cancel", command=zakrit, bg="#FF6347", fg="black")
knopka_cancel.pack(side=tk.RIGHT, padx=5)

okno.mainloop()

