import threading

lock = threading.Lock()
counter = 0

def add():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=add) for _ in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]

print(counter)