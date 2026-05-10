import sys
import matplotlib.pyplot as plt
import numpy as np
import math

def printGraph(position, linkedNode, v):
    
    count = 1
    for p in position:
        plt.plot(p[0], p[1], marker = "o" , markersize = "20", color = "black")
        plt.text(p[0] , p[1], str(count), color = "white",  
                 fontsize="10", verticalalignment="center",
                 horizontalalignment="center")
        count = count + 1
    for i in linkedNode:
        [x1, x2] = position[i[0]]
        [y1, y2] = position[i[1]]
        # plt.axline(x, y, xmax = y2, ymax = x1)
        plt.plot([x1, y1], [x2, y2], color = "whitesmoke")
        
    # plt.show()

def printPath(position , path, start, end, v):
    path[end].insert(0, start)
    print (path[end])
    for i in range(0, len(path[end]) - 1):
        [x1, x2] = position[path[end][i]]
        [y1, y2] = position[path[end][i + 1]]
        plt.plot([x1, y1], [x2, y2], color = "black")
    
    arrX = np.arange(1, v + 1)
    arrY = np.arange(1, v + 1)
    plt.show()

def printMinDistance(dist, node, v):
    for i in range(0, v):
        if dist[i] == sys.maxsize:
            print("Khong co lien ket tu " + str(node + 1) + " den " + str(i + 1))
        else:
            print ("khang cach tu " + str(node + 1) + " den " + str(i + 1) + " la : " + str(dist[i]))

def minDistance(dist, sptSet, node, v):
    min = sys.maxsize
    min_index = node
    for i in range(0, v):
        if sptSet[i] == False and dist[i] <= min:
            min = dist[i]
            min_index = i
    return min_index

def dijkstra(graph, node, end, v, position):
    path = [[] for row in range(v)]
    dist = [sys.maxsize for col in range(v)]
    sptSet = [False for col in range(v)]

    dist[node] = 0

    print (dist)
    for i in range(0, v-1):
        currentNode = minDistance(dist, sptSet, node, v)

        print(currentNode)
        sptSet[currentNode] = True

        for neighborNode in range(0, v):
            print ("test graph " + str(i) + " : " + str(graph))
            if sptSet[neighborNode] == False \
                and graph[currentNode][neighborNode] \
                and dist[currentNode] != sys.maxsize \
                and dist[currentNode] + graph[currentNode][neighborNode] < dist[neighborNode]:
                dist[neighborNode] = dist[currentNode] + graph[currentNode][neighborNode]
                del path[neighborNode][:]
                path[neighborNode] = path[currentNode] + [neighborNode]
    print (dist)
    printMinDistance(dist, node, v)
    printPath(position, path, node, end, v)

def createGrapgh(nodeStart, nodeEnd, nodeNumber):
    position = [[1,6], [1,1], [2, 3], [3, 6], [3,1], [4, 3], [5, 6]]
    temp = [[0,1,5],[0,2,1],[2,3,7],[3,4,1],[3,5,6],[4,5,2],[5,6,3],
            [1,0,5],[2,0,1],[3,2,7],[4,3,2],[5,3,2],[5,4,6],[6,5,3]]
    graph = [[0 for col in range(nodeNumber)] for row in range(nodeNumber)]
    for i in temp:
        graph[i[0]][i[1]] = i[2]
    # for _ in graph:
    #     for i in _:
    #         print(i, end=" ")
    #     print()
    # for r in range(0, nodeNumber):
    #     for c in range(0, nodeNumber):
    #         if(graph[r][c]):
    #             print (str(r) + " va " + str(c) + " co lien ket voi khoang cach la : " + str(graph[r][c]))
    #     print()
    
    # print()
    print(graph)
    printGraph(position ,temp, nodeNumber)
    dijkstra(graph, nodeStart, nodeEnd, nodeNumber, position)

def main():
    # nodeNumber =  int(input("Nhap so dinh ban muon tao do thi : "))
    # nodeStart = int(input("Dinh xuat phat : "))
    createGrapgh(2, 5, 7)

if __name__ == "__main__":
    main()