from queue import Queue
from queues.user_queue import UserQueue
import time
from threading import Thread

MAX_QUEUE_SIZE = 1000

class ProcessesQueue:

    def __init__(self) -> None:
        self.real_time_queue = Queue(maxsize=MAX_QUEUE_SIZE)
        self.user_queue = UserQueue()

    def empty(self):
        return self.real_time_queue.empty()
    
    def get_size(self):
        self.real_time_queue.qsize() + self.user_queue.qsize()
    