def crypter_message():
    print("Cryptage en cours...")
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            contenu = file.read()
            contenu_crypte = cryptage(contenu)
        file_path_crypte = file_path[:-4] + "_crypte.txt"  # Nom du nouveau fichier crypté
        with open(file_path_crypte, "w") as file_crypte:
            file_crypte.write(contenu_crypte)
        label_resultat.config(text="Le contenu du fichier texte a été crypté avec succès.")