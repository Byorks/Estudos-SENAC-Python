import os
import time

# Limpar console
def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")


def carregamento_pontos():
    time.sleep(.5)
    print("...")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print(".")
    time.sleep(1)
