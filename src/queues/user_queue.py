from queue import Queue
import time
from threading import Thread
from process.process import Process
from utils.output import *

MAX_QUEUE_SIZE = 1000

class UserQueue:

    def __init__(self) -> None:
        self.out = Output()
        self.q1 = Queue()                       # RR 1-5
        self.q2 = Queue()                       # RR 6-9
        self.q3 = Queue()                       # RR >= 10
        self.Q1_MAX_PRIORITY = 5        
        self.Q2_MAX_PRIORITY = 6        
        self.Q3_MAX_PRIORITY = 10
        self.Q1_QUANTUM = 5        
        self.Q2_QUANTUM = 10        
        self.Q3_QUANTUM = 15
                

    def get_queue_quantum(self, queue):
        if(queue == self.q1):
            return self.Q1_QUANTUM
        if(queue == self.q2):
            return self.Q2_QUANTUM
        return self.Q3_QUANTUM

    def put(self, process: Process):
        if(process.priority <= self.Q1_MAX_PRIORITY):
            self.q1.put(process)
        elif(process.priority > self.Q1_MAX_PRIORITY and process.priority <= self.Q2_MAX_PRIORITY):
            self.q2.put(process)
        else:
            self.q3.put(process)

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

        if(interrupt):
            last_queue.put(process)
            return 
        
        if(last_queue == self.q1):
            self.q2.put(process)
            self.out.debug(DOWN_PROCESS, pid=process.pid, queue=2)
        elif(last_queue == self.q2):
            self.q3.put(process)
            self.out.debug(DOWN_PROCESS, pid=process.pid, queue=3)
        elif(last_queue == self.q3):
            self.q3.put(process)
        # else:
        #     return
        
    def aging(self):
        for proc in self.q1.queue:
            proc.priority = max(1, proc.priority-1)

        for proc in self.q2.queue:
            proc.priority = max(1, proc.priority-1)

        for proc in self.q3.queue:
            proc.priority = max(1, proc.priority-1)
        
        # self.up()

    def up(self):
        q2 = self.q2.queue.copy()
        q3 = self.q3.queue.copy()
        for process in self.q2.queue:
            if(process.priority <= self.Q1_MAX_PRIORITY):
                self.q1.put(process)
                q2.remove(process)
                self.out.debug(UP_PROCESS, pid=process.pid, queue=1)

        for process in self.q3.queue:
            if(process.priority > self.Q1_MAX_PRIORITY and process.priority <= self.Q2_MAX_PRIORITY):
                self.q2.put(process)
                q3.remove(process)
                self.out.debug(UP_PROCESS, pid=process.pid, queue=2)

        self.q2.queue = q2.copy()
        self.q3.queue = q3.copy()
        
