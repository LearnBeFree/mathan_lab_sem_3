# Лабораторная по матану (3 семестр) — Команда №1, вариант 3

Наша работа — вся в папке `submission/`. Файлы преподавателя (`main.*`, `report_template.*`, `task.md`) лежат на уровень выше и не изменяются. Комплект для сдачи = содержимое `submission/`.

**Сроки:** до **11.12** — свои части готовы и влиты в `main`; затем тренировочный прогон защиты друг перед другом; **14.12** — предварительная защита преподавателю. Дедлайн по условию — 20.12 20:00, ранняя защита возможна до 18.12.

## Задания и ответственные

**A** — Плешнев Арсений Вадимович (сборка отчёта, ревью и мёрж PR) · **B** — Попадюк Евгений Алексеевич · **C** — Дучин Кирилл Дмитриевич · **D** — Филиппов Андрей Алексеевич

| №           | Тема                                                                 | Ответственный | Файл отчёта                                                      |
| ----------- | -------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------- |
| 1.1         | Двойной интеграл по прямоугольнику                                   | D             | `sections/10-double.tex`                                         |
| 1.2         | Двойной интеграл по треугольнику (замена, якобиан)                   | D             | `sections/10-double.tex`                                         |
| 2.1         | Тройной интеграл: поворот декартовых координат                       | D             | `sections/21-rotation.tex`                                       |
| 2.2         | Тройной интеграл: цилиндрические координаты                          | D             | `sections/22-cylinder.tex`                                       |
| 2.3         | Тройной интеграл: сферические координаты                             | D             | `sections/23-sphere.tex`                                         |
| 3.1         | Равновесие и чувствительность                                        | A             | `sections/31-equilibrium.tex`                                    |
| 3.2         | Высшие производные и пределы прогноза                                | B             | `sections/32-taylor.tex`                                         |
| 3.3         | Динамика регулятора                                                  | B             | `sections/33-regulator.tex`                                      |
| 3.4         | Оптимизация затрат                                                   | A             | `sections/34-cost.tex`                                           |
| 3.5.1       | Численные производные и оптимальный шаг                              | A             | `sections/351-derivatives.tex`                                   |
| 3.5.2       | Ошибки прогнозов Тейлора от шага                                     | B             | `sections/352-taylor-errors.tex`                                 |
| 3.5.3–3.5.5 | Эйлер: устойчивость, флаппинг, градиентный спуск                     | C             | `sections/353-simulator.tex`                                     |
| 3.6         | Настройка в реалистичных условиях                                    | C             | `sections/36-realistic.tex`                                      |
| —           | Титульный лист, цель, порядок выполнения, заключение                 | A             | `sections/00-titlepage.tex`, `01-order.tex`, `99-conclusion.tex` |
| —           | Таблица «Проверка реализации» (строки присылает каждый за свой блок) | D             | `sections/90-checks.tex`                                         |

Пункты со звёздочкой (3.1.6\*, 3.2.5\*) — по желанию, на оценку не влияют.

## Как начать

**Linux (Debian/Ubuntu):**

```bash
sudo apt install python3-venv fonts-liberation texlive-xetex texlive-latex-extra texlive-lang-russian texlive-lang-other
sudo apt install ttf-mscorefonts-installer   # шрифты шаблона (multiverse/contrib); без них сборка идёт на Liberation Serif — метрически совместим
```

**Windows:** установить [Python 3.10+](https://www.python.org/downloads/) (галочка «Add to PATH»), [Git](https://git-scm.com/download/win), [MiKTeX](https://miktex.org/download) (недостающие пакеты ставит сам при первой сборке).

**macOS:** `brew install --cask mactex-no-gui` (или полный [MacTeX](https://tug.org/mactex)).

**Запуск (все ОС):**

```bash
git clone git@github.com:LearnBeFree/mathan_lab_sem_3.git
cd mathan_lab_sem_3/submission

# Окружение, вариант 1 — стандартный venv:
python3 -m venv .venv            # Windows: py -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
# ...или вариант 2 — uv (быстрее, активация не нужна; https://docs.astral.sh/uv/):
uv venv .venv
uv pip install -r requirements.txt

python experiments.py            # все части (пока заглушки — это нормально)
xelatex report.tex && xelatex report.tex   # Windows: xelatex report.tex; xelatex report.tex
```

PDF появится в `submission/report.pdf`. С uv запускать через `uv run python experiments.py`. Если активация venv запрещена (Windows) — использовать `.venv\Scripts\python.exe` напрямую.

## Как работать

1. `git pull`, ветка `feat/<номер>-<тема>` (например `feat/2-2-cylinder`).
2. Править только свои файлы `sections/`, свой блок `solution.py` и свои функции `task_*` в `experiments.py`.
3. Перед PR: своя часть запускается (`python experiments.py <номер>`), `report.tex` собирается, в своей части не осталось красных `[TODO: ...]`.
4. Создать PR в `main`; мёржит Aрсений.
5. Рисунки — `figures/<номер>-<имя>.pdf` (например `2-2-error.pdf`), коммитить вместе с кодом.
6. Строки в `sections/90-checks.tex` каждый присылает за свой блок; файл ведёт D.

## Памятка

- Условие и разобранные примеры — `../main.pdf`; образец оформления — `../report_template.pdf`. Номера строк в комментариях — по `main.tex` из репозитория.
- В каждом `sections/*.tex` сверху — комментарий: что сдать, параметры варианта 3, где пример в `main.tex`.
- Красный `[TODO: ...]` в PDF = незаполненное место; перед сдачей их быть не должно.
- Рисунки сохраняем в **PDF** (`fig.savefig("figures/2-2-error.pdf")`) — вектор, как в образцах преподавателя: чётко при любом зуме и мало весит. PNG допустим, но для графиков хуже.
- Версии для титульника: `python -c "import sys, numpy, matplotlib; print(sys.version, numpy.__version__, matplotlib.__version__)"`.
- `a, b, c` в приложении А (интегралы) и приложении Б (модель) — **разные величины**.
