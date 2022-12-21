# SupperSSH

**SupperSSH** est un script qui permet de lancer une liste de commandes predefinis par l'utilisateur sur plusieurs machines,
à l'aide de fichier contenants les adresses IPs et les commandes. 


Pour que cela marche il vous faut la libraire python [paramiko](https://www.paramiko.org/).

pour l'installer utiliser la commande suivante: ``pip install paramiko``.

Ensuite, il faut que vous placer vos fichiers contenant les adresses IPs et commandes dans leurs documents,
et nommees le fichier d'IPs: ``ip_liste.txt`` et le fichier de commandes: ``cmd_liste.txt``
