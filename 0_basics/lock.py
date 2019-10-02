import threading


# We've got a global variable
count = 0
# Here's a lock for it
a = threading.Lock()


def worker(*args):
    """thread worker function, with some funky ordered logic"""
    global count
    # We're using the lock as a context here, so it gets released
    # at the end of this block
    with args[0]:
        count += 1
        print(count)
        count += 4
        print(count)
        count -= 4
        print(count)


# Two will execute, last one will as one finishes
thread_1 = threading.Thread(target=worker, args=[a])
thread_2 = threading.Thread(target=worker, args=[a])
thread_3 = threading.Thread(target=worker, args=[a])
thread_1.start()
thread_2.start()
thread_3.start()
