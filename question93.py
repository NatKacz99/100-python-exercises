from itertools import permutations

def permuation_generator(iterable):
    p = permutations(iterable)
    for i in p:
        print(i)


lst = [1,2,3]
permuation_generator(lst)