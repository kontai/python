import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print('washing', dish, 'dish')
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print("Drying", dish, 'dish')
        input.task_done()

dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()

dishs = ['salad', 'dread', 'entree', 'dessert']
washer(dishs, dish_queue)
dish_queue.join()
