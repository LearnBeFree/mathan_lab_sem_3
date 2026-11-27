"""experiments.py — вычисления на данных варианта 3 и построение графиков.

Требование условия: в solution.py — функции модели и численные методы,
здесь — их вызовы для своего варианта, вывод таблиц и сохранение рисунков.

Запуск (из папки submission, с активированным .venv):
    python experiments.py 2.2      # одна часть (номер = номер задания в отчёте)
    python experiments.py          # все реализованные части

Правила:
  * каждая часть — отдельная функция task_<номер>; добавляй только свои;
  * функции модели и методов вызывать через `import solution` (solution.<имя>);
  * рисунки сохранять в figures/ с префиксом номера задания (2-2-error.pdf);
  * незаполненная часть помечена NotImplementedError — она пропускается с пометкой.
"""

import os
import sys


def task_1_1():
    """1.1 Двойной интеграл по прямоугольнику (D): сетки 4–64, оба метода;
    figures/1-1-region.pdf, figures/1-1-error.pdf."""
    raise NotImplementedError


def task_1_2():
    """1.2 Двойной интеграл по треугольнику (D): замена, якобиан, сетки 4–64;
    figures/1-2-region.pdf, figures/1-2-error.pdf."""
    raise NotImplementedError


def task_2_1():
    """2.1 Поворот координат (D): сетки 8–64, проверка объёма V=abc;
    figures/2-1-region-old.pdf, 2-1-region-new.pdf, 2-1-error.pdf."""
    raise NotImplementedError


def task_2_2():
    """2.2 Цилиндрические координаты (D): сетки 8–64, объём V=pi*R^2*H/2;
    figures/2-2-region.pdf, figures/2-2-error.pdf."""
    raise NotImplementedError


def task_2_3():
    """2.3 Сферические координаты (D): сетки 8–64, объём V=2*pi*R^3/3;
    figures/2-3-region.pdf, figures/2-3-error.pdf."""
    raise NotImplementedError


def task_3_1():
    """3.1 Равновесие и чувствительность (A): значения q*, T, производных,
    эластичностей для таблиц сравнения; figures/3-1-levels.pdf."""
    raise NotImplementedError


def task_3_2():
    """3.2 Пределы прогноза (B): прогнозы P1–P3 при h=s/2 и по двум
    переменным для таблиц сравнения."""
    raise NotImplementedError


def task_3_3():
    """3.3 Динамика регулятора (B): q*, c*, A, k* для u0=0.6/0.75/0.9."""
    raise NotImplementedError


def task_3_4():
    """3.4 Оптимизация затрат (A): c_i*, Phi*, u0*, k*; распределение
    при ограничении c1+c2=N (численно)."""
    raise NotImplementedError


def task_3_5_1():
    """3.5.1 Численные производные (A): ошибки разностей от шага, оптимальные
    шаги; figures/3-5-1-diff-error.pdf."""
    raise NotImplementedError


def task_3_5_2():
    """3.5.2 Ошибки прогнозов Тейлора (B): от h вплоть до s;
    figures/3-5-2-taylor-error.pdf."""
    raise NotImplementedError


def task_3_5_3():
    """3.5.3 Метод Эйлера (C): траектории, граница устойчивости по Delta t;
    figures/3-5-3-trajectories.pdf."""
    raise NotImplementedError


def task_3_5_4():
    """3.5.4 Численный порог флаппинга (C): для u0=0.6/0.75/0.9, сравнение с k*."""
    raise NotImplementedError


def task_3_5_5():
    """3.5.5 Градиентный спуск (C): два правила шага, сравнение с аналитикой;
    figures/3-5-5-paths.pdf."""
    raise NotImplementedError


def task_3_6():
    """3.6 Реалистичные условия (C): lambda(t), задержка tau, средние затраты,
    оптимизация (u0,k); figures/3-6-levels.pdf, figures/3-6-dynamics.pdf."""
    raise NotImplementedError


def _tasks():
    """Реестр частей: имя task_2_2 -> номер '2.2'. Новые функции подхватываются сами."""
    return {
        name[len("task_"):].replace("_", "."): fn
        for name, fn in sorted(globals().items())
        if name.startswith("task_") and callable(fn)
    }


def main(argv):
    os.makedirs("figures", exist_ok=True)
    tasks = _tasks()
    codes = argv[1:]
    unknown = [c for c in codes if c not in tasks]
    if unknown:
        print("Неизвестные номера: " + ", ".join(unknown))
        print("Доступные: " + ", ".join(tasks))
        return 1
    for code in codes or list(tasks):
        print(f"=== {code} ===")
        try:
            tasks[code]()
        except NotImplementedError:
            print(f"[{code}] ещё не реализовано")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
