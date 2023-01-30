from queue import Queue
import time
from threading import Thread
from process.process import Process

MAX_QUEUE_SIZE = 1000

class UserQueue:

    def __init__(self) -> None:
        self.q1 = Queue()           # SJF
        self.q2 = Queue()           # RR
        self.q3 = Queue()           # FIFO
        # self.user_queue = [Queue(maxsize=MAX_QUEUE_SIZE), Queue(maxsize=MAX_QUEUE_SIZE), Queue(maxsize=MAX_QUEUE_SIZE)] ?

    def put(self, process: Process):
        self.q1.put(process)

    def empty(self):
        return self.q1.empty()

    def get(self):
        if(not self.q1.empty()):
            return self.q1.get()
        if(not self.q2.empty()):
            return self.q2.get()
        if(not self.q3.empty()):
            return self.q3.get() 

    def qsize(self):
        return self.q1.qsize() + self.q2.qsize() + self.q3.qsize()
    