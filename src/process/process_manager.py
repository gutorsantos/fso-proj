from process.process import Process
from utils.dir import ROOT_DIR
from queues.processes_queue import ProcessesQueue
from memory.memory_manager import MemoryManager
from threading import Thread
import time

class ProcessManager:
    def __init__(self) -> None:
        self.processes_table: list[Process] = []
        self.queue = ProcessesQueue()
        self.memory_manager = MemoryManager()
        self.current_proc: Process = None
        self.thread = Thread(target=self.__wait_for_process)
        self.thread.start()

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
        '''
        Enquanto houver processo na fila:
            0. pega o primeiro processo da fila
            1. desaloca o processo que estiver em memoria
            2. aloca o novo processo na memoria
            3. insere o processo antigo numa nova fila ou na mesma fila
        '''
        last_proc = self.current_proc
        if(last_proc):
            self.memory_manager.free(last_proc)
        self.memory_manager.alloc(process)
        self.current_proc = process
        return last_proc
    
    def __wait_for_process(self):
        while(True):
            print('esperando por processo...')
            if(not self.queue.real_time_queue.empty()):
                first = self.queue.real_time_queue.get()
                print('executando processo ', first.pid)
                self.__context_switching(first)
                time.sleep(5)
            else:
                # if(not self.user.empty()):
                #     print('executando processo ', self.real_time_queue.get().pid)
                #     time.sleep(5)
                pass

            time.sleep(1)