import sys
sys.setrecursionlimit(200)
k=0
def wish():
    global k
    k=k+1
    print("vannakamda mapla",k)
    wish()
wish()