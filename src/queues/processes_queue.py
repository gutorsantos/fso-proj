from queue import Queue
import time
from threading import Thread

MAX_QUEUE_SIZE = 1000

class ProcessesQueue:

    def __init__(self) -> None:
        self.real_time_queue = Queue(maxsize=MAX_QUEUE_SIZE)
        # self.user_queue = [Queue(maxsize=MAX_QUEUE_SIZE), Queue(maxsize=MAX_QUEUE_SIZE), Queue(maxsize=MAX_QUEUE_SIZE)] ?

    def empty(self):
        return self.real_time_queue.empty()
    