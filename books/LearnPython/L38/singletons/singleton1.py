instances={}

def singleton(aClass):
    def onCall(*args,**kwargs):
        if aClass not in instances:
            instances[aClass]=aClass(*args,**kwargs)
        return instances[aClass]
    return onCall