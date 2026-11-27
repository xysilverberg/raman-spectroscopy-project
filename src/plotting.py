"""Publication-quality figure generation adhering to PaperB_plots.ipynb styling and antislop guidelines."""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=SMALL_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)
plt.rc('xtick', labelsize=MEDIUM_SIZE)
plt.rc('ytick', labelsize=MEDIUM_SIZE)
plt.rc('axes', labelsize=BIGGER_SIZE)
plt.rc('axes', titlesize=BIGGER_SIZE)

OUTPUT_FIGURES_DIR = Path("outputs/figures")
OUTPUT_FIGURES_DIR.mkdir(parents=True, exist_ok=True)
PAPER_COMPUTATIONAL_DIR = Path("paper/figures/computational")
PAPER_COMPUTATIONAL_DIR.mkdir(parents=True, exist_ok=True)

COLORS = {
    "graphene": "#1f77b4",
    "graphene_bilayer": "#2ca02c",
    "graphene_defective": "#d62728",
    "swcnt_metallic": "#9467bd",
    "swcnt_semiconducting": "#ff7f0e",
    "graphene_hbn": "#17becf",
    "hbn_pure": "#8c564b",
    "baseline": "#7f7f7f",
    "residual": "#e377c2",
    "fit": "#bcbd22",
}


def apply_axes_style(ax, xlabel: str = r"Raman shift (cm$^{-1}$)", ylabel: str = "Intensity (counts)"):
    """Apply standard clean axes styling with auto minor locators and tight spines."""
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="both", direction="in", top=True, right=True)
    ax.tick_params(which="major", length=6, width=1.0)
    ax.tick_params(which="minor", length=3, width=0.8)
    for spine in ax.spines.values():
        spine.set_linewidth(1.0)


def save_publication_figure(fig, filename_stem: str):
    """Save high-resolution figures to outputs/figures/ and paper/figures/computational/ in PDF and PNG."""
    fig.tight_layout()
    for directory in [OUTPUT_FIGURES_DIR, PAPER_COMPUTATIONAL_DIR]:
        pdf_path = directory / f"{filename_stem}.pdf"
        png_path = directory / f"{filename_stem}.png"
        fig.savefig(pdf_path, bbox_inches="tight")
        fig.savefig(png_path, dpi=300, bbox_inches="tight")
    print(f"Saved figure: {filename_stem}.pdf & {filename_stem}.png")
