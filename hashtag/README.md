# Projetos do curso de Ciência de Dados (Hashtag Treinamentos)

Um projeto por módulo, a partir do módulo 13 (Machine Learning). Cada pasta segue a mesma estrutura (`_modelo/`): dados, notebooks numerados, referências e relatórios.

| Módulo | Projeto | Estado |
|---|---|---|
| 13 | [Introdução ao Machine Learning](13-introducao-machine-learning) | Em curso |

Os materiais e enunciados do curso não estão aqui: só o meu código e os meus resultados.

## Criar o projeto de um módulo novo

```bash
cd ~/Projetos/estudos-ds/hashtag
./novo_projeto.sh 14-nome-do-modulo
```

## Regras

- Dados brutos em `dados/brutos/` (fora do Git); tabelas finais em `dados/processados/`.
- Notebooks numerados: `01-jr-exploracao.ipynb`, `02-jr-modelo.ipynb`…
- Gráficos com `aplicar_estilo()` de `notebooks/src/graficos.py`.
- Separar treino e teste antes de olhar para os resultados; indicar as métricas no README.
