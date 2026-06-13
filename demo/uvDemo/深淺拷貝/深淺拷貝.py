# 淺拷貝
import copy

a = [1, 2, 3,[4,5,6]]
b = a
b[0] = 100
print(f"a={a},b={b}")

c=copy.copy(a)
c[0]=200
print(f"a={a},b={b},c={c}")

d=copy.deepcopy(a)
d[0]=300
print(f"a={a},b={b},c={c},d={d}")

e=copy.copy(a)
e[3][0]=400
print(f"a={a},b={b},c={c},d={d},e={e}")

f=copy.deepcopy(a)
f[3][0]=500
print(f"a={a},b={b},c={c},d={d},e={e},f={f}")
