# find some number N's all prime number with O(n)
import datetime

def eratosthenes(n):
    tstart = datetime.datetime.now()
    multiples = []
    prime = []
    for i in range(2, n+1):
        if i not in multiples:
            prime.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)

    tend = datetime.datetime.now()
    time = tend - tstart
    print(time.microseconds)
    print(len(prime))
    print(prime)


############################################

#another way
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

def prime_Number(N):

    N = int(N)
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
    print(len(List))
    print(List)


eratosthenes(4000)
prime_Number(4000)

# After compare two ways, Prime_Number use less time than eratosthenes.......
