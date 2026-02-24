"""
Vai ser nos ensinado a como padronizar dados
"""

dados = [" João ", "Maria", "Carlos", "Ana ", "Paulo "]
telefones = ["(11)98765-4321", "(21)92345-6789", "98765-1234"]

# removendo espaços
dados_limpos = [nome.strip() for nome in dados]
print(dados_limpos)

# Pegando os 3 primeiros carácteres dos nomes
iniciais = [nome[:3] for nome in dados_limpos]
print(iniciais)

# Removendo o ddd
telefones_padronizados = []

for tel in telefones:
    if tel.startswith("("):
        telefones_padronizados.append(tel[4:])
    else:
        telefones_padronizados.append(tel)

print(telefones_padronizados)
