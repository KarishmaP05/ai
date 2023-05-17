dict_hn={'S':5,'A':3,'B':4,'D':6,'C':2,'G':0}

dict_gn=dict(
    S=dict(A=1,G=10),
    A=dict(S=1,B=2,C=1),
    B=dict(A=2,D=5),
    D=dict(B=5,C=3,G=2),
    C=dict(A=1,D=3,G=4),
    G=dict(S=10,C=4,D=2)


)
import queue as Q
#from RMP import dict_gn
#from RMP import dict_hn
start='S'
goal='G'
result=''

def get_fn(citystr):
    cities=citystr.split(" , ")
    hn=gn=0
    for ctr in range(0, len(cities)-1):
        gn=gn+dict_gn[cities[ctr]][cities[ctr+1]]
    hn=dict_hn[cities[len(cities)-1]]
    return(hn+gn)
    

def expand(cityq):
    global result
    tot, citystr, thiscity=cityq.get()
    if thiscity==goal:
        result=citystr+" : : "+str(tot)
        return
    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr+" , "+cty), citystr+" , "+cty, cty))
    expand(cityq)

def main():
    cityq=Q.PriorityQueue()
    thiscity=start
    cityq.put((get_fn(start),start,thiscity))
    expand(cityq)
    print("The A* path with the total is: ")
    print(result)

main()