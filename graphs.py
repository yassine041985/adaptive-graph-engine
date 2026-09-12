import networkx as nx 
import matplotlib.pyplot as plt

# Create the graph

G = nx.MultiDiGraph()

# Add nodes 

G.add_node("salesforce")
G.add_node("customer_raw")
G.add_node("customer_clean")
G.add_node("revenue_model")
G.add_node("executive_dashboard")


# Add edges (relationships)

G.add_edge("salesforce","customer_raw", relationsip = "INGESTS_TO" )
G.add_edge("customer_raw","customer_clean", relationsip = "TRANSFORMS_TO" )
G.add_edge("customer_clean","revenue_model", relationsip = "FEEDS" )
G.add_edge("revenue_model","executive_dashboard", relationsip = "POWERS" )
G.add_edge("customer_clean","revenue_model", relationsip = "FEEDS" )
G.add_edge("customer_clean","revenue_model", relationsip = "VALIDATES" )
G.add_edge("customer_clean","revenue_model", relationsip = "DEPENDENCY_OF" )
G.add_edge("executive_dashboard","salesforce", relationsip = "VISUALISED" )


# 1-hop navigation: Graph navigation / traversal

downstream = list(G.successors("customer_raw"))
upstream = list(G.predecessors("customer_raw"))

# Multi-hop navigation: all downstream (descendants) and all upstream (ancestors)

all_downstream = nx.descendants(G,"customer_raw")
all_upstream = nx.ancestors(G,"customer_raw")

print("Nodes: ",G.nodes)
print("Edges: ", G.edges(data=True))
print("one step forward", downstream)
print("one step backward", upstream)

print("All downstream: ", all_downstream)
print("All upstream", all_upstream)

nx.draw(G, with_labels=True)
plt.show()
