from process.process import Process
from utils.dir import ROOT_DIR
from queues.processes_queue import ProcessesQueue
from memory.memory_manager import MemoryManager
from threading import Thread, Lock
import time

class ProcessManager:
    def __init__(self) -> None:
        self.processes_table: list[Process] = []
        self.queue = ProcessesQueue()
        self.memory_manager = MemoryManager()
        self.current_proc: Process = None
        self.real_time_thread = Thread(target=self.real_time_queue_thread)
        self.user_thread = Thread(target=self.user_queue_thread)
        self.queue_lock = Lock()
        self.__wait_for_process()

    def read_processes(self) -> None:
        list = []
        with open(ROOT_DIR+'input/processes.txt') as processes_file:
            list = processes_file.readlines()

        self.processes_table = [Process(p.split(','), id) for (id, p) in enumerate(list)]

    def insert_process_queue(self, process: Process):
        if (process.priority):
            self.queue.user_queue.put(process)
        else:
            self.queue.real_time_queue.put(process)

    def __context_switching(self, process: Process) -> Process:
        """ Realizes the context switching between two processes

        Args:
            process (Process): process that will be executed (allocated in memory)

        Returns:
            Process: the last current process
        """
        last_proc = self.current_proc
        if(last_proc):
            self.memory_manager.free(last_proc)
        self.memory_manager.alloc(process)
        self.current_proc = process
        return last_proc
    
    def __wait_for_process(self):
        self.real_time_thread.start()
        self.user_thread.start()
        # while(True):
        #     print('esperando por processo...')
        #     if(not self.queue.real_time_queue.empty()):
        #         first = self.queue.real_time_queue.get()
        #         print('executando processo ', first.pid)
        #         self.__context_switching(first)
        #         time.sleep(5)
        #     else:
        #         # if(not self.user.empty()):
        #         #     print('executando processo ', self.real_time_queue.get().pid)
        #         #     time.sleep(5)
        #         pass

        #     time.sleep(1)

    def down(self, process: Process):
        if(process.process_time <= 0):
            return
                
    def real_time_running(self):
        process = self.current_proc
        while process.process_time > 0:
            print('executando processo rt', process.pid)
            process.process_time -= 1
        pass

    def real_time_queue_thread(self):
        """ Thread function that will be waiting for the arriving real-time processes """        
        while(True):
            print('esperando por processo rt...')
            if(not self.queue.real_time_queue.empty()):
                self.queue_lock.acquire()
                first: Process = self.queue.real_time_queue.get()
                last = self.__context_switching(first)
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
                    first: Process = self.queue.user_queue.get()
                    last = self.__context_switching(first)
                    print('saiu processo', last)
                    print('executando processo user', first.pid)
                    time.sleep(5)
                    self.queue_lock.release()
            time.sleep(1)