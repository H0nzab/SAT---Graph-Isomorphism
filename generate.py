import random
import sys

n = int(sys.argv[1])
filepath = sys.argv[2]
d = 4 if n >= 5 else (2 if n >= 3 else 1)

while True:
    stubs = [v for v in range(n) for _ in range(d)]
    random.shuffle(stubs)
    edges = set()
    for i in range(0, len(stubs), 2):
        u, v = stubs[i], stubs[i + 1]
        if u == v:
            break
        edge = (min(u, v), max(u, v))
        if edge in edges:
            break
        edges.add(edge)
    else:
        break

edges1 = list(edges)
perm = list(range(n))
random.shuffle(perm)
edges2 = [(min(perm[u], perm[v]), max(perm[u], perm[v])) for u, v in edges1]
random.shuffle(edges1)
random.shuffle(edges2)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(f"{n} {len(edges1)} {len(edges2)}\n")
    for u, v in edges1:
        f.write(f"{u} {v}\n")
    for u, v in edges2:
        f.write(f"{u} {v}\n")