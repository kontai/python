class Test:
    def __init__(self,any):
        self.any=any
    def show(self):
        return self.any
    def __str__(self):
        return self.any
if __name__ == '__main__':
    first = Test('abc')
    second=first.__new__(Test)
    second.any='def'
    print(id(second)-id(first))
    print(id(first))