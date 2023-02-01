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

    def get_queue_quantum(self, queue):
        if(queue == self.q1):
            return 5
        if(queue == self.q2):
            return 10
        return 15


    def put(self, process: Process):
        self.q1.put(process)

    def empty(self):
        return self.q1.empty() and self.q2.empty() and self.q3.empty()

    def get(self):
        if(not self.q1.empty()):
            return (self.q1.get(), self.q1)
        if(not self.q2.empty()):
            return (self.q2.get(), self.q2)
        if(not self.q3.empty()):
            return (self.q3.get(), self.q3)

    def qsize(self):
        return self.q1.qsize() + self.q2.qsize() + self.q3.qsize()
    
    def down(self, process, last_queue, interrupt):
        if(not process):
            return

        if(process.priority and interrupt):
            last_queue.queue.insert(0, process)
            return 
        
        if(last_queue == self.q1):
            self.q2.put(process)
        elif(last_queue == self.q2):
            self.q3.put(process)
        elif(last_queue == self.q3):
            self.q3.put(process)
        else:
            return