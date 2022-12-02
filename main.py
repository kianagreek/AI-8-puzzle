from state import State
from searches import Searches

#TEST 1
sample1=[['B',1,3],[8,2,4],[7,6,5]]
test1 =  Searches(sample1)

#bfs
print("solving: ", test1, " with breadth first search")
bfsResults = test1.bfs(sample1)
#print("search path: ")
#[print(d) for d in bfsResults]
print("depth of bfs is: ", len(bfsResults))

#dfs
print("solving: ", test1, " with depth first search")
dfsResults = test1.dfs(sample1)
#print("search path: ")
#[print(d) for d in dfsResults]
print("depth of dfs is: ", len(dfsResults))

#bestfirst search with manhattan distance
print("solving: ", test1, " with greedy best first search using manhattan distance")
bfResults = test1.bestFirt(sample1,'m')
#print("search path: ") 
#[print(d) for d in bfResults]
print("depth of bf with manhattan distance: ", len(bfResults)) 

#bestfirst search with hamming distance
print("solving: ", test1, " with greedy best first search using hamming distance")
bfResults = test1.bestFirt(sample1,'h')
#print("search path: ", len(bfResults)) 
#[print(d) for d in bfResults]
print("depth of bf with hamming distance: ", len(bfResults)) 

#bestfirst search with permutation inversion
print("solving: ", test1, " with greedy best first search using permutation inversion")
bfResults = test1.bestFirt(sample1,'p')
#print("search path: ") 
#[print(d) for d in bfResults]
print("depth of bf with permutation inversion: ", len(bfResults)) 

#bestfirst search with nilsson's sequence
print("solving: ", test1, " with greedy best first search using Nilsson's sequence")
bfResults = test1.bestFirt(sample1,'n')
#print("search path:")
#[print(d) for d in bfResults]
print("depth of bf with nilsson's sequence: ", len(bfResults)) 

#A* search with manhattan distance
print("solving: ", test1, " with A* using manhattan distance")
aStarResults = test1.aStar(sample1,'m')
#print("search path:) 
#[print(d) for d in aStarResults]
print("depth of A* with manhattan distance: ", len(aStarResults)) 

#A* search with hamming distance
print("solving: ", test1, " with A* using hamming distance")
aStarResults = test1.aStar(sample1,'h')
#print("search path:") 
#[print(d) for d in aStarResults]
print("depth of A* with hamming distance: ", len(aStarResults)) 

#A* search with permutation inversion
print("solving: ", test1, " with A* using permutation inversion")
aStarResults = test1.aStar(sample1,'p')
#print("search path") 
#[print(d) for d in aStarResults]
print("depth of A* with permutation inversion: ", len(aStarResults)) 

#A* search with nilsson's sequence
print("solving: ", test1, " with A* using Nilsson's sequence")
aStarResults = test1.aStar(sample1,'n')
#print("search path:")
#[print(d) for d in aStarResults]
print("depth of A* with nilsson's sequence: ", len(aStarResults)) 

#TEST2
sample2=[[5,1,3],[4,2,8],[7,'B',6]]
test2 =  Searches(sample2)

#bfs
print("solving: ", test2, " with breadth first search")
bfsResults = test2.bfs(sample2)
#print("search path")
#[print(d) for d in bfsResults]
print("depth of bfs is: ", len(bfsResults))

#dfs
print("solving: ", test2, " with depth first search")
dfsResults = test2.dfs(sample2)
#print("search path:")
#[print(d) for d in dfsResults]
print("depth of dfs is: ", len(dfsResults))

#bestfirst search with manhattan distance
print("solving: ", test2, " with greedy best first search using manhattan distance")
bfResults = test2.bestFirt(sample2,'m')
#print("search path:")
#[print(d) for d in bfResults]
print("depth of bf with manhattan distance: ", len(bfResults)) 

#bestfirst search with hamming distance
print("solving: ", test2, " with greedy best first search using hamming distance")
bfResults = test2.bestFirt(sample2,'h')
#print("search path:") 
#[print(d) for d in bfResults]
print("depth of bf with hamming distance: ", len(bfResults)) 

#bestfirst search with permutation inversion
print("solving: ", test2, " with greedy best first search using permutation inversion")
bfResults = test2.bestFirt(sample2,'p')
#print("search path: ")
#[print(d) for d in bfResults]
print("depth of bf with permutation inversion: ", len(bfResults)) 

#bestfirst search with nilsson's sequence
print("solving: ", test2, " with greedy best first search using Nilsson's sequence")
bfResults = test2.bestFirt(sample2,'n')
#print("search path:")
#[print(d) for d in bfResults]
print("depth of bf with nilsson's sequence: ", len(bfResults)) 

