# Introdução ao Machine Learning

*Introduction to machine learning: concepts and first supervised models (Hashtag Treinamentos, module 13).*

> Em curso.

![Gráfico principal](relatorios/imagens/principal.png)

**Resultado principal:** uma frase com o número mais importante.

## Objetivo

Que pergunta o projeto responde e porque interessa (2–3 frases).

## Dados

Resumo dos dados usados. A lista completa, com fonte, data e licença, está em [`referencias/02_fontes.md`](referencias/02_fontes.md); o significado de cada coluna, em [`referencias/01_dicionario_de_dados.md`](referencias/01_dicionario_de_dados.md).

## Método

1. Limpeza e preparação (`notebooks/01-jr-...`)
2. Análise exploratória (`notebooks/02-jr-...`)
3. Modelo e validação (`notebooks/03-jr-...`): como se separaram treino e teste e que métricas se usaram.

## Resultados

Tabela ou gráficos com os números principais.

## Limitações

- O que os dados não permitem concluir.
- Fontes de erro conhecidas.

## Como reproduzir

```bash
conda env create -f ambiente.yml
conda activate nome-do-projeto
jupyter lab
```

Os dados brutos não estão no repositório: descarregar para `dados/brutos/` a partir das fontes indicadas.

## Licença

Código: MIT. Os dados mantêm a licença de cada fonte (ver `referencias/02_fontes.md`).
