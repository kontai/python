def my_intersect(*args):
    res = []
    for x in args[0]:
        for others in args[1:]:
            if x not in others:
                break
            elif x not in res:
                res.append(x)
    return res


def my_union(*args):
    res = []
    for x in args:
        for seq in x:
            if seq not in res:
                res.extend(seq)
    return res

if __name__ == '__main__':
    s1=my_intersect("SPAM","SCAM","SLAM")
    print(s1)