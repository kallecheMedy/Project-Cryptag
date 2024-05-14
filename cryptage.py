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