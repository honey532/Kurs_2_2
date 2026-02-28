---
## Front matter
title: "Этап 1"
subtitle: "Установка Kali Linux"
author: "Глобин Никита Анатольевич"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: IBM Plex Serif
romanfont: IBM Plex Serif
sansfont: IBM Plex Sans
monofont: IBM Plex Mono
mathfont: STIX Two Math
mainfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
romanfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
sansfontoptions: Ligatures=Common,Ligatures=TeX,Scale=MatchLowercase,Scale=0.94
monofontoptions: Scale=MatchLowercase,Scale=0.94,FakeStretch=0.9
mathfontoptions:
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Установка Kali Linux

# Задание

- Установка Kali Linux


# Выполнение лабораторной работы

Подключаем образ(рис. [-@fig:001]).

![001](image/1.png){#fig:001 width=70%}


Первоначальная настройка (рис. [-@fig:002])(рис. [-@fig:003]).

![002](image/2.png){#fig:002 width=70%}

![003](image/3.png){#fig:003 width=70%}

Устоновака (рис. [-@fig:004]).

![004](image/4.png){#fig:004 width=70%}


выбор языка  (рис. [-@fig:005]).

![005](image/5.png){#fig:005 width=70%}


настойка пользователя (рис. [-@fig:006])(рис. [-@fig:007])(рис. [-@fig:008])(рис. [-@fig:009]).

![006](image/6.png){#fig:006 width=70%}

![007](image/7.png){#fig:007 width=70%}

![008](image/8.png){#fig:008 width=70%}

![009](image/9.png){#fig:009 width=70%}


настройка хранилища (рис. [-@fig:010])(рис. [-@fig:011])(рис. [-@fig:012])(рис. [-@fig:013])(рис. [-@fig:014])(рис. [-@fig:015]).

![010](image/10.png){#fig:010 width=70%}

![011](image/11.png){#fig:011 width=70%}

![012](image/12.png){#fig:012 width=70%}

![013](image/13.png){#fig:013 width=70%}

![014](image/14.png){#fig:014 width=70%}

![015](image/15.png){#fig:015 width=70%}


настройка системы (рис. [-@fig:016])(рис. [-@fig:017]).(рис. [-@fig:018]).

![016](image/16.png){#fig:016 width=70%}

![017](image/17.png){#fig:017 width=70%}

![018](image/18.png){#fig:018 width=70%}







# Выводы

По ходу работы мы устоновили Kali Linux


