from parser import *
import sys

def to_adjacency_list(path):
    temp = 0
    k = 0

    destArr = []
    weightArr = []

    city = parse_map_file(path)
    for src in city.adj:
        print(f"{src}:", end = " ")
        for dest in city.adj[src]:
            #print(f"{dest}", end = "")
            destArr.append(dest)
            for weight in range(city.adj[src][dest]):
                temp = temp + 1
            weightArr.append(temp)
            #print(f"({temp})", end = ", ")
            temp = 0
        while k < len(destArr):
            print(destArr[k] + "(" + str(weightArr[k]) + ")", end = "")
            if k < len(destArr) - 1:
                print(", ", end = "")
            k = k + 1
        print("")


#if __name__ == "__main__":
    #main()