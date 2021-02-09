from itertools import permutations
import cProfile

my_list = [1, 2, 3]
list_of_permutations = permutations(my_list)

counter = 0
for permutation in list_of_permutations:
    print(permutation)
    counter += 1
print(counter,"permutations")

def factorial(n):
    if n <= 1:
        return n
    else:
        return factorial(n-1)*n

def counter(n):
    cnt=0
    for i in range(n):
        cnt += 1
    return cnt

cProfile.run("counter(factorial(11))")