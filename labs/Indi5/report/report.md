---
## Front matter
title: "Этап 4."
subtitle: "Использование Burp Suite"
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

Изучить архитектуру и функциональные возможности Burp Suite как инструмента для анализа безопасности веб-приложений, а также освоить практические методы перехвата, модификации и анализа HTTP-трафика для выявления типовых уязвимостей.


# Задание

1. Установка и настройка прокси-сервера Burp Suite

2. Анализ и модификация HTTP-запросов вручную 

# Выполнение лабораторной работы

запускаем  Burp Suite(рис. [-@fig:001]).

![001](image/1.png){#fig:001 width=70%}



создаём временный проект в Burp Suite(рис. [-@fig:002]).

![002](image/2.png){#fig:002 width=70%}



отсеживаем как проходит перехваит при регистрации в Burp Suite(рис. [-@fig:003]).

![003](image/3.png){#fig:003 width=70%}



смотреи что мы перехвотили в Burp Suite(рис. [-@fig:004]).

![004](image/4.png){#fig:004 width=70%}




# Выводы

мы научились анализировать и работать с Burp Suite

