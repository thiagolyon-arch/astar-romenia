# -- coding: utf-8 --
# FASE 2 - CÁLCULO DOS CAMINHOS

# 1. IMPORTAÇÃO DOS DADOS
# Importa o mapa e as estimativas de distância até Bucareste.
from mapa import mapa_romenia, heuristica_bucareste


# 2. FUNÇÃO PARA CALCULAR O CUSTO DE UMA ESTRADA
# Procura a distância entre duas cidades conectadas.
def custo_da_estrada(origem, destino):

    # Percorre os vizinhos da cidade de origem.
    for vizinho, custo in mapa_romenia[origem]:

        # Verifica se o vizinho é o destino procurado.
        if vizinho == destino:
            return custo

    # Retorna None caso não exista uma estrada direta.
    return None


# 3. FUNÇÃO PARA CALCULAR O CUSTO DE UM CAMINHO
# Soma as distâncias de todas as estradas do trajeto.
def custo_do_caminho(caminho):

    total = 0

    for i in range(len(caminho) - 1):
        total = total + custo_da_estrada(
            caminho[i], caminho[i + 1]
        )

    return total
# É necessário o -1 pois entre 4 cidades, são elencados 3 caminhos

# 4. TESTE DAS FUNÇÕES
print('Arad -> Sibiu custa',
      custo_da_estrada('Arad', 'Sibiu'), 'km')

print('Arad -> Bucharest custa',
      custo_da_estrada('Arad', 'Bucharest'),
      '(não existe estrada direta)')


# 5. CRIAÇÃO E COMPARAÇÃO DE CAMINHOS
# Cria dois trajetos diferentes para comparar suas distâncias.
por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']

por_pitesti = [
    'Arad', 'Sibiu', 'Rimnicu Vilcea',
    'Pitesti', 'Bucharest'
]

print()
print('Caminho por Fagaras:', ' -> '.join(por_fagaras))
print('   custo =', custo_do_caminho(por_fagaras), 'km')

print('Caminho por Pitesti:', ' -> '.join(por_pitesti))
print('   custo =', custo_do_caminho(por_pitesti), 'km')


# 6. FUNÇÃO PARA CALCULAR g(n), h(n) E f(n)
# g = custo percorrido; h = estimativa restante; f = g + h.
def mostrar_g_h_f(caminho):

    print(f' {"cidade":<15} {"g(n)":>5} {"h(n)":>5} {"f(n)":>5}')

    for i in range(len(caminho)):

        cidade = caminho[i]

        # Calcula o custo acumulado desde Arad até a cidade atual.
        g = custo_do_caminho(caminho[:i + 1])

        h = heuristica_bucareste[cidade]

        # Soma o custo percorrido com a estimativa restante.
        f = g + h

        print(f' {cidade:<15} {g:>5} {h:>5} {f:>5}')


# 7. EXIBIÇÃO DOS RESULTADOS
print()
print('Valores ao longo do caminho por Fagaras:')
mostrar_g_h_f(por_fagaras)

print()
print('Valores ao longo do caminho por Pitesti:')
mostrar_g_h_f(por_pitesti)


# 8. CONSULTAS E VERIFICAÇÕES DO CÓDIGO
print("\n===== CONSULTAS DO PYTHON =====")

print("Tipo do mapa:", type(mapa_romenia))
print("Quantidade de cidades:", len(mapa_romenia))
print("Arad existe no mapa:", 'Arad' in mapa_romenia)
print("Cidades:", list(mapa_romenia.keys()))
print("Vizinhos de Arad:", mapa_romenia['Arad'])
print("Primeiro vizinho:", mapa_romenia['Arad'][0])
print("Tipo da distância:", type(mapa_romenia['Arad'][0][1]))

print("Arad está conectado a Sibiu:",
      'Sibiu' in [vizinho for vizinho, custo in mapa_romenia['Arad']])

print("Custo Arad-Sibiu:",
      custo_da_estrada('Arad', 'Sibiu'))

print("F = G + H:", 317 + 100)

print("===== FIM DAS CONSULTAS =====")