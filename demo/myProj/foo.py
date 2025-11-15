x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})