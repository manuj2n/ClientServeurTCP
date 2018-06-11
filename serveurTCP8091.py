#! /usr/bin/python3
# -*- coding: utf-8 -*-
# manuj2n

import socket
import string

hote = '127.0.0.1'
port = 8091

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur ecoute sur le port {}".format(port))
connexion_avec_client, infos_connexion = connexion_principale.accept()
msg_recu = ""

while True:
    msg_recu = connexion_avec_client.recv(1024)
    if 'fin' in str(msg_recu):
        print("fin")
        break
    if 'von' in str(msg_recu):
        print("mise en route video")
    if 'voff' in str(msg_recu):
        print("arret de la video")
    if 'reboot' in str(msg_recu):
        print("redemarrage du system")
    print(msg_recu)
    connexion_avec_client.sendall(msg_recu)

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
exit(0)
