import threading
import time

a = threading.Semaphore()
a.acquire()
# Semaphore can be acquired as many times as you set it to allow. It
# defaults to 1, so if you try to acquire twice in the same thread
# you'll wait forever.
a.release()
# You can release as many times as you want with a semaphore that's not
# bound,
a.release()

b = threading.BoundedSemaphore()
b.acquire()
# If you release a bounded semaphore more times than you acquire it, it
# will error out.
b.release()


def worker(*args):
    """thread worker function"""
    args[0].acquire()
    print('Worker Start')
    time.sleep(1)
    print('Worker End')
    args[0].release()
    return

# Two will execute, last one will as one finishes
sem = threading.Semaphore(2)
thread_1 = threading.Thread(target=worker, args=[sem])
thread_2 = threading.Thread(target=worker, args=[sem])
thread_3 = threading.Thread(target=worker, args=[sem])
thread_1.start()
thread_2.start()
thread_3.start()
