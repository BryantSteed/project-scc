# Project Report - Network Analysis SCCs

## Baseline

### Design Experience

For prepost, which returns the pre and post order numbers of every node in its contituent tree map, I will define a function that iterates through the graph and calles the recursive function explore on each one; the same way that the psuedocode works. Because python dictionaries preserve insertion order, I will make another dictionary to keep track of whether they've been visited, the key will be the string of the node in the dictionary and the value a bool variable.

With that, I will simply store the pre and post order numbers in the dictionary that I will eventually return.

### Theoretical Analysis - Pre/Post Order Traversal

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data

| density factor | size  | V | E | runtime |
|----------------|-------|---|---|---------|
| 0.25           | 10    |   |   |         |
| 0.25           | 20    |   |   |         |
| 0.25           | 100   |   |   |         |
| 0.25           | 200   |   |   |         |
| 0.25           | 1000  |   |   |         |
| 0.25           | 2000  |   |   |         |
| 0.25           | 10000 |   |   |         |
| 0.5            | 10    |   |   |         |
| 0.5            | 20    |   |   |         |
| 0.5            | 100   |   |   |         |
| 0.5            | 200   |   |   |         |
| 0.5            | 1000  |   |   |         |
| 0.5            | 2000  |   |   |         |
| 0.5            | 10000 |   |   |         |
| 1              | 10    |   |   |         |
| 1              | 20    |   |   |         |
| 1              | 100   |   |   |         |
| 1              | 200   |   |   |         |
| 1              | 1000  |   |   |         |
| 1              | 2000  |   |   |         |
| 1              | 10000 |   |   |         |
| 2              | 10    |   |   |         |
| 2              | 20    |   |   |         |
| 2              | 100   |   |   |         |
| 2              | 200   |   |   |         |
| 2              | 1000  |   |   |         |
| 2              | 2000  |   |   |         |
| 2              | 10000 |   |   |         |
| 3              | 10    |   |   |         |
| 3              | 20    |   |   |         |
| 3              | 100   |   |   |         |
| 3              | 200   |   |   |         |
| 3              | 1000  |   |   |         |
| 3              | 2000  |   |   |         |
| 3              | 10000 |   |   |         |


### Comparison of Theoretical and Empirical Results

- Theoretical order of growth: *copy from section above* 
- Measured constant of proportionality for theoretical order: 

![img](img.png)

- Empirical order of growth (if different from theoretical): 

![img](img.png)


*Fill me in*

## Core

### Design Experience

I will reverse the graph given to me by iterating through the adjacency list and setting each edge that is connected to by another node to be connected to by that respective node. I will do this by iterating through the graph and creating another graph to do this during the iteration.

After running prepost on the reverse graph, I will iterate through the pre post trees and sort them based on their post order number. Then, I will run interate in the decreasing post order numbr order and run explore succesively, popping out each SCC and adding each SCC set to the list. I will then return that list.

### Theoretical Analysis - SCC

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data

| size  | density factor | V+E | runtime |
|-------|----------------|-----|---------|
| 10    | 0.25           |     |         |
| 20    | 0.25           |     |         |
| 100   | 0.25           |     |         |
| 200   | 0.25           |     |         |
| 1000  | 0.25           |     |         |
| 2000  | 0.25           |     |         |
| 10000 | 0.25           |     |         |
| 10    | 0.5            |     |         |
| 20    | 0.5            |     |         |
| 100   | 0.5            |     |         |
| 200   | 0.5            |     |         |
| 1000  | 0.5            |     |         |
| 2000  | 0.5            |     |         |
| 10000 | 0.5            |     |         |
| 10    | 1              |     |         |
| 20    | 1              |     |         |
| 100   | 1              |     |         |
| 200   | 1              |     |         |
| 1000  | 1              |     |         |
| 2000  | 1              |     |         |
| 10000 | 1              |     |         |
| 10    | 2              |     |         |
| 20    | 2              |     |         |
| 100   | 2              |     |         |
| 200   | 2              |     |         |
| 1000  | 2              |     |         |
| 2000  | 2              |     |         |
| 10000 | 2              |     |         |
| 10    | 3              |     |         |
| 20    | 3              |     |         |
| 100   | 3              |     |         |
| 200   | 3              |     |         |
| 1000  | 3              |     |         |
| 2000  | 3              |     |         |
| 10000 | 3              |     |         |


### Comparison of Theoretical and Empirical Results

- Theoretical order of growth: *copy from section above* 
- Measured constant of proportionality for theoretical order: 
- Empirical order of growth (if different from theoretical): 
- Measured constant of proportionality for empirical order: 

![img](img.png)

*Fill me in*

## Stretch 1

### Design Experience

To identify the different types of edges, I will first run prepost on the graph. I will likely need to reorganize the tree data into a cohesive dictionary that will actually get me all the prepost numbers in one call. Then I will iterate through each edge in the graph by iterating through the key and invidually connections. For each of those edges, I will construct a list that orders the pre-post numbers in order and has the identity of the node it belongs to and whether that number is a pre or post order.

I will then iterate through that list to determine if the pattern in [u[v v]u], in which case its tree/forward, [v[u u]v], in which case its back, or finally [v v] [u u], in which case it's cross.

### Articulation Points Discussion 

*Fill me in*

## Stretch 2

### Design Experience

I found a dataset from a harvard study that has supreme court decisions and how often they have cited eachother. They said in their readme that the data took a long time to collect. It has like 30,288 supreme court decisions in it. This is the link to it https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/XMBQL6. There are hundreds of thousands of edges here, and they give the whole adjacency list in allcites.txt. 

An edge from case1 -> case2 means that case1 has cited case2 in their opinion. This also means that its imposible for cases to cite eachother. I dont think that the strongly connected components will be very big because you cant have a previous case cite a case that happens after. This will be interesting to see if any cycles do actually exist in the data set. If I get any SCCS of more than one node, that would be very interesting. But my guess is that this dataset is a true DAG.

I may need to adapt the dataset and make it smaller for my algorithm because its really big. The whole folder is liek 100MB, so I don't know how my computer will be able to handle that. As far as me interpreting my results, if the data shows that its not a DAG, it would show that the data is incorrect or has some discrepancy. Or it could show that time travel was possible in the 1800's (quite the finding on its own).

### Dataset Description

*Fill me in*

### Findings Discussion

*Fill me in*

## Project Review

*Fill me in*
