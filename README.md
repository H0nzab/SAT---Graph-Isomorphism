# SAT---Graph-Isomorphism

Cílem je zjistit, zda jsou dva grafy $G_1 = (V_1, E_1)$ a $G_2 = (V_2, E_2)$ izomorfní. 
Zjednodušeně řečeno: chceme zjistit, jestli jde o jeden a ten samý graf, který je jen jinak nakreslený (vrcholy mají jiná jména/čísla).
K tomu hledáme tzv. bijekci (vzájemně jednoznačné zobrazení) mezi vrcholy prvního a druhého grafu, která zachovává spojení. 
Nechť mají oba grafy stejný počet vrcholů $n$.

## Proměnné

Protože máme k dispozici pouze hodnoty true/false, tak u každého vrcholu z $G_1$ budeme zkoumat, jestli se mapuje na nějaký z n vrcholů $G_2$.
Budeme proto potřebovat $n^2$ proměnných.

Označíme si je $x_{u,w}$, kde u $\in G_1$ a w $\in G_2$.
Pokud je proměnná $x_{u,w}$ true, tak se vrchol u mapuje na vrchol w.

## Omezení

Potřebujeme 4 podmínky:
1. Každý vrchol z $G_1$ musí ukazovat alespoň na jeden vrchol z $G_2$
   
   $X_{u,1} \lor X_{u,2} \lor X_{u,3} \dots \lor X_{u,n}$
2. Každý vrchol z $G_1$ musí ukazovat nejvýše na jeden vrchol z $G_2$
   
   Pro každou dvojici w != z:
   $\neg X_{u,w} \lor \neg X_{u,z}$
3. Na každý vrchol v $G_1$ musí ukazovat nějaký vrchol z $G_1$
   
   $X_{1,w} \lor X_{2,w} \lor X_{3,w} \dots \lor X_{n,w}$
4. Na každý vrchol v $G_2$ musí ukazovat nějvýše 1 vrchol z $G_2$
   
   Pro každou dvojici u != v:
   $\neg X_{u,w} \lor \neg X_{v,w}$

## Struktura
Hledáme konflikty, které nastanou pokud:
1. Hrana v $G_1$ existuje, ale odpovídající hrana neexistuje v $G_2$
2. Hrana v $G_1$ neexistuje, ale odpovídající hrana existuje v $G_2$
   
   $\neg (X_{u,w} \land X_{v,z})$
   neboli $\neg X_{u,w} \lor \neg X_{v,z}$

## Převod na čísla
Potřebujeme převést vrchol na celé číslo.
Použijeme funkci ID = u * n + w + 1

## Zrychlení
Pokud | $V_1$ | != | $V_2$ |, tak můžeme rovnou skončit, protože grafy nemůžou být izomorfní
