import math
from collections import deque

class BFSService:
    def __init__(self, data, color):
        self.data = data
        self.color = color

    def getNeighbourWeight(self, neighbour, weight, stopTime):
        ''' Assigns weights for stations based on the color of the train and the station color '''
        if self.color == '':
            return weight + stopTime
        if self.color == self.data[neighbour]['color']:
            return weight + stopTime
        if self.data[neighbour]['color'] == '':
            return weight + stopTime
        return weight
    
    def cleanPath(self, path, endNode):
        ''' Removes stations with a color different to the train color (it the train as a color) '''
        clearedPath = []
        for station in path:
            if self.getNeighbourWeight(station, 1, 1) == 2:
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
        
        viablePaths = []
        queue.append([startNode])


        while queue:
            path = queue.popleft()
            name = path[-1]
            stationData = self.data[name]

            if name == endNode:
                viablePaths.append([weight[name], path])

            for neighbour, currentWeight in stationData['connectedStations'].items():
                weightNeighbour = self.getNeighbourWeight(neighbour, currentWeight, self.data[neighbour]['stopTime'])
       
                optionWeight = weight[name] + weightNeighbour
                if weight[neighbour] >= optionWeight:
                    weight[neighbour] = optionWeight
                    new_path = list(path)
                    new_path.append(neighbour)
                    
                    if weightNeighbour == 0:
                        queue.appendleft(new_path)
                    else:
                        queue.append(new_path)
        viablePaths = sorted(viablePaths)
        print(viablePaths)
        print(self.cleanPath(viablePaths[0][1],  endNode))
        if(len(viablePaths) == 0):                
            return []
        return  self.cleanPath(viablePaths[0][1],  endNode)