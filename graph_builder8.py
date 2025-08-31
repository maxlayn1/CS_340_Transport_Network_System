from adjacencylist import *

def createList(path):
    to_adjacency_list(path)

def main():
    createList(str(sys.argv[1]))

main()