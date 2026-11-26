# SAT projekt - Isomorfismus grafů

  

Řešení problému izomorfismu dvou jednoduchých neorientovaných grafů převodem na splnitelnost booleovské formule v konjunktivní normální formě (DIMACS CNF) pomocí SAT solveru **Glucose 4.2**.



## 1. Matematický popis problému

  

Vstupem jsou dva jednoduché neorientované grafy $G_1 = (V_1, E_1)$ a $G_2 = (V_2, E_2)$ se stejným počtem vrcholů $|V_1| = |V_2| = n$, které v obou grafech indexujeme $0, 1, \dots, n-1$. Cílem je najít bijekci $f: V_1  \to V_2$ zachovávající sousednost vrcholů:

  

$$\forall u, v \in V_1 \ (u \neq v): \quad \{u, v\} \in E_1  \iff \{f(u), f(v)\} \in E_2$$

  

Pokud $|E_1| \neq |E_2|$, izomorfismus neexistuje a program končí ještě před sestavením CNF formule.

  

### Rozhodovací proměnné

Zavádíme $n^2$ booleovských proměnných $x_{u,w}$ pro všechna $u \in V_1$ a $w \in V_2$:

* $x_{u,w} = \text{True} \iff f(u) = w$ (vrchol $u$ z grafu $G_1$ se zobrazí na vrchol $w$ z grafu $G_2$).

  

### Constraints

  

**A. Bijekce mezi množinami vrcholů $V_1$ a $V_2$:**

1.  *Každý vrchol $u \in V_1$ se zobrazí alespoň na jeden vrchol v $V_2$:*

$$\forall u \in V_1: \quad  \bigvee_{w=0}^{n-1} x_{u,w}$$

2.  *Každý vrchol $u \in V_1$ se zobrazí nejvýše na jeden vrchol v $V_2$:*

$$\forall u \in V_1, \forall w, z \in V_2 \ (w < z): \quad  \neg x_{u,w} \lor  \neg x_{u,z}$$

3.  *Na každý vrchol $w \in V_2$ se zobrazí alespoň jeden vrchol z $V_1$:*

$$\forall w \in V_2: \quad  \bigvee_{u=0}^{n-1} x_{u,w}$$

4.  *Na každý vrchol $w \in V_2$ se zobrazí nejvýše jeden vrchol z $V_1$:*

$$\forall w \in V_2, \forall u, v \in V_1 \ (u < v): \quad  \neg x_{u,w} \lor  \neg x_{v,w}$$

  

**B. Zachování struktury hran:**

5.  *Pokud dvojice vrcholů $(u, v)$ v $G_1$ má jiný vztah než dvojice $(w, z)$ v $G_2$, nemohou současně platit přiřazení $f(u) = w$ a $f(v) = z$:*

$$\forall u, v \in V_1 \ (u < v), \forall w, z \in V_2 \ (w \neq z): \quad  \big(\{u, v\} \in E_1  \iff \{w, z\} \notin E_2\big) \implies (\neg x_{u,w} \lor  \neg x_{v,z})$$

## 2. Zakódování do CNF

### Zvolené kódování

Formát DIMACS CNF vyžaduje číslování proměnných celými čísly od $1$ do $n^2$. Převod indexů $(u, w)$ na ID proměnné a zpětné dekódování modelu probíhá podle vztahů:


$$\text{ID}(u, w) = u \cdot n + w + 1, \qquad u = \lfloor (\text{ID} - 1) / n \rfloor, \quad w = (\text{ID} - 1) \bmod n$$
  

*  **Počet proměnných:** $n^2$

*  **Počet klauzulí:**

* podmínky bijekce (1–4): $2n + n^2(n - 1)$ klauzulí,

* podmínka zachování hran (5): $4m\left(\binom{n}{2} - m\right)$ binárních klauzulí (kde $m = |E_1| = |E_2|$).

## 3. Uživatelská dokumentace


### Požadavky

* Python 3.10+

* Zkompilovaný SAT solver **Glucose 4.2**

### Spuštění

Z kořenové složky repozitáře:

```bash

python3  src/main.py

```

Na řádce 31 v `main.py` je proměnná `filepath`. V té nastavujeme vstupní soubor s cestou. Sestavená CNF formule v DIMACS formátu se při každém spuštění uloží do souboru `instances/output.cnf`.


Pro generování testovacích izomorfních grafů slouží pomocný skript `generate.py`:

```bash

python3  generate.py <pocet_vrcholu> <vystupni_soubor>

```

### Formát vstupního souboru

Textový soubor, vrcholy jsou indexovány `0` až `n - 1`:

```text

n m1 m2

u1 v1

...

u2 v2

...

```

*  `n` – počet vrcholů v obou grafech

*  `m1`, `m2` – počet hran prvního a druhého grafu

* následuje `m1` řádků s hranami grafu $G_1$ a `m2` řádků s hranami grafu $G_2$.


### Formát výstupu

*  **SAT:** vypíše nalezenou bijekci po řádcích ve tvaru `u -> w` ($u \in V_1, w \in V_2$).

*  **UNSAT:** vypíše zprávu, že grafy nejsou izomorfní.

A nakonec program vypíše čas běhu SAT solveru v sekundách
