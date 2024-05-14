import os
import tkinter as tk
import webbrowser
from tkinter import messagebox, filedialog

# Fonction de cryptage
def cryptage(message):
    alphabet_normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_inverse = alphabet_normal[::-1]
    alphabet_decale = alphabet_inverse[3:] + alphabet_inverse[:3]
    
    message_crypte = ""
    
    for lettre in message:
        if lettre.isalpha() and lettre.isupper():
            index_normal = alphabet_normal.index(lettre)
            lettre_cryptee = alphabet_decale[index_normal]
            message_crypte += lettre_cryptee
        else:
            message_crypte += lettre
    
    return message_crypte

# Fonction de décryptage
def decryptage(message_crypte):
    alphabet_normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_inverse = alphabet_normal[::-1]
    alphabet_decale = alphabet_inverse[3:] + alphabet_inverse[:3]
    
    message_decrypte = ""
    
    for lettre in message_crypte:
        if lettre.isalpha() and lettre.isupper():
            index_decale = alphabet_decale.index(lettre)
            lettre_decryptee = alphabet_normal[index_decale]
            message_decrypte += lettre_decryptee
        else:
            message_decrypte += lettre
    
    return message_decrypte

# Fonction pour enregistrer le fichier crypté
def enregistrer_fichier_crypte(contenu_crypte):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "wb") as file:
            file.write(contenu_crypte)
        messagebox.showinfo("Sauvegarde réussie", "Le fichier crypté a été enregistré avec succès.")

# Fonction pour enregistrer le fichier décrypté
def enregistrer_fichier_decrypte(contenu_decrypte):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(contenu_decrypte)
        messagebox.showinfo("Sauvegarde réussie", "Le fichier décrypté a été enregistré avec succès.")

def quitter_application():
    if messagebox.askokcancel("Quitter", "Êtes-vous sûr de vouloir quitter ?"):
        fenetre.quit()

def ouvrir_page_web():
    webbrowser.open("https://votresite.com/aide")

def ouvrir_page_about():
    path = os.path.abspath("C:\\Users\\walid\\Desktop\\python-cryptage\\àproposde.html")
    webbrowser.open("file://" + path)

# Fonction pour crypter le fichier
def crypter_message():
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            contenu = file.read()
            contenu_crypte = cryptage(contenu)
            if messagebox.askyesno("Enregistrer le fichier crypté", "Voulez-vous enregistrer le fichier crypté ?"):
                enregistrer_fichier_crypte(contenu_crypte.encode("utf-8"))  # Encodez le contenu crypté en UTF-8
            label_resultat.config(text="Le Contenu du fichier texte crypté à 100% ;) ")

# Fonction pour décrypter le fichier
def decrypter_message():
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "rb") as file:  # Ouvrez le fichier en mode binaire
            contenu_crypte = file.read().decode("utf-8")  # Décodage du contenu en UTF-8
            contenu_decrypte = decryptage(contenu_crypte)
            if messagebox.askyesno("Enregistrer le fichier décrypté", "Voulez-vous enregistrer le fichier décrypté ?"):
                enregistrer_fichier_decrypte(contenu_decrypte)
            label_resultat.config(text="Le Contenu du fichier texte décrypté à 100% ;) ")

fenetre = tk.Tk()
fenetre.title("Cryps Software")

image = tk.PhotoImage(file=r"C:\Users\walid\Desktop\python-cryptage\Crips.png")
fenetre.iconphoto(True, image)

barre_menu = tk.Menu(fenetre)

onglet_cryps = tk.Menu(barre_menu, tearoff=0)
onglet_cryps.add_command(label="Crypter le fichier         CTRL+F", command=crypter_message)
onglet_cryps.add_command(label="Décrypter le fichier      CTRL+D", command=decrypter_message)
onglet_cryps.add_separator()
onglet_cryps.add_command(label="Quitter                          ALT+F4", command=quitter_application)
barre_menu.add_cascade(label="Cryps", menu=onglet_cryps)

onglet_help = tk.Menu(barre_menu, tearoff=0)
onglet_help.add_command(label="Aide", command=ouvrir_page_web)
onglet_help.add_command(label="À propos", command=ouvrir_page_about)
barre_menu.add_cascade(label="Help", menu=onglet_help)

fenetre.config(menu=barre_menu)

barre_horizontale = tk.Frame(fenetre, height=2, bg="#AAAAAA")
barre_horizontale.pack(fill=tk.X)

label_titre = tk.Label(fenetre, text="Cryps Software", font=("Helvetica", 16, "bold"))
label_titre.pack(pady=10)

couleur_bouton = "#E2E2E2"

cadre_gris = tk.Frame(fenetre, bg=couleur_bouton)
cadre_gris.pack(fill=tk.X, padx=5, pady=(0, 5))

image_crypter = tk.PhotoImage(file=r"C:\Users\walid\Desktop\python-cryptage\crypter.png")
bouton_crypter = tk.Button(cadre_gris, image=image_crypter, text="Crypter le document", compound=tk.TOP, command=crypter_message, bg=couleur_bouton)
bouton_crypter.grid(row=0, column=0, padx=10, pady=5)

barre_verticale = tk.Canvas(cadre_gris, bg="#AAAAAA", bd=0, highlightthickness=0, width=2, height=50)
barre_verticale.grid(row=0, column=1, sticky="ns", pady=5)

image_decrypter = tk.PhotoImage(file=r"C:\Users\walid\Desktop\python-cryptage\décrypter.png")
bouton_decrypter = tk.Button(cadre_gris, image=image_decrypter, text="Décrypter le document", compound=tk.TOP, command=decrypter_message, bg=couleur_bouton)
bouton_decrypter.grid(row=0, column=2, padx=10, pady=5)

image_help = tk.PhotoImage(file=r"C:\Users\walid\Desktop\python-cryptage\help.png") 
bouton_help = tk.Button(fenetre, image=image_help, command=ouvrir_page_web)
bouton_help.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)

label_bas = tk.Label(fenetre, text="Cryps Software @G7 Corp", font=("Helvetica", 10), fg="#A1A1A1")
label_bas.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10)

label_resultat = tk.Label(fenetre, text="")
label_resultat.pack(padx=20, pady=5)

fenetre.resizable(False, False)

fenetre.mainloop()
