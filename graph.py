import timeit
import sys
import resource

class Graph:
   def __init__(self,num_nodes):
      self.graph={};
      for i in range(0,num_nodes):
         self.graph[i]=set()
   def add_node(self, node):
      self.graph[node]=set()
   def add_edge(self, nodei, nodej):
      self.graph[nodei].add(nodej)
      self.graph[nodej].add(nodei)

   def dfs(self):
      dfs_list = {0}
      visit_list = set()
      while(dfs_list):
         node = dfs_list.pop()
         if(node in visit_list):
            continue
         #print("At node "+str(node))
         visit_list.add(node)
         " Do some random dfs bullshit"
         for child in self.graph[node]:
            dfs_list.add(child)
      print ("done")      

class Edge:
   def __init__(self,node):
      self.dest = node
class Node:
   def __init__(self,id):
      self.adj_nodes=[]
      self.id=id
   def add_egde_from(self,nodei):
      self.adj_nodes.append(nodei)
class Graph2:
   def __init__(self,num_nodes):
      self.nodes = {}
      for i in range(0,num_nodes):
         self.nodes[i]=Node(i)
   def add_edge(self,nodei,nodej):
      self.nodes[nodei].add_egde_from(self.nodes[nodej])
      self.nodes[nodej].add_egde_from(self.nodes[nodei])
   def dfs(self):
      for name,node in self.nodes.items():
         node.visited=False;
      dfs_list = {self.nodes[0]}
      while(dfs_list):
         node = dfs_list.pop()
         if(node.visited):
            continue
         node.visited=True
         #print("At node "+str(node.id))
         "random dfs stuff"
         for child in node.adj_nodes:
            dfs_list.add(child)
      print("done")


num_nodes=2000
g=Graph2(num_nodes)

def add_edges_to_graph():
   global g
   print("defining the graph")
   for i in range(0,num_nodes):
      for j in range(i+1,num_nodes):
         g.add_edge(i,j)
add_edges_to_graph()
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)


def gfunc():
   global g
   print("starting dfs")
   g.dfs()



print(timeit.timeit(gfunc,number = 10))
      

