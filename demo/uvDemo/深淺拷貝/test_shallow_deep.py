import copy



def shallow_copy(l):
    # l = [1, 2, [3, 4]]
    list2 = l.copy()
    list2[0] = 100
    list2[2][0] = 200
    print("shallow copy")
    print(f"list1={l}\nlist2={list2}")


def deep_copy(l):
    # l = [1, 2, [3, 4]]
    list2 = copy.deepcopy(l)
    list2[0] = 100
    list2[2][0] = 200
    print("deep copy")
    print(f"list1={l}\nlist2={list2}")


l1 = [1, 2, [3, 4]]
# 更改終端顏色
print(f"original list={l1}")
shallow_copy(l1)

l2 = [1, 2, [3, 4]]
deep_copy(l2)
