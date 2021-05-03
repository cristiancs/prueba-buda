import sys


if(len(sys.argv) < 3):
    print("Usage: python main.py INPUTFILE START_STATION FINISH_STATION [TRAIN_COLOR]")
    print("Example: \n   python main.py input.txt A F red")
    print("Example: \n   python main.py input.txt A F green")
    print("Example: \n   python main.py input.txt A F")