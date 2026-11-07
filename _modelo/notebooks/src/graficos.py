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
