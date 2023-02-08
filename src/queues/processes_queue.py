from queue import Queue
from queues.user_queue import UserQueue
import time
from threading import Thread

class ProcessesQueue:

    def __init__(self) -> None:
        self.real_time_queue = Queue()
        self.user_queue = UserQueue()
        self.MAX_QUEUE_SIZE = 1000

    def get_size(self):
        return self.real_time_queue.qsize() + self.user_queue.qsize()