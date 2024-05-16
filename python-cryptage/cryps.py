import os
import tkinter as tk
import webbrowser
from tkinter import messagebox, filedialog

# Obtenez le chemin absolu du répertoire où se trouve le script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Chemins relatifs des images
image_path_cripsy = os.path.join(script_directory, "img", "Crips.png")
image_path_crypter = os.path.join(script_directory, "img", "crypter.png")
image_path_decrypter = os.path.join(script_directory, "img", "décrypter.png")
image_path_help = os.path.join(script_directory, "img", "help.png")

# Clé de chiffrement (décalage)
decalage = 3

# Fonction de cryptage
def cryptage(message):
    message_crypte = ""
    for caractere in message:
        if ord(caractere) >= 32 and ord(caractere) <= 126:  # Vérifier si le caractère est imprimable
            index = ord(caractere) - 32  # Décalage par rapport au premier caractère imprimable
            index_crypte = (index + decalage) % 95  # 95 caractères imprimables ASCII de l'espace à ~
            caractere_crypte = chr(index_crypte + 32)  # Décaler à nouveau pour obtenir le caractère crypté
            message_crypte += caractere_crypte
        else:
            message_crypte += caractere
    return message_crypte

# Fonction de décryptage
def decryptage(message_crypte):
    message_decrypte = ""
    for caractere in message_crypte:
        if ord(caractere) >= 32 and ord(caractere) <= 126:  # Vérifier si le caractère est imprimable
            index = ord(caractere) - 32  # Décalage par rapport au premier caractère imprimable
            index_decrypte = (index - decalage) % 95  # 95 caractères imprimables ASCII de l'espace à ~
            caractere_decrypte = chr(index_decrypte + 32)  # Décaler à nouveau pour obtenir le caractère décrypté
            message_decrypte += caractere_decrypte
        else:
            message_decrypte += caractere
    return message_decrypte

# Fonction pour enregistrer le fichier crypté
def enregistrer_fichier_crypte(contenu_crypte):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
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
    # Chemin absolu du fichier HTML local
    path = os.path.abspath(os.path.join(script_directory, "web", "help.html"))
    # Ouvrir le fichier HTML dans le navigateur par défaut
    webbrowser.open("file://" + path)

def ouvrir_page_about():
    path = os.path.abspath(os.path.join(script_directory, "web", "àproposde.html"))
    webbrowser.open("file://" + path)

# Fonction pour crypter le fichier
def crypter_message():
    print("Cryptage en cours...")
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            contenu = file.read()
            contenu_crypte = cryptage(contenu)
        with open(file_path, "w") as file:  # Utilisation de "w" pour écraser le contenu existant
            file.write(contenu_crypte)
        label_resultat.config(text="Le contenu du fichier texte a été crypté avec succès.")

def decrypter_message():
    print("Décryptage en cours...")
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            contenu_crypte = file.read()
            contenu_decrypte = decryptage(contenu_crypte)
        with open(file_path, "w") as file:  # Utilisation de "w" pour écraser le contenu existant
            file.write(contenu_decrypte)
        label_resultat.config(text="Le contenu du fichier texte a été décrypté avec succès.")


fenetre = tk.Tk()
fenetre.title("Cryps Software")

# Charger les images
image_cripsy = tk.PhotoImage(file=image_path_cripsy)
image_crypter = tk.PhotoImage(file=image_path_crypter)
image_decrypter = tk.PhotoImage(file=image_path_decrypter)
image_help = tk.PhotoImage(file=image_path_help)

fenetre.iconphoto(True, image_cripsy)

barre_menu = tk.Menu(fenetre)

onglet_cryps = tk.Menu(barre_menu, tearoff=0)
onglet_cryps.add_command(label="Crypter le fichier", command=crypter_message)
onglet_cryps.add_command(label="Décrypter le fichier", command=decrypter_message)
onglet_cryps.add_separator()
onglet_cryps.add_command(label="Quitter", command=quitter_application)
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

bouton_crypter = tk.Button(cadre_gris, image=image_crypter, text="Crypter le document", compound=tk.TOP, command=crypter_message, bg=couleur_bouton)
bouton_crypter.grid(row=0, column=0, padx=10, pady=5)

barre_verticale = tk.Canvas(cadre_gris, bg="#AAAAAA", bd=0, highlightthickness=0, width=2, height=50)
barre_verticale.grid(row=0, column=1, sticky="ns", pady=5)

bouton_decrypter = tk.Button(cadre_gris, image=image_decrypter, text="Décrypter le document", compound=tk.TOP, command=decrypter_message, bg=couleur_bouton)
bouton_decrypter.grid(row=0, column=2, padx=10, pady=5)

bouton_help = tk.Button(fenetre, image=image_help, command=ouvrir_page_web)
bouton_help.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)

label_bas = tk.Label(fenetre, text="Cryps Software @G7 Corp", font=("Helvetica", 10), fg="#A1A1A1")
label_bas.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10)

label_resultat = tk.Label(fenetre, text="")
label_resultat.pack(padx=20, pady=5)

fenetre.resizable(False, False)

fenetre.mainloop()
