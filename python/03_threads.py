import random
import threading
import time


def worker_factory(worker_id):
    def worker():
        """thread worker function"""
        sleep_length = random.randint(10, 30) / 10
        print('Worker {} started, will do work for {}s'.format(worker_id, sleep_length))
        time.sleep(sleep_length)
        print('Worker {} completed'.format(worker_id))
        return

    return worker


def start_threads():
    threads = []
    for i in range(1, 6):
        t = threading.Thread(target=worker_factory(i))
        threads.append(t)
        t.start()


if __name__ == '__main__':
    start_threads()
