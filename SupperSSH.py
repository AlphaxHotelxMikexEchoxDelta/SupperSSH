import paramiko

print("""
   __|                              __|   __|  |  |
 \__ \  |  |  _ \  _ \   -_)   _| \__ \ \__ \  __ |
 ____/ \_,_| .__/ .__/ \___| _|   ____/ ____/ _| _|
            _|   _|
""")

# Liste d'IPs utiliser pour les connections
liste_IP = []
# Ajoutes les IPs du fichier 'ip_liste' dans la liste 'liste_IP'
def IP(liste_IP=liste_IP):
    ips = open("IP/ip_liste.txt")
    lines = ips.readlines()
    for line in lines:
        # change les '\n' des chaines de caracteres des valeurs de la liste
        ip = line.replace("\n","")
        liste_IP.append(ip)

# Liste de commandes utiliser pour les connections
liste_CMD = []
# Ajoutes les IPs du fichier 'cmd_liste' dans la liste 'liste_CMD'
def CMD(liste_CMD=liste_CMD):
    cmds = open("CMD/cmd_liste.txt")
    lines = cmds.readlines()
    for line in lines:
        # change les '\n' des chaines de caracteres des valeurs de la liste
        cmd = line.replace("\n","")
        liste_CMD.append(cmd)

# definir 'client'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# lance une commandes à l'aide de la methode 'exec_command()',
def runCommandes():
    for cmd in range(len(liste_CMD)):
        stdin, stdout, stderr = client.exec_command(liste_CMD[cmd])
        # Affiche les sorties des commandes envoyees
        print("---commandes {} envoye---".format(cmd+1))
        print("="*30,"\n",stdout,"\n","="*30)

# connection ssh à une machine, à laide de la librairie 'paramiko'
def connect(ip,port,name,passwd):
    client.connect(ip, port=port, username=name, password=passwd)
    # Une fois connecter, ont affiche:
    print("---connection reussi---")
    # Appelle la fonctin 'runCommandes()'
    runCommandes()
    # Arrete la connection ssh
    client.close()
    print("---connection terminee---")

def SupperSSH():
    # Definis les variables 'name' et 'passwd' avec des saisi d'utilisateur
    name = str(input("username: "))
    passwd = str(input("password: "))
    port = int(input("port:"))
    # Lance les connections
    try:
        IP()
    except:
        print("Erreur survenue dans la fonction 'IP()'\nverifier le fichier 'IP/ip_liste.txt'")
        print("voici votre liste d'adresses IP: ",liste_IP)

    try:
        CMD()
    except:
        print("Erreur survenue dans la fonction 'CMD()'\n! verifier le fichier 'CMD/cmd_liste.txt' !")
        print("\nvoici votre liste de commandes: ",liste_CMD)

    for ip in range(len(liste_IP)):
        connect(liste_IP[ip],port,name,passwd)

SupperSSH()
