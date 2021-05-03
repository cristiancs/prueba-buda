import json
def isValidStructure(jsonData):
    if "stations" not in jsonData:
       
        return False
    for station in jsonData['stations']:
        if "connectedStations" not in jsonData['stations'][station] or "color" not in jsonData['stations'][station]:
            return False
    return True
def parse_input(fileName):
    with open(fileName) as file:
        jsonData = json.load(file)
    
    if isValidStructure(jsonData):
       return jsonData['stations']
    else:
        raise ValueError("Invalid File format")