import sys


def index_wordds(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text, 1):
        if letter == ' ':
            result.append(index)
    return result

def index_words(text):
    if text:
        yield 0
    for index,letter in enumerate(text,1):
        if letter == ' ':
            yield index

# print(index_wordds('hello alex da sb'))

g=index_words('hello alex da sb')
print(g)
print(g.__next__())
print(g.send(1))
print(g.send(1))
print(g.send(1))
try:
    print(g.send(1))
except StopIteration :
    exit(1)


