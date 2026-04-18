---
## Front matter
title: "Лабораторная работа № 5."
subtitle: "Дискреционное  разграничение прав в Linux. Исследование влияния дополнительных атрибутов"
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

Изучение механизмов изменения идентификаторов, применения
SetUID- и Sticky-битов. Получение практических навыков работы в кон-
соли с дополнительными атрибутами. Рассмотрение работы механизма
смены идентификатора процессов пользователей, а также влияние бита
Sticky на запись и удаление файлов

# Задание




# Выполнение лабораторной работы

устоновка недостающих пакетов(рис. [-@fig:001]).

![001](image/1.png){#fig:001 width=70%}


проверка пакетов(рис. [-@fig:002]).

![002](image/2.png){#fig:002 width=70%}




создание файла и компиляция (рис. [-@fig:003]).

![003](image/3.png){#fig:003 width=70%}



сравнение с id (рис. [-@fig:004]).

![004](image/4.png){#fig:004 width=70%}



создание файла 2 и компиляция (рис. [-@fig:005]).

![005](image/5.png){#fig:005 width=70%}


изменение правил и владельца (рис. [-@fig:006]).

![006](image/6.png){#fig:006 width=70%}




запуск (рис. [-@fig:007]).

![007](image/7.png){#fig:007 width=70%}



открываем (рис. [-@fig:008]).

![008](image/8.png){#fig:008 width=70%}



меняем правила (рис. [-@fig:009]).

![009](image/9.png){#fig:009 width=70%}


скомпилируем (рис. [-@fig:010]).

![010](image/10.png){#fig:010 width=70%}




setU`D-бит  (рис. [-@fig:011]).

![011](image/11.png){#fig:011 width=70%}



попытка прочитать этот файл (рис. [-@fig:012]).

![012](image/12.png){#fig:012 width=70%}


попытка прочитать этот файл (рис. [-@fig:013]).

![013](image/13.png){#fig:013 width=70%}




работаем с правами (рис. [-@fig:014]).

![014](image/14.png){#fig:014 width=70%}



работаем с правами (рис. [-@fig:015]).

![015](image/15.png){#fig:015 width=70%}


работаем с правами (рис. [-@fig:016]).

![016](image/16.png){#fig:016 width=70%}




работаем с правами (рис. [-@fig:017]).

![017](image/17.png){#fig:017 width=70%}







# Выводы

Мы научились пользовватся SetUID- и Sticky-битов

