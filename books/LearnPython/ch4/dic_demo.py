#!/usr/bin/env python

D = {'b': 2, 'c': 3, 'd': 4, 'a': 1, 'e': 5}

k = list(D.keys())
k.sort()
print(k)
for i in k:
    print(i, D[i])
print('\n')
for key in sorted(D):
    print(key, D[key])

value = D.get('j', 'not exist')  # get key and avoid error message
print(value)
