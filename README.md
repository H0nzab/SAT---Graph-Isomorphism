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
