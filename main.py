from jaal import Jaal
from jaal.datasets import load_got

edge_df, node_df = load_got()
Jaal(edge_df, node_df).plot(directed=True)
