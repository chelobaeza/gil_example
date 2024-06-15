from threading import Thread
import asyncio
from requests import get
import time


N = 18
THREADS_NUM_LIST = [1,2, 4, 8]


async def countdown(n):
    await asyncio.gather(
        *[asyncio.sleep(n) for _ in range(n)]
    )
    # while n > 0:
    #     n -= 1
    #     # time.sleep(n)
    #     await asyncio.sleep(n)


async def run_in_threads(threads_num, func, *args):
    await asyncio.gather(
        *[
            func(*args)
            for _ in range(threads_num)
        ]
    )


async def measure():
    for threads_num in THREADS_NUM_LIST:
        n = N //threads_num
        print(f'{threads_num=}; {n=}')
        for _ in range(1):
            start = time.time()
            await run_in_threads(threads_num, countdown, n)
            print(time.time() - start)
        print()


if __name__ == '__main__':
    asyncio.run(measure())