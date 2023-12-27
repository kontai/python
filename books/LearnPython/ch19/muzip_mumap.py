def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    print(minlen)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]


def mymapPad(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]


S1, S2 = 'abc', 'xyz123'
print(myzip(S1, S2))
print(mymapPad(S1, S2))
print(mymapPad(S1, S2, pad=99))

print(S1+S2)