items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    if key in items:
        print(key, "was found")
    else:
        print(key, "not found!")
