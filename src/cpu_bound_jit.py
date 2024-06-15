from threading import Thread, active_count
from numba import jit
import time



N = 100_000_000
THREADS_NUM_LIST = [1, 2, 4, 8]

@jit(nopython=True, nogil=True)
def countdown(n):
    res = 2
    while n > 0:
        res += n
        n -= 1


def run_in_threads(threads_num, func, *args):
    threads = [Thread(target=func, args=args) for _ in range(threads_num)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def thread_count():
    start = time.time()
    total = time.time() - start
    counts = set()
    while total < 5:
        total = time.time() - start
        counts.add(active_count())
    print(counts)
    


def measure():
    print("Main exec:")
    start = time.time()
    countdown(N)
    print(time.time() - start)
    t= Thread(target=thread_count)
    t.start()
    
    for threads_num in THREADS_NUM_LIST:
        n = N //threads_num
        print(f'{threads_num=}; {n=}')
        for _ in range(3):
            start = time.time()
            run_in_threads(threads_num, countdown, n)
            print(time.time() - start)
        print()
    t.join()


if __name__ == '__main__':
    measure()