import sys
from encoder import SatEncoder

def load_instance(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        
    n, m1, m2 = map(int, lines[0].split())
    
    if m1 != m2:
        return None, None, n 
        
    adj1 = [[False] * n for _ in range(n)]
    adj2 = [[False] * n for _ in range(n)]
    
    idx = 1
    for _ in range(m1):
        u, v = map(int, lines[idx].split())
        adj1[u][v] = adj1[v][u] = True
        idx += 1
        
    for _ in range(m2):
        u, v = map(int, lines[idx].split())
        adj2[u][v] = adj2[v][u] = True
        idx += 1
        
    return adj1, adj2, n

if __name__ == "__main__":
    filepath = "instances/test_n2.txt" 
    
    try:
        adj1, adj2, n = load_instance(filepath)
    except FileNotFoundError:
        print(f"Soubor {filepath} nenalezen.")
        sys.exit(1)
    
    if adj1 is None:
        print("Grafy nemají stejný počet hran, nejsou izomorfní.")
        sys.exit(0)
        
    print(f"Úspěšně načteny grafy o {n} vrcholech.")

    encoder = SatEncoder(adj1, adj2, n)
    encoder.generate_bijection()
    output_path = "instances/output.cnf"
    encoder.save_dimacs(output_path)