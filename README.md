pgmpy-test
==========

A test to see which graph structure is better

Just change the variable g = Graph(num_nodes) or g = Graph2(num_nodes) to see the desired effect


I did the experiment and found some really interesting results. So first of all I made two graph classes.

Class Graph : The graph class uses the networkx structure . Basically it has a dict of nodes. Each node is a set of other node names.

Class Graph2 : This is a list of nodes. Each of the nodes contains a list of other node objects.

Now I made a graph with 2000 nodes and connected all the nodes with each other.
The memory consumed by Graph was 328 MB and the memory consumed by Graph2 was 42MB. (I also read some references online which said that dictionaries typically need 10x memory as compared to lists , so this was not so surprising.)

Now I just ran a search on these two graphs. The dfs on Graph took 0.68 seconds and a dfs on the Graph2 took 0.30 seconds on an average of 10 runs.

These results are really surprising and the performance difference is quite a lot. Also, I believe that most of the algorithms we use don't really require a lot of direct edge or node accesses and hence the performance benefits of dictionaries might not be really helpful to us. 
