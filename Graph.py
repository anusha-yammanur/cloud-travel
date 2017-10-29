"""
Graph data structure with edges and vertices info
"""
class Graph:

	def __init__(self, edges, vertices):
		self.edges = edges
		self.vertices = vertices

	def getAdjVerices(self, vertex):
		return list(self.edges[vertex.item].keys())
