from Graph import Graph
from Item import Item
from Heap import Heap

class Dijkstra:

	"""
	Computes shortest path from source to destination if path exists else returns -1
	"""
	def singleSourceToDest(self, G, src, dest):
		
		"""
		Priority Queue object using minheap DS
		"""
		PQ = Heap(1)
		"""
		Preparing source item object to keep on PQ
		"""
		s = Item(src, 0)
		PQ.insert(s)
		
		"""
		dist array where dist[i] contains shortest distance to ith vertex from source s
		"""
		dist = []

		"""
		Initially none of the vertices are visited and are at a distance of -1 from source
		"""
		for vertex in G.vertices:
			dist.insert(vertex, -1)
		
		"""
		src to src distance is 0
		"""
		dist[src] = 0

		path = {}
		
		while (PQ.isEmpty() == False):
			
			v = PQ.deleteMin()

			"""
			reached destination hence print path and return distance
			"""
			if (v.item == dest):
				print path
				return dist[v.item]

			"""
			computes new distance for the adjacent vertices with respect to current vertex and updates if it is less than old distance from s
			"""
			adjVertices = G.getAdjVerices(v)

			for adjVertex in adjVertices:
				edgLen = G.edges[v.item].get(adjVertex)
				
				if (edgLen != "None"):
					newDist = dist[v.item] + edgLen
				else:
					newDist = -1

				adjVertex = int(adjVertex)
				
				"""
				If this vertex was not visited till now from source and can be reached from current vertex now
					Update distance and insert item into priority queue with new distance as priority
				Else If	New distance is less than old distance. 
					Update distance and priority of adjVertex to new distance on min Heap
				"""
				if (dist[adjVertex] == -1 and newDist != -1):
					dist[adjVertex] = newDist
					w = Item(adjVertex, newDist)
					path[adjVertex] = v.item
					PQ.insert(w)
				elif (dist[adjVertex] > newDist):
					dist[adjVertex] = newDist
					path[adjVertex] = v.item
					PQ.updatePriority(adjVertex, newDist)
		
		"""
		Destination cannot be reached. Hence return -1
		"""
		return -1
