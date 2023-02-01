from process.process import Process
from utils.dir import ROOT_DIR
from queues.processes_queue import ProcessesQueue
from memory.memory_manager import MemoryManager
from threading import Thread, Lock
import time
from queue import Queue
from typing import Union

class ProcessManager:
    def __init__(self) -> None:
        self.processes_table: list[Process] = []
        self.queue = ProcessesQueue()
        self.memory_manager = MemoryManager()
        self.current_proc = (None, None)
        self.real_time_thread = Thread(target=self.real_time_queue_thread)
        self.user_thread = Thread(target=self.user_queue_thread)
        self.queue_lock = Lock()
        self.flag_rt_interrupt = False
        self.__wait_for_process()

    def read_processes(self) -> None:
        list = []
        with open(ROOT_DIR+'input/processes.txt') as processes_file:
            list = processes_file.readlines()

        self.processes_table = [Process(p.split(','), id) for (id, p) in enumerate(list)]

    def insert_process_queue(self, process: Process):
        # if(not process or process.process_time <= 0 or self.queue.get_size() > 1000):
        #     return

        if (process.priority):
            self.queue.user_queue.put(process)
        else:
            self.queue.real_time_queue.put(process)

    def __context_switching(self, process):
        """ Realizes the context switching between two processes

        Args:
            process (Process): process that will be executed (allocated in memory)

        Returns:
            Process: the last current process
        """
        last_proc, last_queue = self.current_proc
        if(last_proc):
            self.memory_manager.free(last_proc)
        if(process[0]):
            self.memory_manager.alloc(process[0])
        self.current_proc = process
        return last_proc, last_queue
    
    def __wait_for_process(self):
        self.real_time_thread.start()
        self.user_thread.start()
                
    def real_time_running(self):
        process, _ = self.current_proc
        while process.process_time > 0:
            print('executando processo rt', process.pid)
            process.process_time -= 1
            time.sleep(1)

    def user_running(self):
        process, queue = self.current_proc
        remaining_quantum = self.queue.user_queue.get_queue_quantum(queue)
        self.flag_rt_interrupt = False
        while remaining_quantum > 0 and process.process_time > 0:
            if(not self.queue.real_time_queue.empty()):
                self.flag_rt_interrupt = True
                # return nao pode ser preemptado no meio do quantum
            print('executando processo user', process.pid)
            remaining_quantum -= 1
            process.process_time -= 1
            # self.queue.user_queue.aging()
            time.sleep(1)
        p = self.__context_switching((None, None))
        self.queue.user_queue.down(*p, self.flag_rt_interrupt)


    def real_time_queue_thread(self):
        """ Thread function that will be waiting for the arriving real-time processes """        
        while(True):
            print('esperando por processo rt...')
            if(not self.queue.real_time_queue.empty()):
                self.queue_lock.acquire()
                first = (self.queue.real_time_queue.get(), self.queue.real_time_queue)
                last = self.__context_switching(first)
                self.queue.user_queue.down(*last, self.flag_rt_interrupt)
                self.real_time_running()
                self.queue_lock.release()
            time.sleep(1)

    def user_queue_thread(self):
        """ Thread function that will be waiting for the arriving user processes """      
        while(True):
            print('esperando por processo usuario...')
            if(not self.queue.user_queue.empty()):
                self.queue_lock.acquire()
                if(not self.queue.real_time_queue.empty()):
                    self.queue_lock.release()
                else:
                    first = self.queue.user_queue.get()
                    last = self.__context_switching(first)
                    self.queue.user_queue.down(*last, self.flag_rt_interrupt)
                    self.user_running()
                    self.queue_lock.release()
            time.sleep(1)