# ---- Tuplas ----
"""
Não podem ser alteradas após sua criação
"""

minha_tupla = (1, 2, 3)

"""
Corroborando com nossos exemplos, podemos representar coordenadas geográficas e cores utilizando tuplas, conforme segue.
"""
lat_long_senac = (-23.668559, -46.702251) #coordenada geográfica
vermelho_rgb = (255, 0, 0) #rgb
amarelo_cmyk = (0, 0, 100, 0) #cmky

## A tupla permite outros tipos de dados
info_cor = ('Vermelho', (255, 0, 0), '#FF0000', True)
print(info_cor)
# Saída: (‘Vermelho’, (255, 0, 0), ‘#FF0000’, True)

"""
As tuplas em Python possuem uma opção de desempacotamento, o qual seria o processo simplificado de atribuição dos dados da tupla a variáveis individuais. Observe o exemplo 3.
"""
r, g, b = vermelho_rgb
print(f'R: {r}, G: {g}, B: {b}')	# Saída: R: 255, G: 0, B: 0


"""
As tuplas desempenham um papel fundamental na matemática e na computação em Python, pois oferecem uma maneira eficiente e estruturada de representar conjuntos imutáveis de valores. Sua imutabilidade garante segurança em operações que exigem dados fixos, como coordenadas cartesianas, vetores, pontos em gráficos, constantes físicas e representações de cores nos modelos RGB e CMYK, em que cada cor pode ser armazenada como uma tupla de três ou quatro valores, respectivamente. Além disso, a capacidade das tuplas de armazenar diferentes tipos de dados as torna ideais para representar estruturas heterogêneas, como registros de banco de dados, informações de configuração e agrupamentos de valores matemáticos em álgebra linear e geometria computacional. Seu desempenho superior em relação às listas, devido à otimização interna de armazenamento, faz das tuplas uma escolha eficiente para aplicações que exigem integridade dos dados e processamento rápido.


"""
