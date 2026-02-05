def singleton(aClass):                                   # On @ decoration
    instance = None
    def onCall(*args, **kwargs):                         # On instance creation
        nonlocal instance
        if instance == None:
            instance = aClass(*args, **kwargs)           # One scope per class
        return instance
    return onCall