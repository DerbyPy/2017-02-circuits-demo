import threading


def worker_factory(worker_id):
    def worker():
        """thread worker function"""
        print('Worker {} started'.format(worker_id))
        x = 1
        while x < 30000000:
            x += 1
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
