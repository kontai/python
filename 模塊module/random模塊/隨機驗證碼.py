import random

def v_code():
    ret=""
    for i in range(6):
        num=random.randint(0,9)
        alt=chr(random.randint(65,122))
        while not alt.isalpha():
            alt=chr(random.randint(65,122))
        tmp=str(random.choice([num,alt]))
        ret+=tmp
    return ret

print(v_code())

