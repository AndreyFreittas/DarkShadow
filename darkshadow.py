import sys
import socket
from datetime import datetime

def banner():
    print("""
██████╗  █████╗ ██████╗ ██╗  ██╗███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
██║  ██║███████║██████╔╝█████╔╝ ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
██║  ██║██╔══██║██╔══██╗██╔═██╗ ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
██████╔╝██║  ██║██║  ██║██║  ██╗███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝
""")


banner()

print('\nDesenvolvido por: https://github.com/AndreyFreittas\n')


if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("\n[ERRO] Nome do host não pôde ser resolvido.")
        sys.exit()
else:
    print("Uso incorreto do script.")
    print(f"Modo de uso: python {sys.argv[0]} <endereço IP ou hostname>")
    sys.exit()


print("-" * 50)
print("Alvo do scan: " + target)
print("Início da varredura em: " + str(datetime.now()))
print("-" * 50)


try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[ABERTA] Porta {port}")
        s.close()

except KeyboardInterrupt:
    print("\n[INTERROMPIDO] Execução cancelada pelo usuário.")
    sys.exit()

except socket.error:
    print("\n[ERRO] O servidor não está respondendo.")
    sys.exit()
