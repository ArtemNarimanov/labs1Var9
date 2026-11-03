# Лабораторная работа № 9. Стационарная теплопроводность в плоском ребре

![tools](https://img.shields.io/badge/tools-Q__eta__calculator%20%C2%B7%20theta-Xi-converter%20%C2%B7%20graphslab9-blue?logo=github)

## 1. Цель работы

Собрать в КОРСАР расчетную схему для моделирования прямоугольного плоского ребра с температурой основания <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-e14cb192aabe-dark.svg"><img src="./pic/formulas/inline-e14cb192aabe-light.svg" alt="T_0" height="15"></picture>, охлаждаемого воздухом при температуре <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-9bbeb7d12eb0-dark.svg"><img src="./pic/formulas/inline-9bbeb7d12eb0-light.svg" alt="T_1" height="15"></picture>. Найти температуру конца ребра, распределение температуры по высоте и мощность теплоотдачи. Сравнить численное решение с аналитическим.

### Навыки, приобретаемые по результатам выполнения работы

- Моделирование ребра элементом с двумерной теплопроводностью (HCS, TYPE=2);
- Проверка теплового баланса;
- Исследование сеточной сходимости.

---

## 2. Описание постановки задачи

### 2.1. Геометрия, допущения и нодализация

Рассматривается ребро постоянной толщины <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-d203ba01eef4-dark.svg"><img src="./pic/formulas/inline-d203ba01eef4-light.svg" alt="\delta" height="14"></picture>, ширины <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-3e23e8160039-dark.svg"><img src="./pic/formulas/inline-3e23e8160039-light.svg" alt="b" height="14"></picture> и высоты охлаждаемой части <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-72dfcfb0c470-dark.svg"><img src="./pic/formulas/inline-72dfcfb0c470-light.svg" alt="L" height="12"></picture>. Координата <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-2d711642b726-dark.svg"><img src="./pic/formulas/inline-2d711642b726-light.svg" alt="x" height="9"></picture> направлена **от несущей оребренной поверхности к концу ребра, от ячейки 1 к ячейке N**; координата <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-a1fce4363854-dark.svg"><img src="./pic/formulas/inline-a1fce4363854-light.svg" alt="y" height="14"></picture> — поперек толщины, от поверхности `/1` к `/2`. Ширина ребра перпендикулярна плоскости рисунка.

Обе широкие поверхности охлаждаемой части обмениваются теплом с воздухом при одинаковых постоянных <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture> и <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-9bbeb7d12eb0-dark.svg"><img src="./pic/formulas/inline-9bbeb7d12eb0-light.svg" alt="T_1" height="15"></picture>. Узкие боковые кромки и торец теплоизолированы. Излучение, внутреннее энерговыделение и зависимость свойств от температуры отсутствуют. Поэтому площадь сечения <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-75115b4c6738-dark.svg"><img src="./pic/formulas/inline-75115b4c6738-light.svg" alt="A_c = b\delta = 2{\cdot}10^{-4}" height="16"></picture> м², охлаждаемый периметр <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-58e6b3afc070-dark.svg"><img src="./pic/formulas/inline-58e6b3afc070-light.svg" alt="P = 2b = 0{,}2" height="15"></picture> м, площадь теплоотдачи <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-190b8b226c33-dark.svg"><img src="./pic/formulas/inline-190b8b226c33-light.svg" alt="A_f = PL = 0{,}012" height="15"></picture> м². Охлаждением узких кромок в этой постановке пренебрегается.

<a id="fig-nodal"></a>

![Нодализация плоского ребра: контактная ячейка 1, охлаждаемые ячейки 2:N](./pic/nodal.svg)

*Рисунок 1 — Продольная теплопроводность HCS и граничные условия BHEAT.*

Для моделирования ребра необходима **двумерная** модель теплопроводности: ребро задается элементом HCS с ключом `TYPE=2`, продольная (по <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-2d711642b726-dark.svg"><img src="./pic/formulas/inline-2d711642b726-light.svg" alt="x" height="9"></picture>) теплопроводность включена, поперечные градиенты учитываются автоматически.

### 2.2. Исходные данные и выбор параметров


| Параметр                                          | Значение       |
|-----------------------------------------------------------|-----------------------:|
| Высота охлаждаемой части <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-72dfcfb0c470-dark.svg"><img src="./pic/formulas/inline-72dfcfb0c470-light.svg" alt="L" height="12"></picture>        | 0.060 м               |
| Толщина <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-d203ba01eef4-dark.svg"><img src="./pic/formulas/inline-d203ba01eef4-light.svg" alt="\delta" height="14"></picture>                                  | 0.002 м               |
| Ширина <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-3e23e8160039-dark.svg"><img src="./pic/formulas/inline-3e23e8160039-light.svg" alt="b" height="14"></picture>                                          | 0.100 м               |
| Длина контактной ячейки <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-e5916cb731c6-dark.svg"><img src="./pic/formulas/inline-e5916cb731c6-light.svg" alt="\ell_c" height="15"></picture>    | 0.001 м               |
| Теплопроводность <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-583cf6290785-dark.svg"><img src="./pic/formulas/inline-583cf6290785-light.svg" alt="\lambda" height="12"></picture>               | 50 Вт/(м·К)       |
| Плотность <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-dabec2cdc19c-dark.svg"><img src="./pic/formulas/inline-dabec2cdc19c-light.svg" alt="\rho" height="14"></picture>                                | 7800 кг/м³         |
| Теплоемкость <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-2e7d2c03a950-dark.svg"><img src="./pic/formulas/inline-2e7d2c03a950-light.svg" alt="c" height="10"></picture>                              | 500 Дж/(кг·К)    |
| Температура основания <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-e14cb192aabe-dark.svg"><img src="./pic/formulas/inline-e14cb192aabe-light.svg" alt="T_0" height="15"></picture>           | 120 °C = 393.15 К    |
| Температура воздуха <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-9bbeb7d12eb0-dark.svg"><img src="./pic/formulas/inline-9bbeb7d12eb0-light.svg" alt="T_1" height="15"></picture>               | 20 °C = 293.15 К     |
| Коэффициенты теплоотдачи <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture> | 3…50 Вт/(м²·К) |


### 2.3. Математическая модель и аналитическое решение

При малом <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-b85ee422228e-dark.svg"><img src="./pic/formulas/inline-b85ee422228e-light.svg" alt="\mathrm{Bi}_\delta = \alpha\delta/(2\lambda)" height="15"></picture> температура сечения почти однородна; в рассматриваемых вариантах <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-80205b80aed7-dark.svg"><img src="./pic/formulas/inline-80205b80aed7-light.svg" alt="\mathrm{Bi}_\delta \le 0{,}001" height="15"></picture>, поэтому двумерное поле HCS сравнивается с одномерным решением.

Уравнение и граничные условия для охлаждаемой части:

<a id="eq-fin"></a>


<picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/equation-aafa0b0a3aec-dark.svg"><img src="./pic/formulas/equation-aafa0b0a3aec-light.svg" alt="\lambda A_c\dfrac{d^2T}{dx^2} - \alpha P(T-T_1) = 0, \qquad T(0) = T_0, \qquad \left.\dfrac{dT}{dx}\right&#124;_{L} = 0. \tag{1}" height="36"></picture>


Введем <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-5c3af7d34eae-dark.svg"><img src="./pic/formulas/inline-5c3af7d34eae-light.svg" alt="\theta = (T-T_1)/(T_0-T_1)" height="15"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-0c655446d538-dark.svg"><img src="./pic/formulas/inline-0c655446d538-light.svg" alt="\xi = x/L" height="16"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-5655b3f1c627-dark.svg"><img src="./pic/formulas/inline-5655b3f1c627-light.svg" alt="m = \sqrt{\alpha P/(\lambda A_c)} = \sqrt{2\alpha/(\lambda\delta)}" height="22"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-19f219da7a17-dark.svg"><img src="./pic/formulas/inline-19f219da7a17-light.svg" alt="M = mL" height="12"></picture>. Решение для теплоизолированного торца и мощность теплоотдачи (Holman [[2]](#ref-holman); открытый вывод — MIT [[3]](#ref-mit)):

<a id="eq-profile"></a>


<picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/equation-c06814c34b63-dark.svg"><img src="./pic/formulas/equation-c06814c34b63-light.svg" alt="\theta(\xi) = \dfrac{\cosh[M(1-\xi)]}{\cosh M}, \qquad T(L) = T_1 + \dfrac{T_0-T_1}{\cosh M}. \tag{2}" height="36"></picture>


<a id="eq-power"></a>


<picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/equation-641abcf1c840-dark.svg"><img src="./pic/formulas/equation-641abcf1c840-light.svg" alt="\dot{Q} = -\lambda A_cT&#x27;(0) = \lambda A_cm(T_0-T_1)\tanh M = \alpha\int_0^L P[T(x)-T_1]dx. \tag{3}" height="33"></picture>


<a id="eq-efficiency"></a>


<picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/equation-1af6d3fdad48-dark.svg"><img src="./pic/formulas/equation-1af6d3fdad48-light.svg" alt="\eta_f = \dfrac{\dot{Q}}{\alpha A_f(T_0-T_1)} = \dfrac{\tanh M}{M}. \tag{4}" height="43"></picture>


Эффективность <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> — отношение мощности ребра к мощности изотермического ребра той же площади при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-e14cb192aabe-dark.svg"><img src="./pic/formulas/inline-e14cb192aabe-light.svg" alt="T_0" height="15"></picture>, т. е. отношение средней относительной температуры ребра к температуре его основания. Аналитическое решение приводится также в учебнике Михеева [[4]](#ref-miheev), разд. 10-6.

---

## 3. Требуемые результаты

- Нодализация задачи, постановка, исходные данные;
- Профили температуры по высоте, мощности подвода и теплоотдачи, проверка баланса;
- Зависимость эффективности от <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture>;
- Скрипты обработки, расчета аналитики и отклонений; сводные таблицы сходимости;
- Вывод о достаточном разбиении, точности представления контакта и границах одномерного приближения.

---

## 4. Ход выполнения работы

Для выполнения задачи были созданы файлы задачи `kordat` и обработки данных `kutdat` для всех расчетных вариантов. Нодализация задачи представлена на рисунке [1](#fig-nodal).

Схема собрана следующим образом:

- ребро задано элементом **HCS** с `TYPE=2` (двумерная теплопроводность): <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-8ce86a6ae65d-dark.svg"><img src="./pic/formulas/inline-8ce86a6ae65d-light.svg" alt="N" height="12"></picture> ячеек по высоте (<picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-2d711642b726-dark.svg"><img src="./pic/formulas/inline-2d711642b726-light.svg" alt="x" height="9"></picture>, ключи `N`, `XL`), <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-86be9a55762d-dark.svg"><img src="./pic/formulas/inline-86be9a55762d-light.svg" alt="K" height="12"></picture> ячеек по толщине (<picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-a1fce4363854-dark.svg"><img src="./pic/formulas/inline-a1fce4363854-light.svg" alt="y" height="14"></picture>); продольная теплопроводность включена, направление от несущей оребренной поверхности к концу ребра совпадает с осью <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-2d711642b726-dark.svg"><img src="./pic/formulas/inline-2d711642b726-light.svg" alt="x" height="9"></picture>;
- **ячейка 1** — контактная, длина <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-bfa27e335e3e-dark.svg"><img src="./pic/formulas/inline-bfa27e335e3e-light.svg" alt="\ell_c = 0{,}001" height="15"></picture> м: задана температура границ ячейки <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-a32255d13ee3-dark.svg"><img src="./pic/formulas/inline-a32255d13ee3-light.svg" alt="T_0 = 393{,}15" height="15"></picture> К;
- **ячейки 2…N** — охлаждаемые: на поверхностях `/1` и `/2` задано граничное условие BHEAT с коэффициентами теплоотдачи <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-59c28bf970ce-dark.svg"><img src="./pic/formulas/inline-59c28bf970ce-light.svg" alt="\alpha = 3\ldots50" height="14"></picture> Вт/(м²·К) и температурой воздуха <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-0d2363524ac8-dark.svg"><img src="./pic/formulas/inline-0d2363524ac8-light.svg" alt="T_1 = 293{,}15" height="15"></picture> К; торец и узкие кромки — адиабатические.

В качестве начальных условий принималось равномерное поле <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-526833ee7145-dark.svg"><img src="./pic/formulas/inline-526833ee7145-light.svg" alt="T = T_0" height="15"></picture> во всех ячейках. Для вывода расчетной схемы в стационарный режим расчет выполнялся до времени <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-e87b53fb439a-dark.svg"><img src="./pic/formulas/inline-e87b53fb439a-light.svg" alt="t = 5000" height="14"></picture> с, что превышает ориентир установления стационарности <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7f57202da228-dark.svg"><img src="./pic/formulas/inline-7f57202da228-light.svg" alt="10L^2/a \approx 2808" height="16"></picture> с, где температуропроводность <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-712725ba29a5-dark.svg"><img src="./pic/formulas/inline-712725ba29a5-light.svg" alt="a = \lambda/(\rho c) = 1{,}28\cdot10^{-5}" height="18"></picture> м²/с. Вывод расчетных значений (температур ячеек и тепловых потоков) осуществляется с периодичностью 5000 с, так как интерес представляют только вышедшие на статику значения параметров.

Выполнен контрольный расчет при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-0ddf590cd206-dark.svg"><img src="./pic/formulas/inline-0ddf590cd206-light.svg" alt="T_0 = T_1" height="15"></picture>: поле температуры равномерно и совпадает с <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-9bbeb7d12eb0-dark.svg"><img src="./pic/formulas/inline-9bbeb7d12eb0-light.svg" alt="T_1" height="15"></picture>, мощность теплоотдачи равна нулю — схема собрана корректно. Проверены площади обеих сторон, выполнен расчет с выключенной продольной теплопроводностью.

Выполнены вариантные расчеты по <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture>. За варианты коэффициента теплоотдачи были взяты значения: 3, 5, 10, 25, 50 Вт/(м²·К).

Построены <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1165c59bb905-dark.svg"><img src="./pic/formulas/inline-1165c59bb905-light.svg" alt="T(x)" height="15"></picture> и <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7695d2a56e69-dark.svg"><img src="./pic/formulas/inline-7695d2a56e69-light.svg" alt="\theta(\xi)" height="16"></picture> для всех <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture>, графики <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture> и <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> от <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture>; наложена аналитика.

![Профиль T(x) при alpha = 3](./pic/README_plots/graph_2.png)

*Рисунок 2 — Температурный профиль <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1165c59bb905-dark.svg"><img src="./pic/formulas/inline-1165c59bb905-light.svg" alt="T(x)" height="15"></picture> при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture> Вт/(м²·К).*

![Профиль theta(xi) при alpha = 3](./pic/README_plots/graph_3.png)

*Рисунок 3 — Относительный температурный профиль <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7695d2a56e69-dark.svg"><img src="./pic/formulas/inline-7695d2a56e69-light.svg" alt="\theta(\xi)" height="16"></picture> при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture> Вт/(м²·К).*

![Профиль T(x) при alpha = 5](./pic/README_plots/graph_4.png)

*Рисунок 4 — Температурный профиль <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1165c59bb905-dark.svg"><img src="./pic/formulas/inline-1165c59bb905-light.svg" alt="T(x)" height="15"></picture> при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-11fdec7448c8-dark.svg"><img src="./pic/formulas/inline-11fdec7448c8-light.svg" alt="\alpha = 5" height="14"></picture> Вт/(м²·К).*

![Профиль theta(xi) при alpha = 5](./pic/README_plots/graph_5.png)

*Рисунок 5 — Относительный температурный профиль <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7695d2a56e69-dark.svg"><img src="./pic/formulas/inline-7695d2a56e69-light.svg" alt="\theta(\xi)" height="16"></picture> при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-11fdec7448c8-dark.svg"><img src="./pic/formulas/inline-11fdec7448c8-light.svg" alt="\alpha = 5" height="14"></picture> Вт/(м²·К).*

![Профиль T(x) при alpha = 10](./pic/README_plots/graph_6.png)

*Рисунок 6 — Температурный профиль <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1165c59bb905-dark.svg"><img src="./pic/formulas/inline-1165c59bb905-light.svg" alt="T(x)" height="15"></picture> при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-e0bcac71b4a3-dark.svg"><img src="./pic/formulas/inline-e0bcac71b4a3-light.svg" alt="\alpha = 10" height="14"></picture> Вт/(м²·К).*

![Профиль theta(xi) при alpha = 10](./pic/README_plots/graph_7.png)

*Рисунок 7 — Относительный температурный профиль <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7695d2a56e69-dark.svg"><img src="./pic/formulas/inline-7695d2a56e69-light.svg" alt="\theta(\xi)" height="16"></picture> при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-e0bcac71b4a3-dark.svg"><img src="./pic/formulas/inline-e0bcac71b4a3-light.svg" alt="\alpha = 10" height="14"></picture> Вт/(м²·К).*

![Профиль T(x) при alpha = 25](./pic/README_plots/graph_8.png)

*Рисунок 8 — Температурный профиль <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1165c59bb905-dark.svg"><img src="./pic/formulas/inline-1165c59bb905-light.svg" alt="T(x)" height="15"></picture> при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-08ffccf37974-dark.svg"><img src="./pic/formulas/inline-08ffccf37974-light.svg" alt="\alpha = 25" height="14"></picture> Вт/(м²·К).*

![Профиль theta(xi) при alpha = 25](./pic/README_plots/graph_9.png)

*Рисунок 9 — Относительный температурный профиль <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7695d2a56e69-dark.svg"><img src="./pic/formulas/inline-7695d2a56e69-light.svg" alt="\theta(\xi)" height="16"></picture> при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-08ffccf37974-dark.svg"><img src="./pic/formulas/inline-08ffccf37974-light.svg" alt="\alpha = 25" height="14"></picture> Вт/(м²·К).*

![Профиль T(x) при alpha = 50](./pic/README_plots/graph_10.png)

*Рисунок 10 — Температурный профиль <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1165c59bb905-dark.svg"><img src="./pic/formulas/inline-1165c59bb905-light.svg" alt="T(x)" height="15"></picture> при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture> Вт/(м²·К).*

![Профиль theta(xi) при alpha = 50](./pic/README_plots/graph_11.png)

*Рисунок 11 — Относительный температурный профиль <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7695d2a56e69-dark.svg"><img src="./pic/formulas/inline-7695d2a56e69-light.svg" alt="\theta(\xi)" height="16"></picture> при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture> Вт/(м²·К).*

![Зависимость T(L) от alpha](./pic/README_plots/graph_12.png)

*Рисунок 12 — Температура конца ребра <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture> в зависимости от α (численно и аналитически).*

![Зависимость Q от alpha](./pic/README_plots/graph_13.png)

*Рисунок 13 — Мощность теплоотдачи <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture> в зависимости от α (численно и аналитически).*

![Зависимость eta_f от alpha](./pic/README_plots/graph_14.png)

*Рисунок 14 — Эффективность ребра <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> в зависимости от α (численно и аналитически).*

Для <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture> и 50 выполнены расчеты на сетках <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-da5502ebce3e-dark.svg"><img src="./pic/formulas/inline-da5502ebce3e-light.svg" alt="N-1 = 5\ldots50" height="14"></picture> ячеек при постоянных <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-72dfcfb0c470-dark.svg"><img src="./pic/formulas/inline-72dfcfb0c470-light.svg" alt="L" height="12"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-e5916cb731c6-dark.svg"><img src="./pic/formulas/inline-e5916cb731c6-light.svg" alt="\ell_c" height="15"></picture> и <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-86be9a55762d-dark.svg"><img src="./pic/formulas/inline-86be9a55762d-light.svg" alt="K" height="12"></picture>. Были взяты количества ячеек: 5, 10, 20, 30, 40, 50. Затем было проверено <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-fc026a95db6e-dark.svg"><img src="./pic/formulas/inline-fc026a95db6e-light.svg" alt="K = 3, 5, 7" height="15"></picture> при фиксированной продольной сетке. Было произведено сравнение разности температур середины толщины и поверхностей.

**Сходимость по числу ячеек по высоте, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>:**

![alpha=3, N-1=5](./pic/README_plots/graph_15.png)

*Рисунок 15 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-914688053611-dark.svg"><img src="./pic/formulas/inline-914688053611-light.svg" alt="N-1 = 5" height="14"></picture>.*

![alpha=3, N-1=10](./pic/README_plots/graph_16.png)

*Рисунок 16 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-352d0db1e232-dark.svg"><img src="./pic/formulas/inline-352d0db1e232-light.svg" alt="N-1 = 10" height="14"></picture>.*

![alpha=3, N-1=20](./pic/README_plots/graph_17.png)

*Рисунок 17 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-41cf6b25fd26-dark.svg"><img src="./pic/formulas/inline-41cf6b25fd26-light.svg" alt="N-1 = 20" height="14"></picture>.*

![alpha=3, N-1=30](./pic/README_plots/graph_18.png)

*Рисунок 18 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-a53e5a3590a5-dark.svg"><img src="./pic/formulas/inline-a53e5a3590a5-light.svg" alt="N-1 = 30" height="14"></picture>.*

![alpha=3, N-1=40](./pic/README_plots/graph_19.png)

*Рисунок 19 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-8dc0a0ebb28d-dark.svg"><img src="./pic/formulas/inline-8dc0a0ebb28d-light.svg" alt="N-1 = 40" height="14"></picture>.*

![alpha=3, N-1=50](./pic/README_plots/graph_20.png)

*Рисунок 20 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-48eeef94b005-dark.svg"><img src="./pic/formulas/inline-48eeef94b005-light.svg" alt="N-1 = 50" height="14"></picture>.*

**Сходимость по числу ячеек по высоте, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>:**

![alpha=50, N-1=5](./pic/README_plots/graph_21.png)

*Рисунок 21 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-914688053611-dark.svg"><img src="./pic/formulas/inline-914688053611-light.svg" alt="N-1 = 5" height="14"></picture>.*

![alpha=50, N-1=10](./pic/README_plots/graph_22.png)

*Рисунок 22 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-352d0db1e232-dark.svg"><img src="./pic/formulas/inline-352d0db1e232-light.svg" alt="N-1 = 10" height="14"></picture>.*

![alpha=50, N-1=20](./pic/README_plots/graph_23.png)

*Рисунок 23 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-41cf6b25fd26-dark.svg"><img src="./pic/formulas/inline-41cf6b25fd26-light.svg" alt="N-1 = 20" height="14"></picture>.*

![alpha=50, N-1=30](./pic/README_plots/graph_24.png)

*Рисунок 24 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-a53e5a3590a5-dark.svg"><img src="./pic/formulas/inline-a53e5a3590a5-light.svg" alt="N-1 = 30" height="14"></picture>.*

![alpha=50, N-1=40](./pic/README_plots/graph_25.png)

*Рисунок 25 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-8dc0a0ebb28d-dark.svg"><img src="./pic/formulas/inline-8dc0a0ebb28d-light.svg" alt="N-1 = 40" height="14"></picture>.*

![alpha=50, N-1=50](./pic/README_plots/graph_26.png)

*Рисунок 26 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-48eeef94b005-dark.svg"><img src="./pic/formulas/inline-48eeef94b005-light.svg" alt="N-1 = 50" height="14"></picture>.*

**Влияние числа ячеек по толщине K (при фиксированной продольной сетке):**

![alpha=3, K=3](./pic/README_plots/graph_27.png)

*Рисунок 27 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1de9a5b9680a-dark.svg"><img src="./pic/formulas/inline-1de9a5b9680a-light.svg" alt="K = 3" height="14"></picture>.*

![alpha=3, K=5](./pic/README_plots/graph_28.png)

*Рисунок 28 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c60f03e77856-dark.svg"><img src="./pic/formulas/inline-c60f03e77856-light.svg" alt="K = 5" height="14"></picture>.*

![alpha=3, K=7](./pic/README_plots/graph_29.png)

*Рисунок 29 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-9e9d70da3bc8-dark.svg"><img src="./pic/formulas/inline-9e9d70da3bc8-light.svg" alt="K = 7" height="12"></picture>.*

![alpha=50, K=3](./pic/README_plots/graph_30.png)

*Рисунок 30 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1de9a5b9680a-dark.svg"><img src="./pic/formulas/inline-1de9a5b9680a-light.svg" alt="K = 3" height="14"></picture>.*

![alpha=50, K=5](./pic/README_plots/graph_31.png)

*Рисунок 31 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c60f03e77856-dark.svg"><img src="./pic/formulas/inline-c60f03e77856-light.svg" alt="K = 5" height="14"></picture>.*

![alpha=50, K=7](./pic/README_plots/graph_32.png)

*Рисунок 32 — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-9e9d70da3bc8-dark.svg"><img src="./pic/formulas/inline-9e9d70da3bc8-light.svg" alt="K = 7" height="12"></picture>.*

![Сравнение по K, alpha=3](./pic/README_plots/graph_33.png)

*Рисунок 33 — Сравнение результатов по K при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-76fe4fec6c0a-dark.svg"><img src="./pic/formulas/inline-76fe4fec6c0a-light.svg" alt="\alpha = 3" height="14"></picture>.*

![Сравнение по K, alpha=50](./pic/README_plots/graph_34.png)

*Рисунок 34 — Сравнение результатов по K при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture>.*

Был произведен самый подробный расчет для <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1c74e5eaafa3-dark.svg"><img src="./pic/formulas/inline-1c74e5eaafa3-light.svg" alt="\alpha = 50" height="14"></picture> при количестве ячеек по длине 50 и по толщине 7.

---

## 5. Получение результатов работы

Для получения результатов необходимо:

- выполнить запуск кода КОРСАР при помощи команды

```cmd
START.bat
```

- после окончания расчета выполнить процессинг бинарного файла результатов расчета `korres` при помощи команды

```cmd
PROC.bat
```

- выполнить обработку результатов (приложение Python): построение профилей <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-1165c59bb905-dark.svg"><img src="./pic/formulas/inline-1165c59bb905-light.svg" alt="T(x)" height="15"></picture> и <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7695d2a56e69-dark.svg"><img src="./pic/formulas/inline-7695d2a56e69-light.svg" alt="\theta(\xi)" height="16"></picture>, графиков <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture> и <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> от <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture> с наложением аналитики, расчет отклонений и сводные таблицы сходимости.

---

## 6. Сравнение с аналитическим решением

Для проверки результатов расчета использовалось аналитическое решение формулы (2)–(4). Полученные расчетные оценки:


| <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture>, Вт/(м²·К) | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture>, К | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture>, Вт | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> |
|---------------------------:|-----------:|----------------:|----------:|
| 3                          | 383.2435   | 3.3614          | 0.9337    |
| 5                          | 377.5051   | 5.3705          | 0.8951    |
| 10                         | 365.5023   | 9.7623          | 0.8135    |
| 25                         | 342.0889   | 19.5            | 0.65      |
| 50                         | 322.4829   | 30.2317         | 0.5039    |


С помощью приложения [`Q_eta_calculator`](https://github.com/ArtemNarimanov/Q_eta_calculator), написанного на Python, из результатов КОРСАР получены следующие значения:


| <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture>, Вт/(м²·К) | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture>, К | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture>, Вт | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> |
|---------------------------:|-----------:|----------------:|----------:|
| 3                          | 383.5      | 3.37            | 0.936     |
| 5                          | 377.8      | 5.391           | 0.8986    |
| 10                         | 366        | 9.831           | 0.8193    |
| 25                         | 342.8      | 19.78           | 0.6593    |
| 50                         | 323.2      | 30.9            | 0.5151    |


В SMath Solver получены отклонения данных на основе Корсара от аналитической оценки:


| <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture>, Вт/(м²·К) | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-6af80f5bfd31-dark.svg"><img src="./pic/formulas/inline-6af80f5bfd31-light.svg" alt="\Delta T(L)" height="15"></picture>, К | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-12a6885b421a-dark.svg"><img src="./pic/formulas/inline-12a6885b421a-light.svg" alt="\Delta\dot{Q}" height="20"></picture>, Вт | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-29a0844b4f58-dark.svg"><img src="./pic/formulas/inline-29a0844b4f58-light.svg" alt="\Delta\eta_f" height="16"></picture> |
|---------------------------:|-------------------:|-----------------------:|-----------------:|
| 3                          | 0.2565             | 0.0086                 | 0.0023           |
| 5                          | 0.2949             | 0.0205                 | 0.0035           |
| 10                         | 0.4977             | 0.0687                 | 0.0058           |
| 25                         | 0.7111             | 0.28                   | 0.0093           |
| 50                         | 0.7171             | 0.6683                 | 0.0112           |


В SMath Solver получены отклонения в процентах:


| <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture>, Вт/(м²·К) | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture>, % | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture>, % | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture>, % |
|---------------------------:|----------:|-------------:|-------------:|
| 3                          | 0.0669    | 0.2552       | 0.2457       |
| 5                          | 0.0781    | 0.3803       | 0.3895       |
| 10                         | 0.136     | 0.6988       | 0.7079       |
| 25                         | 0.2074    | 1.4156       | 1.4106       |
| 50                         | 0.2219    | 2.1628       | 2.1743       |


Самое подробное решение представлено вариантом с альфой 50, количеством ячеек по высоте 50, количеством ячеек по толщине 7. Аналитическое решение с такой же сеткой сделано в SMath Solver.

Отклонения результатов, полученных в РК Корсар, от аналитической оценки посчитаны по формуле:


<picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/equation-1fea5bbaad67-dark.svg"><img src="./pic/formulas/equation-1fea5bbaad67-light.svg" alt="\Delta T_i = T_i^{\text{КОРСАР}} - T_i^{\text{ан}}." height="21"></picture>


Максимальное отклонение посчитано по формуле:


<picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/equation-06cbe04adad6-dark.svg"><img src="./pic/formulas/equation-06cbe04adad6-light.svg" alt="\Delta T_{\max} = \max_{1\le i\le n}\left\lvert\Delta T_i\right\rvert." height="26"></picture>


Максимальное отклонение составляет 3,47 К, это 1,1837 %

Среднее отклонение посчитано по формуле


<picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/equation-d52e035d3f6c-dark.svg"><img src="./pic/formulas/equation-d52e035d3f6c-light.svg" alt="\operatorname{MAE} = \frac{1}{n}\sum_{i=1}^{n}\left\lvert\Delta T_i\right\rvert." height="43"></picture>


Среднее отклонение составило 1,5659 К.

Среднеквадратичное отклонение посчитано по формуле:


<picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/equation-2c7b73bc4fb1-dark.svg"><img src="./pic/formulas/equation-2c7b73bc4fb1-light.svg" alt="\operatorname{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(\Delta T_i)^2}." height="48"></picture>


Оно составило 1,7832 К.

Проведены расчеты на сеточную сходимость по длине. Результаты для варианта с альфой 50 показаны в таблице:


| <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-a5b94796d549-dark.svg"><img src="./pic/formulas/inline-a5b94796d549-light.svg" alt="N-1" height="12"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture>, К | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture>, Вт | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> |
|------:|-----------:|----------------:|----------:|
| 5     | 328.5      | 35.44           | 0.5906    |
| 10    | 324.8      | 32.43           | 0.5405    |
| 20    | 323.2      | 30.9            | 0.5151    |
| 30    | 322.6      | 30.33           | 0.5055    |
| 40    | 322.2      | 29.99           | 0.4998    |
| 50    | 322        | 29.74           | 0.4957    |


Относительные отклонения от аналитики приведены в таблице


| <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-a5b94796d549-dark.svg"><img src="./pic/formulas/inline-a5b94796d549-light.svg" alt="N-1" height="12"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture>, % | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture>, % | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture>, % |
|------:|----------:|-------------:|-------------:|
| 5     | 1.865866  | 17.22794     | 17.20579     |
| 10    | 0.718519  | 7.271506     | 7.263346     |
| 20    | 0.222368  | 2.210594     | 2.222663     |
| 30    | 0.036312  | 0.325155     | 0.317523     |
| 40    | -0.08773  | -0.79949     | -0.81365     |
| 50    | -0.14974  | -1.62644     | -1.62731     |


Проведены расчеты на сеточную сходимость по толщине. Результаты для варианта с альфой 50 показаны в таблице:


| <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-86be9a55762d-dark.svg"><img src="./pic/formulas/inline-86be9a55762d-light.svg" alt="K" height="12"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture>, Вт | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture>, К | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> |
|----:|----------------:|-----------:|----------:|
| 3   | 30.920          | 323.2      | 0.515     |
| 5   | 30.920          | 323.2      | 0.515     |
| 7   | 30.900          | 323.2      | 0.515     |


Относительные отклонения от аналитики приведены в таблице:


| <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-86be9a55762d-dark.svg"><img src="./pic/formulas/inline-86be9a55762d-light.svg" alt="K" height="12"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture>, % | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture>, %  | <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture>, % |
|----:|-------------:|-----------:|-------------:|
| 3   | 2.27674924   | 0.22236838 | 2.2821988    |
| 5   | 2.27674924   | 0.22236838 | 2.2821988    |
| 7   | 2.210593516  | 0.22236838 | 2.202818     |


### 6.1. Выводы

1. Результаты, полученные в РК КОРСАР, с высокой точностью совпадают с аналитическими оценками. Отклонения основных величин — <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture> и <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> — не превышают 3 % для всех вариантов.
2. Получена зависимость эффективности ребра от коэффициента теплоотдачи: с увеличением <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture> эффективность ребра уменьшается.
3. Расчеты на сеточную сходимость показали, что достаточно разбиения на 40 ячеек по длине. Разбиение по толщине практически не влияет на результаты.
4. В рассматриваемых вариантах одномерное приближение правомерно при <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-24e8a551b6a1-dark.svg"><img src="./pic/formulas/inline-24e8a551b6a1-light.svg" alt="\mathrm{Bi}_{\delta} \le 0.001" height="15"></picture>. При больших значениях <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture> или большой толщине ребра, когда <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c503e776f5be-dark.svg"><img src="./pic/formulas/inline-c503e776f5be-light.svg" alt="\mathrm{Bi}_{\delta} \gg 1" height="15"></picture>, необходимо учитывать поперечные градиенты температуры и охлаждение узких кромок.


---

## 7. Используемые инструменты

Для обработки результатов КОРСАР и построения графиков использовались авторские репозитории:

| Репозиторий | Назначение в работе |
|---|---|
| [Q_eta_calculator](https://github.com/ArtemNarimanov/Q_eta_calculator) | Расчёт <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7b02c5fbbc7e-dark.svg"><img src="./pic/formulas/inline-7b02c5fbbc7e-light.svg" alt="T(L)" height="15"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture> и <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> по результатам КОРСАР (разд. 6) |
| [theta-Xi-converter](https://github.com/ArtemNarimanov/theta-Xi-converter) | Преобразование профилей температуры в относительные координаты <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7695d2a56e69-dark.svg"><img src="./pic/formulas/inline-7695d2a56e69-light.svg" alt="\theta(\xi)" height="16"></picture> |
| [-graphslab9](https://github.com/ArtemNarimanov/-graphslab9) | Построение графиков (рис. 2–34) |

---

## 8. Список литературы

1. <a id="ref-korsar"></a> **КОРСАР/В3. Руководство пользователя.** §2.3.16, с. 71–89: HCS, продольная теплопроводность, ключи TYPE, DFZ, B, TAV; §2.3.20, с. 96–98: BHEAT.
2. <a id="ref-holman"></a> **Holman J. P.** Heat Transfer. — 10th ed. — McGraw-Hill, 2010. — Гл. 2, раздел *Extended Surfaces*: прямое ребро постоянного сечения, теплоизолированный торец и эффективность.
3. <a id="ref-mit"></a> **MIT.** Thermodynamics and Propulsion. §18.2 Heat Transfer From a Fin. — Уравнения (18.8), (18.11), (18.13): уравнение ребра, профиль и мощность при теплоизолированном торце.
4. <a id="ref-miheev"></a> **Михеев, М. А.** Основы теплопередачи / М. А. Михеев, И. М. Михеева. — Изд. 2-е, стереотип. — Москва : Энергия, 1977. — 344 с. : ил.
5. <a id="ref-qeta"></a> **Q_eta_calculator.** Расчёт мощности теплоотдачи и эффективности ребра по результатам КОРСАР. — GitHub. — URL: https://github.com/ArtemNarimanov/Q_eta_calculator (дата обращения: 02.11.2026).
6. <a id="ref-theta"></a> **theta-Xi-converter.** Преобразование профилей температуры в относительные координаты <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-7695d2a56e69-dark.svg"><img src="./pic/formulas/inline-7695d2a56e69-light.svg" alt="\theta(\xi)" height="16"></picture>. — GitHub. — URL: https://github.com/ArtemNarimanov/theta-Xi-converter (дата обращения: 02.11.2026).
7. <a id="ref-graphslab"></a> **-graphslab9.** Построение графиков результатов расчёта. — GitHub. — URL: https://github.com/ArtemNarimanov/-graphslab9 (дата обращения: 02.11.2026).


## 9. Сокращения и обозначения

HCS — теплопроводящая конструкция; BHEAT — заданное граничное условие; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-72dfcfb0c470-dark.svg"><img src="./pic/formulas/inline-72dfcfb0c470-light.svg" alt="L" height="12"></picture> — высота охлаждаемой части, м; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-e5916cb731c6-dark.svg"><img src="./pic/formulas/inline-e5916cb731c6-light.svg" alt="\ell_c" height="15"></picture> — длина контактной ячейки, м; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-d203ba01eef4-dark.svg"><img src="./pic/formulas/inline-d203ba01eef4-light.svg" alt="\delta" height="14"></picture> — толщина, м; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-3e23e8160039-dark.svg"><img src="./pic/formulas/inline-3e23e8160039-light.svg" alt="b" height="14"></picture> — ширина, м; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-2d711642b726-dark.svg"><img src="./pic/formulas/inline-2d711642b726-light.svg" alt="x" height="9"></picture> — координата по высоте, м; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-a1fce4363854-dark.svg"><img src="./pic/formulas/inline-a1fce4363854-light.svg" alt="y" height="14"></picture> — координата по толщине, м; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-583cf6290785-dark.svg"><img src="./pic/formulas/inline-583cf6290785-light.svg" alt="\lambda" height="12"></picture> — теплопроводность, Вт/(м·К); <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4893e9df8b54-dark.svg"><img src="./pic/formulas/inline-4893e9df8b54-light.svg" alt="\alpha" height="10"></picture> — коэффициент теплоотдачи, Вт/(м²·К); <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-e14cb192aabe-dark.svg"><img src="./pic/formulas/inline-e14cb192aabe-light.svg" alt="T_0" height="15"></picture>, <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-9bbeb7d12eb0-dark.svg"><img src="./pic/formulas/inline-9bbeb7d12eb0-light.svg" alt="T_1" height="15"></picture> — температуры основания и воздуха; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-5494a82a5f60-dark.svg"><img src="./pic/formulas/inline-5494a82a5f60-light.svg" alt="A_c" height="15"></picture> — площадь сечения, м²; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-84cc5863a0df-dark.svg"><img src="./pic/formulas/inline-84cc5863a0df-light.svg" alt="A_f" height="15"></picture> — охлаждаемая площадь, м²; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-5c62e091b8c0-dark.svg"><img src="./pic/formulas/inline-5c62e091b8c0-light.svg" alt="P" height="12"></picture> — охлаждаемый периметр, м; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-4065187ab116-dark.svg"><img src="./pic/formulas/inline-4065187ab116-light.svg" alt="\dot{Q}" height="20"></picture> — мощность, Вт; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-c85cee5084c7-dark.svg"><img src="./pic/formulas/inline-c85cee5084c7-light.svg" alt="\eta_f" height="14"></picture> — эффективность ребра; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-19f219da7a17-dark.svg"><img src="./pic/formulas/inline-19f219da7a17-light.svg" alt="M = mL" height="12"></picture> — безразмерный параметр ребра; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-b85ee422228e-dark.svg"><img src="./pic/formulas/inline-b85ee422228e-light.svg" alt="\mathrm{Bi}_\delta = \alpha\delta/(2\lambda)" height="15"></picture> — число Био по толщине; <picture><source media="(prefers-color-scheme: dark)" srcset="./pic/formulas/inline-978e87e4f3d8-dark.svg"><img src="./pic/formulas/inline-978e87e4f3d8-light.svg" alt="\tanh" height="14"></picture> — гиперболический тангенс.

 
