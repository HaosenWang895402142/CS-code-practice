# find some number N's all prime number with O(n)

import datetime

def Create_List(N):

    List = []
    for i in range(2,N+1):
        List.append(i)

    return List

def Find_multiple(A,N,List):

    multiple_List = []
    for i in List:
        if (i > A) and (i % A ==0):
            multiple_List.append(i)

    return multiple_List

def Remove_Element(List,multiple_List):

    for i in multiple_List:
        if (i in List):
            List.remove(i)
    return List

def main():

    N = eval(input("enter a integer: "))
    tstart = datetime.datetime.now()
    List = Create_List(N)
    for A in List:
        multiple_List = Find_multiple(A,N,List)
        List=Remove_Element(List,multiple_List)
        #print(List)
        #print(multiple_List)

    tend = datetime.datetime.now()
    time = tend - tstart
    print(time.microseconds)
    print(List)
    print(len(List))

main()

