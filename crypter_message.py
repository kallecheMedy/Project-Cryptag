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