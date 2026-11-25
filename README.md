# astar-romenia

Busca A* de Arad a Bucareste (Russell & Norvig, cap. 3),
feita em 6 fases na disciplina Engenharia de Software.

Aluno(a): Thiago Luis Sabino Leão

## Por que o algoritmo A* encontra o caminho de menor custo?

O algoritmo A* tem como objetivo encontrar o caminho de menor custo entre uma cidade de origem e uma cidade de destino.

Para isso, utiliza a fórmula:

*f(n) = g(n) + h(n)*

Onde:

- *g(n):* representa o custo real do caminho percorrido desde a origem até a cidade atual.
- *h(n):* representa a estimativa da distância restante até o destino.
- *f(n):* representa o custo total estimado, resultado da soma de g(n) + h(n).

A cada etapa da busca, o algoritmo analisa as opções disponíveis na fronteira e seleciona o nó que apresenta o menor valor de f(n).

A heurística utilizada é admissível, pois nunca superestima o custo real restante até o destino. Essa característica permite que o A* encontre uma solução de menor custo.

### Exemplo prático: Arad até Bucareste

Foram comparados dois caminhos:

| Caminho | Distância |
|---|---:|
| Caminho por Fagaras | 450 km |
| Caminho por Pitesti | 418 km |

*Resultado:* o caminho por Pitesti apresenta o menor custo, totalizando 418 km.

### Conclusão

O A* encontra o caminho de menor custo porque considera tanto a distância já percorrida quanto a estimativa da distância que ainda falta. Assim, consegue avaliar as alternativas e priorizar os caminhos mais promissores até alcançar o destino.
