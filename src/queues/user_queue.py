from queue import Queue
import time
from threading import Thread
from process.process import Process

MAX_QUEUE_SIZE = 1000

class UserQueue:

    def __init__(self) -> None:
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

        if(process.priority and interrupt):
            last_queue.put(process)
            return 
        
        if(last_queue == self.q1):
            self.q2.put(process)
        elif(last_queue == self.q2):
            self.q3.put(process)
        elif(last_queue == self.q3):
            self.q3.put(process)
        else:
            return
        
    def aging(self):
        for proc in self.q1.queue:
            proc.priority -= 1

        for proc in self.q2.queue:
            proc.priority -= 1

        for proc in self.q3.queue:
            proc.priority -= 1
        
        self.up()

    def up(self):
        for process in self.q2.queue:
            if(process.priority <= self.Q1_MAX_PRIORITY):
                print(f'processo {process.pid} subiu para fila 1')
                self.q1.put(process)
        for process in self.q3.queue:
            if(process.priority > self.Q1_MAX_PRIORITY and process.priority <= self.Q2_MAX_PRIORITY):
                print(f'processo {process.pid} subiu para fila 2')
                self.q2.put(process)
