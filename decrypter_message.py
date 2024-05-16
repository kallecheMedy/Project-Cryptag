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