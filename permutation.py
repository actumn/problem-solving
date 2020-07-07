from itertools import permutations

pool = ['A', 'B', 'C']

for a in permutations(pool):
    print(''.join(a))
    
print(list(map(''.join, permutations(pool))))
