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

    def _rule_3_w_at_least_one_u(self):
        """
        Pravidlo 3: Na každý vrchol v G2 musí ukazovat nějaký vrchol z G1.
        """
        for w in range(self.n):
            clause = []
            for u in range(self.n):
                clause.append(self.var_id(u, w))
            
            self.clauses.append(clause)
