from inter2 import my_intersect, my_union


def show(func, *args):
    print(func(*args))


s1, s2, s3 = "SPAM", "SCAM", "SLAM"
show(my_intersect, s1, s2, s3)
show(my_union, s1, s2)
show(my_intersect, [1, 2, 3], (1, 4))
show(my_intersect, s1, s2, s3)
show(my_union,s1, s2, s3)


