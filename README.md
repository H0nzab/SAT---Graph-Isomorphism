# SAT---Graph-Isomorphism

Cílem je zjistit, zda jsou dva grafy $G_1 = (V_1, E_1)$ a $G_2 = (V_2, E_2)$ izomorfní. 
Zjednodušeně řečeno: chceme zjistit, jestli jde o jeden a ten samý graf, který je jen jinak nakreslený (vrcholy mají jiná jména/čísla).
K tomu hledáme tzv. bijekci (vzájemně jednoznačné zobrazení) mezi vrcholy prvního a druhého grafu, která zachovává spojení. 
Nechť mají oba grafy stejný počet vrcholů $n$.

Protože máme k dispozici pouze hodnoty true/false, tak u každého vrcholu z $G_1$ budeme zkoumat, jestli se mapuje na nějaký z n vrcholů $G_2$.
Budeme proto potřebovat $n^2$ proměnných.

Označíme si je $x_{u,w}$, kde u $\in G_1$ a w $\in G_2$.
Pokud je proměnná $x_{u,w}$ true, tak se vrchol u mapuje na vrchol w.
