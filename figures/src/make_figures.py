#!/usr/bin/env python3
"""Generate original journal figures for the maintenance–reserve–gating model."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Mapping

os.environ.setdefault("SOURCE_DATE_EPOCH", "0")

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


DEFAULT_PARAMETERS: dict[str, float] = {
    "gate_k": 2.0,
    "gate_n": 4.0,
    "activation_k": 1.35,
    "activation_n": 4.0,
    "uptake_efficiency": 1.05,
    "reserve": 5.0,
    "leak_rate": 0.35,
    "external_equilibrium": 0.15,
    "basal_consumption": 0.12,
    "activity_consumption": 2.15,
    "genetic_age_drain": 0.25,
}


def gating_components(
    exposure: np.ndarray,
    parameters: Mapping[str, float],
) -> dict[str, np.ndarray]:
    """Evaluate one explicitly illustrative, dimensionless gating model."""

    x = np.asarray(exposure, dtype=float)
    if np.any(x < 0):
        raise ValueError("exposure values must be non-negative")

    gate = x ** parameters["gate_n"] / (
        parameters["gate_k"] ** parameters["gate_n"]
        + x ** parameters["gate_n"]
    )
    activation = x ** parameters["activation_n"] / (
        parameters["activation_k"] ** parameters["activation_n"]
        + x ** parameters["activation_n"]
    )
    uptake = gate * parameters["uptake_efficiency"] * x
    leak = (
        parameters["leak_rate"]
        * gate
        * np.maximum(
            parameters["reserve"] - parameters["external_equilibrium"] * x,
            0.0,
        )
    )
    consumption = (
        parameters["basal_consumption"]
        + parameters["activity_consumption"] * activation
        + parameters["genetic_age_drain"]
    )
    net_reserve_change = uptake - leak - consumption
    return {
        "gate": gate,
        "activation": activation,
        "uptake": uptake,
        "leak": leak,
        "consumption": consumption,
        "net_reserve_change": net_reserve_change,
    }


def relative_depletion_pressure(net_reserve_change: np.ndarray) -> np.ndarray:
    """Return non-negative modeled depletion pressure scaled to [0, 1]."""

    loss = np.maximum(-np.asarray(net_reserve_change, dtype=float), 0.0)
    maximum = float(loss.max()) if loss.size else 0.0
    return loss / maximum if maximum > 0 else loss


COLORS = {
    "ink": "#162536",
    "muted": "#66788A",
    "grid": "#D8E0E7",
    "known": "#2F5D8A",
    "known_fill": "#E9F1F8",
    "measure": "#24776E",
    "measure_fill": "#E6F4F1",
    "hypothesis": "#B96B25",
    "hypothesis_fill": "#FFF1E3",
    "harm": "#9C3F50",
    "harm_fill": "#F8E8EC",
    "balance": "#287D61",
}


def _configure_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "axes.titlesize": 10,
            "axes.labelsize": 8.5,
            "axes.edgecolor": COLORS["ink"],
            "axes.labelcolor": COLORS["ink"],
            "xtick.color": COLORS["ink"],
            "ytick.color": COLORS["ink"],
            "text.color": COLORS["ink"],
            "svg.fonttype": "none",
            "svg.hashsalt": "maintenance-reserve-gating-v0.1.0",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "savefig.facecolor": "white",
        }
    )


def _box(
    ax,
    xy: tuple[float, float],
    width: float,
    height: float,
    text: str,
    *,
    edge: str,
    fill: str,
    fontsize: float = 8.0,
    linewidth: float = 1.2,
) -> None:
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.012,rounding_size=0.012",
        linewidth=linewidth,
        edgecolor=edge,
        facecolor=fill,
        zorder=2,
    )
    ax.add_patch(patch)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        linespacing=1.18,
        zorder=3,
    )


def _arrow(
    ax,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    color: str,
    dashed: bool = False,
    curve: float = 0.0,
    linewidth: float = 1.25,
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=9,
            linewidth=linewidth,
            linestyle=(0, (4, 3)) if dashed else "solid",
            color=color,
            connectionstyle=f"arc3,rad={curve}",
            shrinkA=2,
            shrinkB=2,
            zorder=1,
        )
    )


def _save(fig: mpl.figure.Figure, output_dir: Path, stem: str) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for suffix, kwargs in (
        (
            "svg",
            {
                "metadata": {
                    "Date": None,
                    "Creator": "cerebellar-maintenance-reserve-gating-hypothesis",
                }
            },
        ),
        (
            "pdf",
            {
                "metadata": {
                    "CreationDate": None,
                    "ModDate": None,
                    "Creator": "cerebellar-maintenance-reserve-gating-hypothesis",
                    "Producer": "Matplotlib",
                }
            },
        ),
        (
            "png",
            {
                "dpi": 600,
                "metadata": {
                    "Software": "cerebellar-maintenance-reserve-gating-hypothesis"
                },
            },
        ),
    ):
        destination = output_dir / f"{stem}.{suffix}"
        fig.savefig(destination, bbox_inches="tight", pad_inches=0.05, **kwargs)
        if suffix == "svg":
            svg_text = destination.read_text(encoding="utf-8")
            normalized = "\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n"
            destination.write_text(normalized, encoding="utf-8", newline="\n")
        outputs.append(destination)
    eps_name = {
        "fig1-framework": "Fig1.eps",
        "fig2-nonlinear-gating": "Fig2.eps",
        "fig3-study-program": "Fig3.eps",
    }[stem]
    fig.savefig(
        output_dir / eps_name,
        format="eps",
        bbox_inches="tight",
        pad_inches=0.05,
        metadata={"Creator": "cerebellar-maintenance-reserve-gating-hypothesis"},
    )
    plt.close(fig)
    return outputs


def _figure_framework(output_dir: Path) -> list[Path]:
    fig, ax = plt.subplots(figsize=(7.35, 4.65))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.01,
        0.965,
        "A nested, falsifiable maintenance–reserve–gating model",
        fontsize=11,
        fontweight="bold",
        va="top",
    )

    _box(
        ax,
        (0.03, 0.72),
        0.16,
        0.11,
        "Genotype G\nknown modifiers",
        edge=COLORS["known"],
        fill=COLORS["known_fill"],
        fontsize=7.0,
    )
    _box(
        ax,
        (0.25, 0.72),
        0.18,
        0.11,
        "Known pressure $D_G$\nprotein | Ca²⁺ | ER",
        edge=COLORS["known"],
        fill=COLORS["known_fill"],
        fontsize=6.8,
    )
    _box(
        ax,
        (0.03, 0.44),
        0.16,
        0.11,
        "Measured E(t)\nprelocked E*",
        edge=COLORS["measure"],
        fill=COLORS["measure_fill"],
        fontsize=6.8,
    )
    _box(
        ax,
        (0.25, 0.44),
        0.18,
        0.11,
        "Candidate score S*(t)\nfixed map h(E*; θ)",
        edge=COLORS["hypothesis"],
        fill=COLORS["hypothesis_fill"],
        fontsize=6.2,
    )
    _box(
        ax,
        (0.03, 0.18),
        0.16,
        0.11,
        "Baseline reserve B₀\nhypothetical",
        edge=COLORS["hypothesis"],
        fill=COLORS["hypothesis_fill"],
        fontsize=7.0,
    )
    _box(
        ax,
        (0.44, 0.45),
        0.09,
        0.09,
        "φ(S*)→X(t)\nhypothetical",
        edge=COLORS["hypothesis"],
        fill=COLORS["hypothesis_fill"],
        fontsize=5.0,
    )
    _box(
        ax,
        (0.54, 0.51),
        0.14,
        0.13,
        "Coupling R | gate P(X)\nactivation / exchange",
        edge=COLORS["hypothesis"],
        fill=COLORS["hypothesis_fill"],
        fontsize=5.5,
    )
    _box(
        ax,
        (0.48, 0.25),
        0.17,
        0.13,
        "Reserve B(t)\nU − outward loss ℒ\n− demand",
        edge=COLORS["hypothesis"],
        fill=COLORS["hypothesis_fill"],
        fontsize=6.0,
    )
    _box(
        ax,
        (0.70, 0.32),
        0.16,
        0.15,
        "Candidate factor L(t)\nNfL | MRI/MRS\nphysiology | digital",
        edge=COLORS["hypothesis"],
        fill=COLORS["hypothesis_fill"],
        fontsize=6.2,
    )
    _box(
        ax,
        (0.70, 0.68),
        0.16,
        0.15,
        "Network state\nPurkinje | glia\nMLIN | synapses",
        edge=COLORS["known"],
        fill=COLORS["known_fill"],
        fontsize=6.5,
    )
    _box(
        ax,
        (0.89, 0.60),
        0.095,
        0.17,
        "Dysfunction\n↓\nDegeneration",
        edge=COLORS["harm"],
        fill=COLORS["harm_fill"],
        fontsize=6.5,
    )

    _arrow(ax, (0.19, 0.775), (0.25, 0.775), color=COLORS["known"])
    _arrow(ax, (0.43, 0.775), (0.70, 0.755), color=COLORS["known"])
    _arrow(ax, (0.19, 0.495), (0.25, 0.495), color=COLORS["measure"])
    _arrow(ax, (0.43, 0.495), (0.44, 0.495), color=COLORS["hypothesis"], dashed=True)
    _arrow(ax, (0.53, 0.495), (0.54, 0.565), color=COLORS["hypothesis"], dashed=True)
    _arrow(ax, (0.19, 0.235), (0.48, 0.315), color=COLORS["hypothesis"], dashed=True, curve=-0.08)
    _arrow(ax, (0.61, 0.51), (0.61, 0.38), color=COLORS["hypothesis"], dashed=True)
    ax.plot(
        [0.65, 0.675, 0.675],
        [0.315, 0.315, 0.68],
        color=COLORS["hypothesis"],
        lw=1.2,
        linestyle=(0, (4, 3)),
        solid_capstyle="round",
        zorder=1,
    )
    _arrow(ax, (0.675, 0.68), (0.70, 0.71), color=COLORS["hypothesis"], dashed=True)
    _arrow(ax, (0.78, 0.68), (0.78, 0.47), color=COLORS["hypothesis"], dashed=True)
    _arrow(ax, (0.86, 0.755), (0.89, 0.685), color=COLORS["known"])
    _arrow(ax, (0.17, 0.72), (0.54, 0.60), color=COLORS["hypothesis"], dashed=True, curve=0.22)

    ax.plot([0.04, 0.09], [0.055, 0.055], color=COLORS["known"], lw=1.4)
    ax.text(0.10, 0.055, "empirically supported link", va="center", fontsize=7.2)
    ax.plot(
        [0.31, 0.36],
        [0.055, 0.055],
        color=COLORS["hypothesis"],
        lw=1.4,
        linestyle=(0, (4, 3)),
    )
    ax.text(0.37, 0.055, "hypothesis-specific link", va="center", fontsize=7.2)
    ax.text(
        0.67,
        0.055,
        "L is inferred from Y—not a causal substance",
        va="center",
        fontsize=7.2,
        color=COLORS["muted"],
    )
    return _save(fig, output_dir, "fig1-framework")


def _figure_gating(output_dir: Path) -> list[Path]:
    x = np.linspace(0, 10, 1001)
    values = gating_components(x, DEFAULT_PARAMETERS)
    pressure = relative_depletion_pressure(values["net_reserve_change"])
    minimum_x = x[np.argmin(values["net_reserve_change"])]
    crossing_indices = np.where(np.diff(np.signbit(values["net_reserve_change"])))[0]
    balance_x = x[crossing_indices[-1]] if len(crossing_indices) else 10

    fig, axes = plt.subplots(
        3,
        1,
        figsize=(7.35, 6.1),
        sharex=True,
        gridspec_kw={"height_ratios": [0.9, 1.15, 1.0], "hspace": 0.18},
    )
    fig.suptitle(
        "Predicted non-monotonic input response under one illustrative parameter set",
        x=0.02,
        y=0.99,
        ha="left",
        fontsize=11,
        fontweight="bold",
    )

    zones = (
        (0.0, 1.0, "I  idle", "#EEF3F7"),
        (1.0, 3.4, "II  danger", "#FCE9E5"),
        (3.4, float(balance_x), "III  supply ↑", "#FFF3DF"),
        (float(balance_x), 10.0, "IV  rebalance", "#E7F4EE"),
    )
    for ax in axes:
        for left, right, _, color in zones:
            ax.axvspan(left, right, color=color, zorder=0)
        ax.grid(axis="y", color=COLORS["grid"], lw=0.6, zorder=0)
        ax.spines[["top", "right"]].set_visible(False)

    axes[0].plot(x, values["activation"], color=COLORS["harm"], lw=2.0, label="module activation A(X)")
    axes[0].plot(x, values["gate"], color=COLORS["hypothesis"], lw=2.0, label="exchange gate P(X)")
    axes[0].set_ylabel("Fraction open / active")
    axes[0].set_ylim(-0.03, 1.08)
    axes[0].legend(frameon=False, ncol=2, loc="lower right", fontsize=7.6)

    axes[1].plot(x, values["uptake"], color=COLORS["balance"], lw=2.2, label="uptake U")
    axes[1].plot(x, values["consumption"], color=COLORS["harm"], lw=2.0, label="consumption M + D")
    axes[1].plot(x, values["leak"], color=COLORS["hypothesis"], lw=2.0, label="outward loss ℒ")
    axes[1].set_ylabel("Illustrative flux\n(arbitrary units)")
    axes[1].legend(frameon=False, ncol=3, loc="upper left", fontsize=7.4)

    net = values["net_reserve_change"]
    axes[2].axhline(0, color=COLORS["ink"], lw=0.9)
    axes[2].plot(x, net, color=COLORS["ink"], lw=2.2, label="dB/dt")
    axes[2].fill_between(x, net, 0, where=net < 0, color=COLORS["harm"], alpha=0.20)
    axes[2].fill_between(x, net, 0, where=net >= 0, color=COLORS["balance"], alpha=0.20)
    axes[2].plot(x, pressure * 2.3, color=COLORS["harm"], lw=1.3, ls=(0, (4, 2)), label="relative depletion pressure (scaled)")
    axes[2].scatter([minimum_x], [net.min()], s=24, color=COLORS["harm"], zorder=5)
    axes[2].annotate(
        "maximal modeled loss",
        xy=(minimum_x, net.min()),
        xytext=(minimum_x + 0.6, net.min() - 0.9),
        arrowprops={"arrowstyle": "->", "color": COLORS["harm"], "lw": 0.9},
        fontsize=7.4,
        color=COLORS["harm"],
    )
    axes[2].annotate(
        "net balance restored",
        xy=(balance_x, 0),
        xytext=(balance_x + 0.4, -1.7),
        arrowprops={"arrowstyle": "->", "color": COLORS["balance"], "lw": 0.9},
        fontsize=7.4,
        color=COLORS["balance"],
    )
    axes[2].set_ylabel("Net reserve change")
    axes[2].set_xlabel("Hypothetical maintenance input X (dimensionless)")
    axes[2].legend(frameon=False, ncol=2, loc="upper left", fontsize=7.4)

    for left, right, label, _ in zones:
        midpoint = (left + right) / 2
        axes[0].text(
            midpoint,
            1.055,
            label,
            ha="center",
            va="bottom",
            fontsize=7.0,
            color=COLORS["muted"],
        )

    fig.text(
        0.985,
        0.012,
        "Hypothetical X axis; X=S only for display. Illustration, not patient data.\nZone boundaries depend on fixed model parameters shown in source.",
        ha="right",
        fontsize=7.0,
        color=COLORS["muted"],
    )
    return _save(fig, output_dir, "fig2-nonlinear-gating")


def _figure_program(output_dir: Path) -> list[Path]:
    fig, ax = plt.subplots(figsize=(8.0, 5.45))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(
        0.01,
        0.965,
        "Prospective validation and gated early-intervention programme",
        fontsize=11,
        fontweight="bold",
        va="top",
    )

    _box(
        ax,
        (0.04, 0.68),
        0.20,
        0.15,
        "5-y natural history\nSCA3 primary test bed\nSCA6 transport test | controls",
        edge=COLORS["measure"],
        fill=COLORS["measure_fill"],
        fontsize=6.5,
    )
    _box(
        ax,
        (0.31, 0.70),
        0.18,
        0.13,
        "Locked E* → S*\nwindow + h + knots\nfrozen pre-outcome",
        edge=COLORS["hypothesis"],
        fill=COLORS["hypothesis_fill"],
        fontsize=6.8,
    )
    _box(
        ax,
        (0.56, 0.70),
        0.18,
        0.13,
        "Nested models\nSCA3 H1\n+ external replication\nSCA6 transport + G×S*",
        edge=COLORS["known"],
        fill=COLORS["known_fill"],
        fontsize=5.9,
    )
    _box(
        ax,
        (0.80, 0.67),
        0.17,
        0.18,
        "Statistical result\nG×S* + non-linearity\nnot gate proof\nnot outward-loss proof",
        edge=COLORS["harm"],
        fill=COLORS["harm_fill"],
        fontsize=5.5,
    )
    _arrow(ax, (0.24, 0.755), (0.31, 0.765), color=COLORS["measure"])
    _arrow(ax, (0.49, 0.765), (0.56, 0.765), color=COLORS["known"])
    _arrow(ax, (0.74, 0.765), (0.80, 0.765), color=COLORS["harm"])

    ax.text(
        0.04,
        0.59,
        "Known-target examples: independent evidence gates govern every intervention module",
        fontsize=8.2,
        fontweight="bold",
    )
    ax.plot([0.04, 0.96], [0.565, 0.565], color=COLORS["grid"], lw=1.0)

    _box(
        ax,
        (0.06, 0.28),
        0.27,
        0.20,
        "Known-target example: SCA3\nmutant-ATXN3 lowering\nOnly after safety, dose\n+ CSF target engagement",
        edge=COLORS["known"],
        fill=COLORS["known_fill"],
        fontsize=6.6,
    )
    _box(
        ax,
        (0.365, 0.28),
        0.27,
        0.20,
        "Known-target example: SCA6\nL-arginine uncertainty\nRandomized clinical benefit\n+ enhanced safety monitoring",
        edge=COLORS["measure"],
        fill=COLORS["measure_fill"],
        fontsize=6.6,
    )
    _box(
        ax,
        (0.67, 0.28),
        0.27,
        0.20,
        "Circuit phase 0 (conditional)\nReliable human classifier\nPrecedes decline | normalizes\nWashout reversibility",
        edge=COLORS["hypothesis"],
        fill=COLORS["hypothesis_fill"],
        fontsize=6.6,
    )
    ax.plot([0.195, 0.805], [0.535, 0.535], color=COLORS["grid"], lw=1.2)
    _arrow(ax, (0.195, 0.535), (0.195, 0.48), color=COLORS["known"])
    _arrow(ax, (0.50, 0.535), (0.50, 0.48), color=COLORS["measure"])
    _arrow(ax, (0.805, 0.535), (0.805, 0.48), color=COLORS["hypothesis"], dashed=True)

    ax.text(
        0.185,
        0.21,
        "Target engagement + disease-activity MRI\nnot X validation",
        ha="center",
        fontsize=6.5,
        color=COLORS["muted"],
    )
    ax.text(
        0.50,
        0.21,
        "Clinical efficacy + withdrawal pattern\nnot a validated surrogate claim",
        ha="center",
        fontsize=6.5,
        color=COLORS["muted"],
    )
    ax.text(
        0.815,
        0.21,
        "Target engagement + reversibility first\nnot disease modification",
        ha="center",
        fontsize=6.5,
        color=COLORS["muted"],
    )

    ax.plot([0.04, 0.96], [0.15, 0.15], color=COLORS["grid"], lw=1.0)
    ax.text(
        0.04,
        0.105,
        "Shared core: blinded SARA/f-SARA • NfL • genotype-specific MRI/MRS • digital gait • PRO • safety • concurrent controls",
        fontsize=7.4,
    )
    ax.text(
        0.04,
        0.06,
        "Failure is informative: no model upgrade; no post-hoc redefinition of S, X, or R; trial gates stay target-specific.",
        fontsize=7.0,
        color=COLORS["harm"],
        fontweight="bold",
    )
    return _save(fig, output_dir, "fig3-study-program")


def generate_all(output_dir: Path) -> list[Path]:
    _configure_style()
    outputs: list[Path] = []
    outputs.extend(_figure_framework(output_dir))
    outputs.extend(_figure_gating(output_dir))
    outputs.extend(_figure_program(output_dir))
    return outputs


if __name__ == "__main__":
    generate_all(Path(__file__).resolve().parents[1])
