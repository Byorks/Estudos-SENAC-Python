'''
 ---- Callbacks -----
 Se trata de colocar funções como argumento de outras funções, fazendo uma execução mais tardia

'''
import time

# Exemplo de callbacks com Marvel Rivals
ultimate_status = "carregada"
momento_certo = False

def ativar_ultimate(momento_certo):
    if momento_certo == True:
        print("Homem-aranha: I'm Spider-man!")
    else:
        print("Aguardando o momento certo pra ultar")


def segurar_ultimate():
    print("Aguardando o momento certo pra ultar")


def carregar_ultimate(callback):
    print("ultimante carregando...")
    time.sleep(2)
    if ultimate_status == "carregada":
        print("Ultimate carregada")
        callback(momento_certo)


carregar_ultimate(ativar_ultimate)
