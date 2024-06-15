from threading import Thread
import asyncio
from requests import get
import time


N = 1_0
THREADS_NUM_LIST = [1, 2, 4, 8]


def countdown(n):
    while n > 0:
        n -= 1
        time.sleep(n)


def run_in_threads(threads_num, func, *args):
    threads = [Thread(target=func, args=args) for _ in range(threads_num)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def measure():
    for threads_num in THREADS_NUM_LIST:
        n = N //threads_num
        print(f'{threads_num=}; {n=}')
        for _ in range(3):
            start = time.time()
            run_in_threads(threads_num, countdown, n)
            print(time.time() - start)
        print()


if __name__ == '__main__':
    measure()