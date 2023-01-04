from queue import Queue

MAX_QUEUE_SIZE = 1000

class Queue:

    def __init__(self) -> None:
        self.real_time_queue = Queue(maxsize=MAX_QUEUE_SIZE)
        # self.user_queue = [Queue(maxsize=MAX_QUEUE_SIZE), Queue(maxsize=MAX_QUEUE_SIZE), Queue(maxsize=MAX_QUEUE_SIZE)] ?

