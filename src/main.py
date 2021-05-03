import sys

from services.FileHandlerService import parse_input
from services.BFSService import BFSService

if(len(sys.argv) < 4):
    print("Usage: python main.py INPUTFILE START_STATION FINISH_STATION [TRAIN_COLOR]")
    print("Example: \n   python main.py input.txt A F red")
    print("   python main.py input.txt A F green")
    print("   python main.py input.txt A F")


class Main:
   
    def __init__(self, args):
        if(len(args) < 4):
            print(args)
            raise ValueError("Missing params")
        self.input_file = args[1]
        self.start_station = args[2]
        self.finish_station = args[3]
        self.train_color = args[4] if len(args) > 4 else ""

        if not self.train_color in ["red","green",""]:
            raise ValueError("Wrong color selected, options are red, green, empty")
    def run(self):
        data = parse_input(self.input_file)
        bfs = BFSService(data, self.train_color)
        response = bfs.getRoute(self.start_station, self.finish_station)
        if len(response):
            return  "->".join(response)
        else:
            return "No Routes"

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main = Main(sys.argv)
    print(main.run())