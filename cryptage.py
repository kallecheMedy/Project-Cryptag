def cryptage(message):
    message_crypte = ""
    for caractere in message:
        if caractere.isalpha():
            if caractere.isupper():
                decalage_caractere = decalage
                lettre_debut = 'A'
            else:
                decalage_caractere = decalage + 32
                lettre_debut = 'a'
            index = ord(caractere) - ord(lettre_debut)
            index_crypte = (index + decalage_caractere) % 26
            lettre_cryptee = chr(ord(lettre_debut) + index_crypte)
            message_crypte += lettre_cryptee
        else:
            message_crypte += caractere
    return message_crypte