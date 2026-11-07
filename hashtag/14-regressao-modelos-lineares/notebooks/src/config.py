from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"
PASTA_BRUTOS = PASTA_DADOS / "brutos"            # originais, nunca editar (fora do Git)
PASTA_INTERMEDIOS = PASTA_DADOS / "intermedios"  # gerados por scripts (fora do Git)
PASTA_PROCESSADOS = PASTA_DADOS / "processados"  # tabelas finais (no Git)

DADOS_ORIGINAIS = PASTA_BRUTOS / "diabetes_original.csv"
DADOS_TRATADOS = PASTA_PROCESSADOS / "diabetes_tratado.csv"


PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"

SEMENTE = 42  # semente fixa para resultados reprodutíveis
