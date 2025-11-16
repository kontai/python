#    有红、黄、蓝三种颜色的球，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。
max = 8
count = 0

for i in range(4):
    R = i
    for j in range(4):
        Y = j
        G = (max - i - j)
        if (G <= 6):
            count += 1
            print("Ball%2d:" % count, R, Y, G)
