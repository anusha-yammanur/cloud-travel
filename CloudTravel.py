from Graph import Graph
from Dijkstra import Dijkstra
import math

class CloudTravel:

	radius = 4000

	"""
	computes shortest distance beween origin and destination
	"""
	def shortestCouriertrip(self, latitude, longitude, canTravel, origin, dest):

		if(self._validateInput(latitude, longitude, canTravel, origin, dest) == True):
		
			edges = []
			airports = []

			""" Precomputes distances and stores in edges
				edges = [{1: 200, 2: 300},{2: 600, 3: 400}]
				means distance between airport 0 and 1 is 200 units
				                               0 and 2 is 300 units
	                                           1 and 2 is 600 units
	                                           1 and 3 is 400 units
			"""
			for airport, adjAirports in enumerate(canTravel):
				adjVertices = adjAirports.split(" ")
				weights = {}
			
				for adjVertex in adjVertices:
					weights[adjVertex] = self.radius * math.acos(math.sin(latitude[int(airport)]) * math.sin(latitude[int(adjVertex)] * math.cos(latitude[int(airport)]) * math.cos(latitude[int(adjVertex)]) * math.cos(longitude[int(airport)]-longitude[int(adjVertex)])))
			
				edges.append(weights)
				airports.append(airport)
			
			""" creates Graph object for the given data   """
			G = Graph(edges, airports)
			D = Dijkstra()
			print D.singleSourceToDest(G, origin, dest)
			print "\n"

	def _validateInput(self, latitude, longitude, canTravel, origin, dest):

		"""
		latitude, longitude, and canTravel will each contain the same number of elements.
		"""
		if (len(latitude) != len(longitude)):
			print "Erraneous Data \n"
			return False

		"""
		latitude, longitude, and canTravel will each contain the same number of elements.
		"""
		if (len(latitude) != len(canTravel)):
			print "Erraneous Data \n"
			return False

		"""
		latitude, longitude, and canTravel will contain between 1 and 20 elements, inclusive
		"""
		if (len(latitude) < 1 or len(latitude) > 20):
			print "Erraneous length of data \n"
			return False

		"""
		Each element of latitude will be between -89 and 89, inclusive.
		Each element of longitude will be between -179 and 179, inclusive
		Each integer represented in each element of canTravel will be between 0 and n - 1, where n is the number of elements in latitude
		"""
		for idx in range(0, len(latitude)):
			if (latitude[idx] < -89 or latitude[idx] > 89 or longitude[idx] < -179 or longitude[idx] > 179):
				print "Invalid lat/long Data \n"
				return False
			
			adjVertices = canTravel[idx].split(" ")
			for adjVertex in adjVertices:
				if (origin < 0 or origin >= len(latitude)):
					print "Invalid canTravel Data \n"
					return False

		"""
		origin and destination will be between 0 and n - 1, inclusive, where n is the number of elements in latitude
		"""
		if (origin < 0 or origin >= len(latitude) or dest < 0 or dest > len(longitude)):
			print "Invald Origin or Destiniation \n"
			return False

		"""
		No two airports will reside at the same latitude and longitude
		"""
		for idx1 in range(0, len(latitude)):
			for idx2 in range(0, len(latitude)):
				if (idx1 != idx2 and latitude[idx1] == latitude[idx2] and longitude[idx1] == longitude[idx2]):
					print "No two airports will reside at same latitude and longitude \n"
					return False

		return True