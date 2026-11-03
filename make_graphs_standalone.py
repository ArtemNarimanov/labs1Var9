#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_graphs_standalone.py — независимый скрипт: все 33 графика вшиты внутрь.

Конфиги configs/*.gslab НЕ нужны: относительные пути к .dat (от папки, где
лежит этот файл), стартовые номера строк, цвета, легенды и подписи зашиты в GRAPHS.

Запуск:
    py -3.10 make_graphs_standalone.py                # все графики -> pic/plots/ рядом со скриптом
    py -3.10 make_graphs_standalone.py --out-dir out  # своя папка для PNG
    py -3.10 make_graphs_standalone.py graph_2 graph_15   # отдельные по имени
"""

import argparse
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # без GUI-окна, только файлы
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent

# (name, x_file, lines=[(path, legend, start, color), ...], title, xlabel, ylabel)
GRAPHS = [
    (
        'graph_2',
        'task/Пункт 2 var3 20 5/X.dat',
        [
            ('task/Пункт 2 var3 20 5/result_tav.dat', 'Корсар', 4, '#0a86f5'),
            ('task/Пункт 2 var3 20 5/T3.dat', 'Аналитика', 1, '#ff0000')
        ],
        'График средней по толщине температуры ребра',
        'X, м',
        'T, К',
    ),
    (
        'graph_3',
        'task/Пункт 2 var3 20 5/xi.dat',
        [
            ('task/Пункт 2 var3 20 5/result_theta_tav.dat', 'Корсар', 1, '#11ee4e'),
            ('task/Пункт 2 var3 20 5/Тетта 3.dat', 'Аналитика', 1, '#ff8000')
        ],
        'График безразмерных температур',
        'ξ',
        'θ',
    ),
    (
        'graph_4',
        'task/Пункт 2 var5 20 5/X.dat',
        [
            ('task/Пункт 2 var5 20 5/result_tav.dat', 'Корсар', 4, '#0a86f5'),
            ('task/Пункт 2 var5 20 5/Т 5.dat', 'Аналитика', 1, '#ff0000')
        ],
        'График средней по толщине температуры ребра',
        'X, м',
        'T, К',
    ),
    (
        'graph_5',
        'task/Пункт 2 var5 20 5/xi.dat',
        [
            ('task/Пункт 2 var5 20 5/result_theta_tav.dat', 'Корсар', 1, '#11ee4e'),
            ('task/Пункт 2 var5 20 5/Тетта 5.dat', 'Аналитика', 1, '#ff8000')
        ],
        'График безразмерных температур',
        'ξ',
        'θ',
    ),
    (
        'graph_6',
        'task/Пункт 2 var10 20 5/X.dat',
        [
            ('task/Пункт 2 var10 20 5/result_tav.dat', 'Корсар', 4, '#0a86f5'),
            ('task/Пункт 2 var10 20 5/Т10.dat', 'Аналитика', 1, '#ff0000')
        ],
        'График средней по толщине температуры ребра',
        'X, м',
        'T, К',
    ),
    (
        'graph_7',
        'task/Пункт 2 var10 20 5/xi.dat',
        [
            ('task/Пункт 2 var10 20 5/result_theta_tav.dat', 'Корсар', 1, '#11ee4e'),
            ('task/Пункт 2 var10 20 5/Тетта 10.dat', 'Аналитика', 1, '#ff8000')
        ],
        'График безразмерных температур',
        'ξ',
        'θ',
    ),
    (
        'graph_8',
        'task/Пункт 2 var25 20 5/X.dat',
        [
            ('task/Пункт 2 var25 20 5/result_tav.dat', 'Корсар', 4, '#0a86f5'),
            ('task/Пункт 2 var25 20 5/Т25.dat', 'Аналитика', 1, '#ff0000')
        ],
        'График средней по толщине температуры ребра',
        'X, м',
        'T, К',
    ),
    (
        'graph_9',
        'task/Пункт 2 var25 20 5/xi.dat',
        [
            ('task/Пункт 2 var25 20 5/result_theta_tav.dat', 'Корсар', 1, '#11ee4e'),
            ('task/Пункт 2 var25 20 5/Тетта25.dat', 'Аналитика', 1, '#ff8000')
        ],
        'График безразмерных температур',
        'ξ',
        'θ',
    ),
    (
        'graph_10',
        'task/Пункт 2 var50 20 5/X.dat',
        [
            ('task/Пункт 2 var50 20 5/result_tav.dat', 'Корсар', 4, '#0a86f5'),
            ('task/Пункт 2 var50 20 5/Т50.dat', 'Аналитика', 1, '#ff0000')
        ],
        'График средней по толщине температуры ребра',
        'X, м',
        'T, К',
    ),
    (
        'graph_11',
        'task/Пункт 2 var50 20 5/xi.dat',
        [
            ('task/Пункт 2 var25 20 5/result_theta_tav.dat', 'Корсар', 1, '#11ee4e'),
            ('task/Пункт 2 var25 20 5/Тетта25.dat', 'Аналитика', 1, '#ff8000')
        ],
        'График безразмерных температур',
        'ξ',
        'θ',
    ),
    (
        'graph_12',
        'task/Пункт 3 графики/a.dat',
        [
            ('task/Пункт 3 графики/TL Корсар.dat', 'Корсар', 1, '#0a86f5'),
            ('task/Пункт 3 графики/TL Аналитика.dat', 'Аналитика', 1, '#ff0000')
        ],
        'График зависимости температуры на конце ребра от коэф-та теплоотдачи',
        'α, Вт/(м^2*К)',
        'T, К',
    ),
    (
        'graph_13',
        'task/Пункт 3 графики/a.dat',
        [
            ('task/Пункт 3 графики/Q Корсар.dat', 'Корсар', 1, '#0a86f5'),
            ('task/Пункт 3 графики/Q Аналитика.dat', 'Аналитика', 1, '#ff0000')
        ],
        'График зависимости теплого потока от коэф-та теплоотдачи',
        'α, Вт/(м^2*К)',
        'Q, Вт',
    ),
    (
        'graph_14',
        'task/Пункт 3 графики/a.dat',
        [
            ('task/Пункт 3 графики/Этта Корсар.dat', 'Корсар', 1, '#0a86f5'),
            ('task/Пункт 3 графики/Этта Аналитика.dat', 'Аналитика', 1, '#ff0000')
        ],
        'График зависимости эффективности ребра от коэф-та теплоотдачи',
        'α, Вт/(м^2*К)',
        'η',
    ),
    (
        'graph_15',
        'task/Пункт 4.1 var3 5 5/X5.dat',
        [
            ('task/Пункт 4.1 var3 5 5/result_tav.dat', 'Средняя температура по толщине', 3, '#ff8040'),
            ('task/Пункт 4.1 var3 5 5/result_tw1.dat', 'Температура на стенке', 3, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_16',
        'task/Пункт 4.1 var3 10 5/X10.dat',
        [
            ('task/Пункт 4.1 var3 10 5/result_tav.dat', 'Средняя температура по толщине', 3, '#ff8040'),
            ('task/Пункт 4.1 var3 10 5/result_tw1.dat', 'Температура на стенке', 3, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_17',
        'task/Пункт 4.1 var3 20 5/X.dat',
        [
            ('task/Пункт 4.1 var3 20 5/result_tav.dat', 'Средняя температура по толщине', 4, '#ff8040'),
            ('task/Пункт 4.1 var3 20 5/result_tw1.dat', 'Температура на стенке', 4, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_18',
        'task/Пункт 4.1 var3 30 5/X30.dat',
        [
            ('task/Пункт 4.1 var3 30 5/result_tav.dat', 'Средняя температура по толщине', 4, '#ff8040'),
            ('task/Пункт 4.1 var3 30 5/result_tw1.dat', 'Температура на стенке', 4, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_19',
        'task/Пункт 4.1 var50 40 5/X40.dat',
        [
            ('task/Пункт 4.1 var50 40 5/result_tav.dat', 'Средняя температура по толщине', 5, '#ff8040'),
            ('task/Пункт 4.1 var50 40 5/result_tw1.dat', 'Температура на стенке', 5, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_20',
        'task/Пункт 4.1 var50 50 5/X50.dat',
        [
            ('task/Пункт 4.1 var50 50 5/result_tav.dat', 'Средняя температура по толщине', 6, '#ff8040'),
            ('task/Пункт 4.1 var50 50 5/result_tw1.dat', 'Температура на стенке', 6, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_21',
        'task/Пункт 4.1 var50 5 5/X5.dat',
        [
            ('task/Пункт 4.1 var50 5 5/result_tav.dat', 'Средняя температура по толщине', 3, '#ff8040'),
            ('task/Пункт 4.1 var50 5 5/result_tw1.dat', 'Температура на стенке', 3, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_22',
        'task/Пункт 4.1 var50 10 5/X10.dat',
        [
            ('task/Пункт 4.1 var50 10 5/result_tav.dat', 'Средняя температура по толщине', 3, '#ff8040'),
            ('task/Пункт 4.1 var50 10 5/result_tw1.dat', 'Температура на стенке', 3, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_23',
        'task/Пункт 4.1 var50 20 5/X.dat',
        [
            ('task/Пункт 4.1 var50 20 5/result_tav.dat', 'Средняя температура по толщине', 4, '#ff8040'),
            ('task/Пункт 4.1 var50 20 5/result_tw1.dat', 'Температура на стенке', 4, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_24',
        'task/Пункт 4.1 var50 30 5/X30.dat',
        [
            ('task/Пункт 4.1 var50 30 5/result_tav.dat', 'Средняя температура по толщине', 4, '#ff8040'),
            ('task/Пункт 4.1 var50 30 5/result_tw1.dat', 'Температура на стенке', 4, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_25',
        'task/Пункт 4.1 var50 40 5/X40.dat',
        [
            ('task/Пункт 4.1 var50 40 5/result_tav.dat', 'Средняя температура по толщине', 5, '#ff8040'),
            ('task/Пункт 4.1 var50 40 5/result_tw1.dat', 'Температура на стенке', 5, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_26',
        'task/Пункт 4.1 var50 50 5/X50.dat',
        [
            ('task/Пункт 4.1 var50 50 5/result_tav.dat', 'Средняя температура по толщине', 6, '#ff8040'),
            ('task/Пункт 4.1 var50 50 5/result_tw1.dat', 'Температура на стенке', 6, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_27',
        'task/Пункт 4.2 var3 20 3/X.dat',
        [
            ('task/Пункт 4.2 var3 20 3/result_tav.dat', 'Средняя температура по толщине', 4, '#ff8040'),
            ('task/Пункт 4.2 var3 20 3/result_tw1.dat', 'Температура на стенке', 4, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_28',
        'task/Пункт 4.2 var3 20 5/X.dat',
        [
            ('task/Пункт 4.2 var3 20 5/result_tav.dat', 'Средняя температура по толщине', 4, '#ff8040'),
            ('task/Пункт 4.2 var3 20 5/result_tw1.dat', 'Температура на стенке', 4, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_29',
        'task/Пункт 4.2 var3 20 7/X.dat',
        [
            ('task/Пункт 4.2 var3 20 7/result_tav.dat', 'Средняя температура по толщине', 4, '#ff8040'),
            ('task/Пункт 4.2 var3 20 7/result_tw1.dat', 'Температура на стенке', 4, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_30',
        'task/Пункт 4.2 var50 20 3/X.dat',
        [
            ('task/Пункт 4.2 var50 20 3/result_tav.dat', 'Средняя температура по толщине', 4, '#ff8040'),
            ('task/Пункт 4.2 var50 20 3/result_tw1.dat', 'Температура на стенке', 4, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_31',
        'task/Пункт 4.2 var50 20 5/X.dat',
        [
            ('task/Пункт 4.2 var50 20 5/result_tav.dat', 'Средняя температура по толщине', 4, '#ff8040'),
            ('task/Пункт 4.2 var50 20 5/result_tw1.dat', 'Температура на стенке', 4, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_32',
        'task/Пункт 4.2 var50 20 7/X.dat',
        [
            ('task/Пункт 4.2 var50 20 7/result_tav.dat', 'Средняя температура по толщине', 4, '#ff8040'),
            ('task/Пункт 4.2 var50 20 7/result_tw1.dat', 'Температура на стенке', 4, '#3621f8')
        ],
        'График средней температуры по толщине и температуры на стенке',
        'X, м',
        'T, К',
    ),
    (
        'graph_33',
        'task/Пункт 4.2 var3 20 7/X.dat',
        [
            ('task/Пункт 4.2 var3 20 3/result_tav.dat', 'При K =3', 4, '#ff8040'),
            ('task/Пункт 4.2 var3 20 5/result_tav.dat', 'При K = 5', 4, '#3621f8'),
            ('task/Пункт 4.2 var3 20 7/result_tav.dat', 'При K = 7', 4, '#2e8b57')
        ],
        'График средних температур по толщине ребра',
        'X, м',
        'T, К',
    ),
    (
        'graph_34',
        'task/Пункт 4.2 var50 20 7/X.dat',
        [
            ('task/Пункт 4.2 var50 20 3/result_tav.dat', 'При K =3', 4, '#ff8040'),
            ('task/Пункт 4.2 var50 20 5/result_tav.dat', 'При K = 5', 4, '#3621f8'),
            ('task/Пункт 4.2 var50 20 7/result_tav.dat', 'При K = 7', 4, '#2e8b57')
        ],
        'График средних температур по толщине ребра',
        'X, м',
        'T, К',
    ),
]


def read_dat(path: Path, start: int = 1) -> list[float]:
    """Читает все числовые токены файла начиная со строки `start` (1-based).

    Разделители — пробелы и точка с запятой; токены из всех строк склеиваются
    в один плоский список float. Покрывает и однострочные файлы (X.dat, xi.dat),
    и многострочные result_*.dat, где первые строки — заголовок/нулевая шапка.
    """
    if not path.is_file():
        raise FileNotFoundError(f"файл не найден: {path}")
    values: list[float] = []
    with open(path, "r", encoding="utf-8-sig") as f:
        for lineno, line in enumerate(f, start=1):
            if lineno < start:
                continue
            for tok in line.replace(";", " ").split():
                try:
                    values.append(float(tok))
                except ValueError:
                    raise ValueError(
                        f"не число '{tok}' в {path} (строка {lineno})"
                    ) from None
    if not values:
        raise ValueError(f"пустые данные: {path} (start={start})")
    return values


def markers_for(legends: list[str]) -> list[str]:
    """Маркеры как в Graphs.ipynb: «Средняя температура по толщине / стенка» — ^, D;
    остальные серии идут по циклу o, s, ^, D (в т.ч. 3-серийные K=3/5/7)."""
    if legends and legends[0].startswith("Средняя температура"):
        return ["^", "D"]
    return ["o", "s", "^", "D"]


def render(graph: tuple, out_dir: Path) -> Path:
    """Строит один график по вшитому описанию и сохраняет PNG."""
    name, x_file, lines, title, xlabel, ylabel = graph
    x = read_dat(BASE / x_file)
    markers = markers_for([ln[1] for ln in lines])

    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    for i, (p, legend, start, color) in enumerate(lines):
        y = read_dat(BASE / p, start=start)
        ax.plot(
            x, y,
            color=color,
            linewidth=2,
            marker=markers[i % len(markers)],
            markersize=4,
            label=legend,
        )

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(framealpha=0.9)
    fig.tight_layout(pad=0.4)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / (name + ".png")
    fig.savefig(out_path)
    plt.close(fig)
    return out_path


def main() -> int:
    ap = argparse.ArgumentParser(description="Независимый скрипт графиков (пути вшиты)")
    ap.add_argument("names", nargs="*", help="имена графиков, напр. graph_2 (по умолчанию все)")
    ap.add_argument("--out-dir", default=None, help="папка для PNG (по умолчанию pic/plots/ рядом со скриптом)")
    args = ap.parse_args()

    out_dir = Path(args.out_dir) if args.out_dir else BASE / "pic" / "plots"

    graphs = GRAPHS
    if args.names:
        wanted = set(args.names)
        graphs = [g for g in GRAPHS if g[0] in wanted]
        missing = wanted - {g[0] for g in graphs}
        if missing:
            print("не найдены: " + ", ".join(sorted(missing)))

    ok, failed = 0, []
    for g in graphs:
        try:
            out = render(g, out_dir)
            print(f"[OK] {g[0]} -> {out}")
            ok += 1
        except Exception as e:
            print(f"[FAIL] {g[0]}: {e}")
            failed.append(g[0])

    print(f"\nВсего: {len(graphs)}, успешно: {ok}, ошибок: {len(failed)}")
    if failed:
        print("Провалено: " + ", ".join(failed))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
