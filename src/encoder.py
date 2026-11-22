class SatEncoder:
    def __init__(self, adj1, adj2, n):
        self.adj1 = adj1
        self.adj2 = adj2
        self.n = n
        self.clauses = []

    def var_id(self, u, w):
        """
        Vrací ID proměnné pro tvrzení: vrchol u z G1 se mapuje na w z G2.
        Indexy u, w očekává od 0 do n-1.
        """
        return u * self.n + w + 1

    def _rule_1_u_at_least_one_w(self):
        """
        Pravidlo 1: Každý vrchol z G1 musí ukazovat alespoň na jeden vrchol z G2.
        """
        for u in range(self.n):
            clause = []
            for w in range(self.n):
                clause.append(self.var_id(u, w))
            
            self.clauses.append(clause)

    def _rule_2_u_at_most_one_w(self):
        """
        Pravidlo 2: Každý vrchol z G1 musí ukazovat nejvýše na jeden vrchol z G2.
        """
        for u in range(self.n):
            for w in range(self.n):
                for z in range(w + 1, self.n):
                    self.clauses.append([-self.var_id(u, w), -self.var_id(u, z)])

    def _rule_3_w_at_least_one_u(self):
        """
        Pravidlo 3: Na každý vrchol v G2 musí ukazovat nějaký vrchol z G1.
        """
        for w in range(self.n):
            clause = []
            for u in range(self.n):
                clause.append(self.var_id(u, w))
            
            self.clauses.append(clause)

    def _rule_4_w_at_most_one_u(self):
        """
        Pravidlo 4: Na každý vrchol v G2 musí ukazovat nejvýše 1 vrchol z G1.
        """
        for w in range(self.n):
            for u in range(self.n):
                for v in range(u + 1, self.n):
                    self.clauses.append([-self.var_id(u, w), -self.var_id(v, w)])

    def _rule_edges(self):
        """
        Pravidlo pro zachování struktury: Pokud má dvojice vrcholů (u, v) v G1 jiný vztah
        (hrana vs. nehrana) než dvojice (w, z) v G2, nesmí platit obojí
        mapování (u -> w i v -> z) zároveň.
        """
        for u in range(self.n):
            for v in range(u + 1, self.n):
                for w in range(self.n):
                    for z in range(self.n):
                        if w == z:
                            continue
                        if self.adj1[u][v] != self.adj2[w][z]:
                            self.clauses.append([
                                -self.var_id(u, w),
                                -self.var_id(v, z)
                            ])

    def generate_bijection(self):
        self._rule_1_u_at_least_one_w()
        self._rule_2_u_at_most_one_w()
        self._rule_3_w_at_least_one_u()
        self._rule_4_w_at_most_one_u()
        self._rule_edges()
