# each rotation, put the last number in front of list
# input: list, rotations
# output: final List

#show all steps, print each show and step rotation number

def rotate_list(List, rotation):

    a = len(List)
    for i in range(rotation):
        print(i+1)
        i = List[len(List) - 1]
        List.pop(len(List) - 1)
        List.insert(0, i)
        print(List)


rotate_list([1,2,9,4,5,6,7,8,9],10)