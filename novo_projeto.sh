#!/bin/bash
# Cria um projeto novo a partir do _modelo.
# Uso (na raiz do repositório):  ./novo_projeto.sh machine-learning/classificacao-fraudes
set -e
cd "$(dirname "$0")"
[ -z "$1" ] && { echo "Uso: ./novo_projeto.sh area/nome-do-projeto"; exit 1; }
[ -e "$1" ] && { echo "Já existe: $1"; exit 1; }
mkdir -p "$(dirname "$1")"
cp -R _modelo "$1"
sed -i '' "s/^# Título do projeto.*/# $(basename "$1")/" "$1/README.md" 2>/dev/null || sed -i "s/^# Título do projeto.*/# $(basename "$1")/" "$1/README.md"
echo "Criado: $1"