#A* search with manhattan distance
print("solving: ", test2, " with A* using manhattan distance")
aStarResults = test2.aStar(sample2,'m')
#print("search path:")
#[print(d) for d in aStarResults]
#print("depth of A* with manhattan distance: ", len(aStarResults))

#A* search with hamming distance
print("solving: ", test2, " with A* using hamming distance")
aStarResults = test2.aStar(sample2,'h')
depth = len(aStarResults)
#print("search path:")
#print("depth of A* with hamming distance: ", depth) 
[print(d) for d in aStarResults]

#A* search with permutation inversion
print("solving: ", test2, " with A* using permutation inversion")
aStarResults = test2.aStar(sample2,'p')
#print("search path:")
#[print(d) for d in aStarResults]
print("depth of A* with permutation inversion: ", len(aStarResults)) 

#A* search with nilsson's sequence
print("solving: ", test2, " with A* using Nilsson's sequence")
aStarResults = test2.aStar(sample2,'n')
depth = len(aStarResults) 
#print("search path:")
#[print(d) for d in aStarResults]
print("depth of A* with nilsson's sequence: ", depth)

#TEST3
sample3=[[2,8,3],[1,6,4],[7,'B',5]] #challenge config
test3 =  Searches(sample3)

#bfs
print("solving: ", test3, " with breadth first search")
bfsResults = test3.bfs(sample3)
#print("search path:")
#[print(d) for d in bfsResults]
print("depth of bfs is: ", len(bfsResults))

#dfs
print("solving: ", test3, " with depth first search")
dfsResults = test3.dfs(sample3)
#print("search path:")
#[print(d) for d in dfsResults]
print("depth of dfs is: ", len(dfsResults))

#bestfirst search with manhattan distance
print("solving: ", test3, " with greedy best first search using manhattan distance")
bfResults = test3.bestFirt(sample3,'m')
#print("printing closed list")
#[print(d) for d in bfResults]
print("depth of bf with manhattan distance: ", len(bfResults)) 

#bestfirst search with hamming distance
print("solving: ", test3, " with greedy best first search using hamming distance")
bfResults = test3.bestFirt(sample3,'h')
#print("printing path") 
#[print(d) for d in bfResults]
print("depth of bf with hamming distance: ", len(bfResults)) 

#bestfirst search with permutation inversion
print("solving: ", test3, " with greedy best first search using permutation inversion")
bfResults = test3.bestFirt(sample3,'p')
#print("printing path ") 
#[print(d) for d in bfResults]
print("depth of bf with permutation inversion: ", len(bfResults)) 

#bestfirst search with nilsson's sequence
print("solving: ", test3, " with greedy best first search using Nilsson's sequence")
bfResults = test3.bestFirt(sample3,'n')
#print("printing path")
#[print(d) for d in bfResults]
print("depth of bf with nilsson's sequence: ", len(bfResults)) 

#A* search with manhattan distance
print("solving: ", test3, " with A* using manhattan distance")
aStarResults = test3.aStar(sample3,'m')
#print("printing path") 
#[print(d) for d in aStarResults]
print("depth of A* with manhattan distance: ", len(aStarResults)) 

#A* search with hamming distance
print("solving: ", test3, " with A* using hamming distance")
aStarResults = test3.aStar(sample3,'h')
depth = len(aStarResults)
#print("printing path") 
#[print(d) for d in aStarResults]
print("depth of A* with hamming distance: ", depth) 

#A* search with permutation inversion
print("solving: ", test3, " with A* using permutation inversion")
aStarResults = test3.aStar(sample3,'p')
#print("printing path")
#[print(d) for d in aStarResults]
print("depth of A* with permutation inversion: ", len(aStarResults))

#A* search with nilsson's sequence
print("solving: ", test3, " with A* using Nilsson's sequence")
aStarResults = test3.aStar(sample3,'n')
depth = len(aStarResults) 
#print("search path:")
#[print(d) for d in aStarResults]
print("depth of A* with nilsson's sequence: ", depth)

#TEST4
sample4=[[5,1,4],[7,'B',6],[3,8,2]] #greater challenge config
test4 =  Searches(sample4)
#bfs
print("solving: ", test4, " with breadth first search")
bfsResults = test4.bfs(sample4)
#print("search path")
#[print(d) for d in bfsResults]
print("depth of bfs is: ", len(bfsResults))

#dfs
print("solving: ", test4, " with depth first search")
dfsResults = test4.dfs(sample4)
#print("search path: ")
#[print(d) for d in dfsResults]
print("depth of dfs is: ", len(dfsResults))

#bestfirst search with manhattan distance
print("solving: ", test4, " with greedy best first search using manhattan distance")
bfResults = test4.bestFirt(sample4,'m')
#print("printing closed list")
#[print(d) for d in bfResults]
print("depth of bf with manhattan distance: ", len(bfResults)) 

