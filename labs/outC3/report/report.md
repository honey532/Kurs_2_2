---
## Front matter
title: "Внешний курс"
subtitle: "часть 3"
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

-  тест 4.1
-  тест 4.2
-  тест 4.3



# Выполнение лабораторной работы

1. вопрос 1 из (рис. [-@fig:001]).

![001](image/1.png){#fig:001 width=70%}

2. вопрос 2 из (рис. [-@fig:002]).

![002](image/2.png){#fig:002 width=70%}


3. вопрос 3 из (рис. [-@fig:003]).

![003](image/3.png){#fig:003 width=70%}


4. вопрос 4 из (рис. [-@fig:004]).

![004](image/4.png){#fig:004 width=70%}


5. вопрос 5 из (рис. [-@fig:005]).

![005](image/5.png){#fig:005 width=70%}


6. вопрос 6 из (рис. [-@fig:006]).

![006](image/6.png){#fig:006 width=70%}


7. вопрос 7 из (рис. [-@fig:007]).

![007](image/7.png){#fig:007 width=70%}


8. вопрос 8 из (рис. [-@fig:008]).

![008](image/8.png){#fig:008 width=70%}


9. вопрос 9 из (рис. [-@fig:009]).

![009](image/9.png){#fig:009 width=70%}


10. вопрос 10 из (рис. [-@fig:010]).

![010](image/10.png){#fig:010 width=70%}

11. вопрос 11 из (рис. [-@fig:011]).

![011](image/11.png){#fig:011 width=70%}


12. вопрос 12 из (рис. [-@fig:012]).

![012](image/12.png){#fig:012 width=70%}


13. вопрос 13 из (рис. [-@fig:013]).

![013](image/13.png){#fig:013 width=70%}


сертификат (рис. [-@fig:014]).

![014](image/out.png){#fig:014 width=70%}





# Выводы


прошли третью часть курса. И весь курс.


