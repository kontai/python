class singleton:
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.aClass(*args, **kwargs)
        return self.instance
