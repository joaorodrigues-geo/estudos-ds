#!/bin/bash
# Cria a pasta de um projeto novo a partir do _modelo.
# Uso (dentro de estudos-ds/hashtag):  ./novo_projeto.sh 14-regressao-linear
set -e
cd "$(dirname "$0")"
[ -z "$1" ] && { echo "Uso: ./novo_projeto.sh NN-nome-do-modulo"; exit 1; }
[ -e "$1" ] && { echo "Já existe: $1"; exit 1; }
cp -R _modelo "$1"
sed -i '' "s/^# Título do projeto.*/# $1/" "$1/README.md" 2>/dev/null || sed -i "s/^# Título do projeto.*/# $1/" "$1/README.md"
echo "Criado: hashtag/$1"
