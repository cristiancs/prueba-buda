import math
from collections import deque

class BFSService:
    def __init__(self, data, color):
        self.data = data
        self.color = color

    def getNeighbourWeight(self, neighbour):
        ''' Assigns weights for stations based on the color of the train and the station color '''
        if self.color == '':
            return 1
        if self.color == self.data[neighbour]['color']:
            return 1
        if self.data[neighbour]['color'] == '':
            return 1
        return 0
    
    def cleanPath(self, path, endNode):
        ''' Removes stations with a color different to the train color (it the train as a color) '''
        clearedPath = []
        for station in path:
            if self.getNeighbourWeight(station) == 1:
                clearedPath.append(station)
        if clearedPath[-1] != endNode:
            return []
        return clearedPath

    def getRoute(self, startNode, endNode):
        if startNode not in self.data or endNode not in self.data:
            raise IndexError("Start or end node not found")
        
        weight = dict()
        queue = deque()

        for node in self.data:
            weight[node] = math.inf
        weight[startNode] = 0
        
        visited = set()

        viablePaths = []
        queue.append([startNode])


        while queue:
            path = queue.popleft()
            name = path[-1]
            stationData = self.data[name]

            if name == endNode:
                viablePaths.append(path)

            for neighbour in stationData['connectedStations']:
                
                weightNeighbour = self.getNeighbourWeight(neighbour)
                optionWeight = weight[name] + weightNeighbour
                if weight[neighbour] >= optionWeight:
                    weight[neighbour] = optionWeight
                    new_path = list(path)
                    new_path.append(neighbour)
                    
                    if weightNeighbour == 0:
                        queue.appendleft(new_path)
                    else:
                        queue.append(new_path)

                        
        if(len(viablePaths) == 0):                
            return []
        return  self.cleanPath(sorted(viablePaths, key=len)[0],  endNode)