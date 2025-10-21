with open('data.txt', 'r') as f:
    I = iter(lambda: f.read(5), '')
    for block in I: print(block, end=' ')
