import socket
import sys
from datetime import datetime
import pyfiglet


ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

remoteServerIP = input('Entrez l\'IP d\'une machine à scanner : ')

print('-' * 60)
print('Lancement du scan des ports de la machine  ' + remoteServerIP)
print('-' * 60)

t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print('Port {}:   Ouvert'.format(port))
        sock.close()
    t2 = datetime.now()

    total = t2 - t1
    print('Scan complété en: {}'.format(str(total)))

except KeyboardInterrupt:
    print('Vous avez appuyez sur CTRL+C.')
    sys.exit()
except socket.gaierror:
    print("\n Le nom d'hôte n'a pas pu être résolu.")
    sys.exit()
except socket.error:
    print('Impossible de se connecter au serveur.')
    sys.exit()
