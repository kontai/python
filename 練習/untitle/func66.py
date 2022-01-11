def eater(name):
    print('%s 准备开始吃饭啦' %name)
    food_list=[]
    while True:
        food=yield food_list
        print('%s 吃了 %s' % (name,food))
        food_list.append(food)
g=eater('egon')
g.send(None)
g.send('蒸羊羔')
g.send('蒸鹿茸')
g.send('蒸熊掌')
g.send('烧素鸭')
g.close()
g.send('烧素鹅')
g.send('烧鹿尾')
