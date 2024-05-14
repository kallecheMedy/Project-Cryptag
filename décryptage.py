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