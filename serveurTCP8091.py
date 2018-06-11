#! /usr/bin/python3
# -*- coding: utf-8 -*-
# manuj2n

import socket

hote = '127.0.0.1'
port = 8091

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur ecoute sur le port {}".format(port))
connexion_avec_client, infos_connexion = connexion_principale.accept()
msg_recu = ""
while msg_recu != "fin":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    print(msg_recu)
    chaine = msg_recu
    connexion_avec_client.sendall(chaine)

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
exit(0)
