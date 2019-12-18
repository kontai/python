class Color:
    def __init__(self, color="gray"):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter  # 類屬性可增加判別參數功能
    def color(self, color):
        print("color=" + self._color)
        if color == "red":
            print("hot")
        elif color == "blue":
            print("sky")
        else:
            print("rare color....")

    def get_color(self):
        print(self._color)


if __name__ == "__main__":
    cr = Color("green")
    cr.color = "red"  # 通過類屬性,隱藏類實例,5並可直接賦值

    print(cr.color)
