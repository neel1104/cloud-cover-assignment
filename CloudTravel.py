from Graph import Graph
from math import acos, sin, cos, radians


class CloudTravel:
    R = 4000
    def __init__(self):
        self.g = None

    @staticmethod
    def calculateDistance(p1, p2):
        lat1, lon1 = p1
        lat2, lon2 = p2
        return (
            CloudTravel.R * acos(
                sin(radians(lat1)) * sin(radians(lat2))
                + cos(radians(lat1)) * cos(radians(lat2)) *
                cos(radians(lon1 - lon2))
            )
        )
    
    @staticmethod
    def validate(p):
        assert p[0] <= 89
        assert p[0] >= -89
        assert p[1] <= 179
        assert p[1] >= -179
        return True

    def makeGraph(self, latitude, longitude, canTravel):
        n = len(latitude)
        self.g = Graph()

        # add edges
        for i in range(n):
            fromi = [int(x) for x in canTravel[i].split()]
            for j in fromi:
                self.validate([latitude[i], longitude[j]])
                p1 = (latitude[i], longitude[i])
                p2 = (latitude[j], longitude[j])

                self.g.add_edge(i, j, self.calculateDistance(p1, p2))


    def shortestCourierTrip(self, latitude, longitude, canTravel, origin, destination):
        self.makeGraph(latitude, longitude, canTravel)
        shortestdistance = self.g.dijkstra(origin, destination)
        return -1 if shortestdistance is None else shortestdistance
