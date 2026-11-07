"""Funções para treinar, validar e comparar modelos de regressão."""
import pandas as pd
from sklearn.compose import TransformedTargetRegressor
from sklearn.model_selection import GridSearchCV, KFold, cross_validate
from sklearn.pipeline import Pipeline

METRICAS = {
    "MAE": "neg_mean_absolute_error",
    "RMSE": "neg_root_mean_squared_error",
    "R2": "r2",
}


def construir_modelo(regressor, preprocessamento=None, transformador_alvo=None):
    """Junta pré-processamento, regressor e transformação do alvo num só objeto."""
    passos = []
    if preprocessamento is not None:
        passos.append(("preprocessamento", preprocessamento))
    passos.append(("regressor", regressor))
    modelo = Pipeline(passos)
    if transformador_alvo is not None:
        modelo = TransformedTargetRegressor(regressor=modelo, transformer=transformador_alvo)
    return modelo


def validacao_cruzada(modelo, X, y, n_divisoes=5, semente=42):
    """Validação cruzada KFold. Devolve um DataFrame com uma linha por divisão."""
    kf = KFold(n_splits=n_divisoes, shuffle=True, random_state=semente)
    res = cross_validate(modelo, X, y, cv=kf, scoring=METRICAS, n_jobs=-1)
    tabela = pd.DataFrame({
        "MAE": -res["test_MAE"],
        "RMSE": -res["test_RMSE"],
        "R2": res["test_R2"],
        "tempo_s": res["fit_time"] + res["score_time"],
    })
    tabela.index.name = "divisao"
    return tabela


def comparar_modelos(modelos, X, y, n_divisoes=5, semente=42):
    """Corre a validação cruzada para cada modelo e junta tudo numa tabela longa."""
    partes = []
    for nome, modelo in modelos.items():
        t = validacao_cruzada(modelo, X, y, n_divisoes, semente).reset_index()
        t.insert(0, "modelo", nome)
        partes.append(t)
    return pd.concat(partes, ignore_index=True)


def resumo(resultados):
    """Média e desvio-padrão de cada métrica por modelo, ordenado pelo RMSE."""
    r = resultados.groupby("modelo")[["MAE", "RMSE", "R2"]].agg(["mean", "std"])
    return r.sort_values(("RMSE", "mean"))


def grid_search(modelo, grade, X, y, n_divisoes=5, semente=42):
    """GridSearchCV com o RMSE como critério de escolha."""
    kf = KFold(n_splits=n_divisoes, shuffle=True, random_state=semente)
    gs = GridSearchCV(modelo, grade, cv=kf, scoring=METRICAS, refit="RMSE", n_jobs=-1)
    gs.fit(X, y)
    return gs
