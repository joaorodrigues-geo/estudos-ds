"""Estilo dos gráficos com as cores da marca (sem as cores padrão do matplotlib)."""
import matplotlib as mpl
from cycler import cycler

CORES = {
    "navy": "#0B2A3C",
    "verde": "#1F6F50",
    "cinzento": "#4E5A63",
    "ocre": "#9C4E26",
    "areia": "#F4EFE6",
    "linha": "#DDD3C2",
}

# Ordem para séries categóricas. Para valores contínuos usar "cividis" ou "viridis".
PALETA = [CORES["navy"], CORES["verde"], CORES["cinzento"], CORES["ocre"]]


def aplicar_estilo():
    """Chamar uma vez no início do notebook."""
    mpl.rcParams.update({
        "axes.prop_cycle": cycler(color=PALETA),
        "image.cmap": "cividis",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": CORES["linha"],
        "axes.labelcolor": CORES["navy"],
        "axes.titlecolor": CORES["navy"],
        "axes.titleweight": "bold",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": CORES["linha"],
        "grid.linewidth": 0.6,
        "xtick.color": CORES["cinzento"],
        "ytick.color": CORES["cinzento"],
        "legend.frameon": False,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
    })


def rotular_barras(ax, formato="{:.0f}"):
    """Escreve o valor na ponta de cada barra (a cor nunca é a única pista)."""
    for barras in ax.containers:
        ax.bar_label(barras, fmt=formato, padding=3, color=CORES["navy"], fontsize=9)


def comparar_metricas(resultados, ordem=None, ficheiro=None):
    """Caixas das métricas da validação cruzada, um painel por métrica."""
    import matplotlib.pyplot as plt
    import seaborn as sns

    ordem = ordem or list(resultados.groupby("modelo")["RMSE"].mean().sort_values().index)
    fig, eixos = plt.subplots(1, 3, figsize=(14, 0.55 * len(ordem) + 2), sharey=True)
    for ax, metrica in zip(eixos, ["MAE", "RMSE", "R2"]):
        sns.boxplot(data=resultados, x=metrica, y="modelo", order=ordem, ax=ax,
                    color=CORES["linha"], linecolor=CORES["navy"], fliersize=0, width=0.55)
        sns.stripplot(data=resultados, x=metrica, y="modelo", order=ordem, ax=ax,
                      color=CORES["verde"], size=4)
        medias = resultados.groupby("modelo")[metrica].mean().reindex(ordem)
        for i, v in enumerate(medias):
            ax.text(v, i - 0.36, f"{v:.2f}", ha="center", fontsize=8, color=CORES["navy"])
        ax.set_title(metrica)
        ax.set_xlabel("")
        ax.set_ylabel("")
    fig.suptitle("Validação cruzada (5 divisões) — cada ponto é uma divisão", x=0.01, ha="left")
    fig.tight_layout()
    if ficheiro:
        fig.savefig(ficheiro)
    return fig


def coeficientes(df_coef, titulo="Coeficientes do modelo", ficheiro=None):
    """Barras horizontais dos coeficientes, com o valor escrito em cada barra."""
    import matplotlib.pyplot as plt

    df = df_coef.sort_values("coeficiente")
    cores = [CORES["cinzento"] if c < 0 else CORES["verde"] for c in df["coeficiente"]]
    fig, ax = plt.subplots(figsize=(8, 0.42 * len(df) + 1.5))
    barras = ax.barh(df.index, df["coeficiente"], color=cores)
    ax.bar_label(barras, fmt="{:.1f}", padding=3, fontsize=8, color=CORES["navy"])
    ax.axvline(0, color=CORES["cinzento"], linewidth=0.8)
    ax.margins(x=0.12)
    ax.set_title(titulo)
    ax.set_xlabel("Efeito na progressão da doença (variáveis padronizadas)")
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    if ficheiro:
        fig.savefig(ficheiro)
    return fig


def residuos(y_real, y_previsto, titulo="Resíduos no conjunto de teste", ficheiro=None):
    """Três vistas dos resíduos: real vs previsto, resíduo vs previsto e distribuição."""
    import matplotlib.pyplot as plt
    import numpy as np

    res = np.asarray(y_real) - np.asarray(y_previsto)
    fig, eixos = plt.subplots(1, 3, figsize=(15, 4.5))
    lim = [min(np.min(y_real), np.min(y_previsto)), max(np.max(y_real), np.max(y_previsto))]
    eixos[0].scatter(y_previsto, y_real, s=18, color=CORES["navy"], alpha=0.7)
    eixos[0].plot(lim, lim, color=CORES["ocre"], linewidth=1, label="previsão perfeita")
    eixos[0].set(xlabel="Previsto", ylabel="Real", title="Real vs previsto")
    eixos[0].legend()
    eixos[1].scatter(y_previsto, res, s=18, color=CORES["verde"], alpha=0.7)
    eixos[1].axhline(0, color=CORES["ocre"], linewidth=1)
    eixos[1].set(xlabel="Previsto", ylabel="Resíduo (real − previsto)", title="Resíduos vs previsto")
    eixos[2].hist(res, bins=20, color=CORES["navy"], alpha=0.85)
    eixos[2].axvline(0, color=CORES["ocre"], linewidth=1)
    eixos[2].set(xlabel="Resíduo", ylabel="Contagem", title="Distribuição dos resíduos")
    fig.suptitle(titulo, x=0.01, ha="left")
    fig.tight_layout()
    if ficheiro:
        fig.savefig(ficheiro)
    return fig
