from process.process import Process
from utils.dir import ROOT_DIR
from queues.processes_queue import ProcessesQueue
from memory.memory_manager import MemoryManager
from resources.resource_manager import ResourceManager
from threading import Thread, Lock
import time
from queue import Queue
from typing import Union

class ProcessManager:
    def __init__(self) -> None:
        self.processes_table: list[Process] = []
        self.queue = ProcessesQueue()
        self.memory_manager = MemoryManager()
        self.resource_manager = ResourceManager()
        self.current_proc = (None, None)
        self.real_time_thread = Thread(target=self.real_time_queue_thread)
        self.user_thread = Thread(target=self.user_queue_thread)
        self.queue_lock = Lock()
        self.blocked_processes = []
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
            result = self.memory_manager.alloc(process[0])
            if(result < 0):
                return -1
        self.current_proc = process
        return 1
    
    def __wait_for_process(self):
        self.real_time_thread.start()
        self.user_thread.start()
                
    def unblock_processes(self):
        for blocked in self.blocked_processes:
            result = self.resource_manager.request(blocked)
            if(result > 0):
                self.blocked_processes.remove(blocked)
                self.queue.user_queue.put(blocked)
                break
        
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

            print('executando processo user', process.pid)
            remaining_quantum -= 1
            process.process_time -= 1
            time.sleep(1)

        if(process.process_time <= 0):
            print('desalocou recursos')
            self.resource_manager.deallocate(process)
            self.unblock_processes()   
        else:
            self.queue.user_queue.down(*self.current_proc, self.flag_rt_interrupt)


    def real_time_queue_thread(self):
        """ Thread function that will be waiting for the arriving real-time processes """        
        while(True):
            print('esperando por processo rt...')
            if(not self.queue.real_time_queue.empty()):
                self.queue_lock.acquire()
                first = (self.queue.real_time_queue.get(), self.queue.real_time_queue)
                result = self.__context_switching(first)
                if(result > 0):
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
                    resources = self.resource_manager.request(first[0])
                    if(resources):
                        result = self.__context_switching(first)
                        if(result > 0):
                            self.user_running()
                        # self.queue.user_queue.aging()
                        # print(self.queue.user_queue.q2.queue)
                    elif(not resources):
                        print('bloqueou')
                        self.blocked_processes.append(first[0])

                    self.queue_lock.release()
            time.sleep(1)