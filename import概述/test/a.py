#  Copyright (c) 2019.
#  file name=$filename
#
import b

X=1

if __name__ == '__main__':
    import a
    print(a.X,a.b.Y,a.b.c.Z)

    from imp import reload
    print(reload(a))
    print(a.X,a.b.Y,a.b.c.Z)

    from import概述.遞歸導入所有模塊.reloadall import reload_all
    print(reload_all(a))
    print(a.X,a.b.Y,a.b.c.Z)
