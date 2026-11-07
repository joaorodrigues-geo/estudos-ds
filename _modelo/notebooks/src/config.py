from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"
PASTA_BRUTOS = PASTA_DADOS / "brutos"            # originais, nunca editar (fora do Git)
PASTA_INTERMEDIOS = PASTA_DADOS / "intermedios"  # gerados por scripts (fora do Git)
PASTA_PROCESSADOS = PASTA_DADOS / "processados"  # tabelas finais (no Git)

# caminho para os dados do projeto
DADOS_ORIGINAIS = PASTA_BRUTOS / "nome_do_ficheiro.csv"  # mudar para o ficheiro do projeto

PASTA_MODELOS = PASTA_PROJETO / "modelos"
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"

SEMENTE = 42  # semente fixa para resultados reprodutíveis
