A = 't' if 'spam' else 'f'  # 等同於 'spam'?'t':'f'
print(A, '\n')

print(['1', '2', '3'][2])
B = ['f', 't'][bool('spam')]
print(B + '\n')

print([bool('spam')])
print(True + True)
