li = [1, 2, 3]

while True:
    l=input("index=")
    if l=='q':
        break
    position=int(l)

    try:
        print(li[position])
    except IndexError as ie:
        print("Bad Index:", ie)
    except Exception as e:
        print("other exception:", e)
