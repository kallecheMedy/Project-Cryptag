def decrypter_message():
    print("Décryptage en cours...")
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            contenu_crypte = file.read()
            contenu_decrypte = decryptage(contenu_crypte)
        file_path_decrypte = file_path[:-4] + "_decrypte.txt"  # Nom du nouveau fichier décrypté
        with open(file_path_decrypte, "w") as file_decrypte:
            file_decrypte.write(contenu_decrypte)
        label_resultat.config(text="Le contenu du fichier texte a été décrypté avec succès.")

