#   嵌套作用域中的变量在嵌套的函数被调用时才进行査找 , 所以它们实际上记住的是同样的值
#   (在最后一次循环迭代中循环变量的值 ) 。
#   也就是说 , 我们将从列表中的每个函数得到4的平方的函数 ,因为 i 对 f 在每一个列表中的函
#   数都是相同的值4 。

def makeActionsI():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)

    return acts


acts = makeActionsI()
print(acts[0])
print(acts[0](2))
print(acts[2](2))
print(acts[4](2))


# 这是在嵌套作用域的值和默认参数方面遗留的一种仍需要解释清楚的情况 , 而不是引用
#  所在的嵌套作用域的值。也就是说,为了让这类代码能够工作,必须使用默认参数把当
#  前的值传递给嵌套作用域的变量。因为默认参数是在嵌套函数创建时评估的(而不是在其稍候調用時）,
#  毎一个函数记住了自己的变量i的値


def makeActionsII():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)  # ******************
    return acts


acts2 = makeActionsII()
print(acts2[0])
print(acts2[0](2))
print(acts2[2](2))
print(acts2[4](2))
