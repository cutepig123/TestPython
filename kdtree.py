import random

class Node:pass

#build a k-d tree
def kdtree(pointList, depth=0):
	if not pointList:
		return
 
	# Select axis based on depth so that axis cycles through all valid values
	k = len(pointList[0]) # assumes all points have the same dimension
	axis = depth % k
 
	# Sort point list and choose median as pivot element
	pointList.sort(cmp=lambda x,y:cmp(x[axis],y[axis]))
	median = len(pointList)/2 # choose median
 
	# Create node and construct subtrees
	node = Node()
	node.location = pointList[median]
	node.leftChild = kdtree(pointList[0:median], depth+1)
	node.rightChild = kdtree(pointList[median+1:], depth+1)
	return node
	
#srch a elem in k-d tree
def srch(tree,node,depth=0):
	k = len(node) 
	axis = depth % k
	if node[axis] == tree.location[axis]:
		print 'find ',node , '@ depth=',depth
		if node != tree.location:
			print 'algorithm fail!'
	elif node[axis] >tree.location[axis]:
		srch(tree.rightChild,node,depth+1)
	else:
		srch(tree.leftChild,node,depth+1)
		
def  printTree(node, depth):
	if node:
		s=''
		for i in range(0,depth):
			s=s+ '\t'
		print s , node.location
		if node.leftChild:
			printTree(node.leftChild,depth+1);
		if node.rightChild:
			printTree(node.rightChild,depth+1);
			
N=20
pointList = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,1), (7,2)]
for i in range(0,N):
	a = random.choice(range(1,100))
	b = random.choice(range(1,100))
	pointList.append([a,b])

tree = kdtree(pointList)
printTree(tree,0)

M=0
for i in range(1,M):
	a = random.choice(range(1,len(pointList)))
	srch(tree,pointList[a],0)

srch(tree,(7,1),0)