#bestfirst search with hamming distance
print("solving: ", test4, " with greedy best first search using hamming distance")
bfResults = test4.bestFirt(sample4,'h')
#print("printing path") 
#[print(d) for d in bfResults]
print("depth of bf with hamming distance: ", len(bfResults)) 

#bestfirst search with permutation inversion
print("solving: ", test4, " with greedy best first search using permutation inversion")
bfResults = test4.bestFirt(sample4,'p')
#print("printing path ") 
#[print(d) for d in bfResults]
print("depth of bf with permutation inversion: ", len(bfResults)) 

#bestfirst search with nilsson's sequence
print("solving: ", test4, " with greedy best first search using Nilsson's sequence")
bfResults = test4.bestFirt(sample4,'n')
#print("printing path")
#[print(d) for d in bfResults]
print("depth of bf with nilsson's sequence: ", len(bfResults)) 

#A* search with manhattan distance
print("solving: ", test4, " with A* using manhattan distance")
aStarResults = test4.aStar(sample4,'m')
#print("printing path") 
#[print(d) for d in aStarResults]
print("depth of A* with manhattan distance: ", len(aStarResults)) 

#A* search with hamming distance
print("solving: ", test4, " with A* using hamming distance")
aStarResults = test4.aStar(sample4,'h')
depth = len(aStarResults)
#print("search path:")
#[print(d) for d in aStarResults]
print("depth of A* with hamming distance: ", depth) 

#A* search with permutation inversion
print("solving: ", test4, " with A* using permutation inversion")
aStarResults = test4.aStar(sample4,'p')
#print("printing path")
#[print(d) for d in aStarResults]
print("depth of A* with permutation inversion: ", len(aStarResults))

#A* search with nilsson's sequence
print("solving: ", test4, " with A* using Nilsson's sequence")
aStarResults = test4.aStar(sample4,'n')
depth = len(aStarResults) 
#print("search path:")
#[print(d) for d in aStarResults]
print("depth of A* with nilsson's sequence: ", depth)

#TEST5
sample5=[[4,5,1],[3,6,'B'],[8,7,2]] #greater challenge config
test5 =  Searches(sample5)

#bfs
print("solving: ", test5, " with breadth first search")
bfsResults = test5.bfs(sample5)
#print("search path: ")
#[print(d) for d in bfsResults]
print("depth of bfs is: ", len(bfsResults))

#dfs
print("solving: ", test5, " with depth first search")
dfsResults = test5.dfs(sample5)
#print("search path: ")
#[print(d) for d in dfsResults]
print("depth of dfs is: ", len(dfsResults))

#bestfirst search with manhattan distance
print("solving: ", test5, " with greedy best first search using hamming distance")
bfResults = test5.bestFirt(sample5,'m')
#print("printing closed list")
#[print(d) for d in bfResults]
print("depth of bf with manhattan distance: ", len(bfResults)) 

#bestfirst search with hamming distance
print("solving: ", test5, " with greedy best first search using hamming distance")
#print("printing path") 
#[print(d) for d in bfResults]
print("depth of bf with hamming distance: ", len(bfResults)) 

#bestfirst search with permutation inversion
print("solving: ", test5, " with greedy best first search using permutation inversions")
bfResults = test5.bestFirt(sample5,'p')
#print("printint path ") 
#[print(d) for d in bfResults]
print("depth of bf with permutation inversion: ", len(bfResults)) 

#bestfirst search with nilsson's sequence
print("solving: ", test5, " with greedy best first search using Nilsson's sequence")
bfResults = test5.bestFirt(sample5,'n')
#print("printing path")
#[print(d) for d in bfResults]
print("depth of bf with nilsson's sequence: ", len(bfResults)) 

#A* search with manhattan distance
print("solving: ", test5, " with A* using manhattan distance")
aStarResults = test5.aStar(sample5,'m')
#print("printing path") 
#[print(d) for d in aStarResults]
print("depth of A* with manhattan distance: ", len(aStarResults)) 

#A* search with hamming distance
print("solving: ", test5, " with A* using hamming distance")
aStarResults = test5.aStar(sample5,'h')
depth = len(aStarResults)
#print("printing path") 
#[print(d) for d in aStarResults]
print("depth of A* with hamming distance: ", depth) 

#A* search with permutation inversion
print("solving: ", test5, " with A* using permutation inversion")
aStarResults = test5.aStar(sample5,'p')
#print("printing path")
#[print(d) for d in aStarResults]
print("depth of A* with permutation inversion: ", len(aStarResults))

#A* search with nilsson's sequence
print("solving: ", test5, " with A* using Nilsson's sequence")
aStarResults = test5.aStar(sample5,'n')
depth = len(aStarResults) 
#[print(d) for d in aStarResults]
print("depth of A* with nilsson's sequence: ", depth)