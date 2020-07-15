Bonus: Dijkstra's Algorithm, A* ("A star")

Graph Representations
---------------------

* Adjacency Matrix

  A  B  C
A f  T  T

B T  f  T

C f  f  f

* Adjacency List (We'll use this)

edges = {
    'A': [B, C],
    'B': [B, A, C],  # order doesn't matter
    'C': []
}

