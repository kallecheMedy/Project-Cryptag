def decryptage(message_crypte):
    message_decrypte = ""
    for caractere in message_crypte:
        if caractere.isalpha():
            if caractere.isupper():
                decalage_caractere = decalage
                lettre_debut = 'A'
            else:
                decalage_caractere = decalage + 32
                lettre_debut = 'a'
            index = ord(caractere) - ord(lettre_debut)
            index_decrypte = (index - decalage_caractere) % 26
            lettre_decryptee = chr(ord(lettre_debut) + index_decrypte)
            message_decrypte += lettre_decryptee
        else:
            message_decrypte += caractere
    return message_decrypte