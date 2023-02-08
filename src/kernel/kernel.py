from process.process_manager import ProcessManager
from file.file_manager import FileManager
from memory.memory_manager import MemoryManager
from resources.resource_manager import ResourceManager
import time
from sys import argv
from utils.output import Output, DEBUG_MODE_ON
import operator

class Kernel:
    def __init__(self) -> None:
        if(len(argv) > 1 and argv[1] == '-d'):
            Output(True).debug(DEBUG_MODE_ON)
            

        self.file_manager = FileManager()
        self.resource_manager = ResourceManager()
        self.memory_manager = MemoryManager()
        self.process_manager = ProcessManager()

    def manual_throw(self):
        # ========================== PROCESS SCHEDULING TEST =========================================== 
        self.process_manager.insert_process_queue(self.process_manager.processes_table[2])
        self.process_manager.insert_process_queue(self.process_manager.processes_table[3])
        time.sleep(3)
        self.process_manager.insert_process_queue(self.process_manager.processes_table[0])
        self.process_manager.insert_process_queue(self.process_manager.processes_table[1])
        # ========================== END PROCESS SCHEDULING TEST =========================================== 

    def throw_process(self):
        sorted_proc = list(sorted(self.process_manager.processes_table, key=operator.attrgetter('starting_time')))
        acc = 0
        for p in sorted_proc:
            time.sleep(p.starting_time-acc)
            self.process_manager.queue_lock.acquire()
            self.process_manager.insert_process_queue(p)
            self.process_manager.queue_lock.release()
            acc = p.starting_time

    def run(self) -> None:
        try:
            self.start()
            self.throw_process()
            self.process_manager.real_time_thread.join()
            self.process_manager.user_thread.join()
            
        except KeyboardInterrupt:
            print(self.file_manager.disk)
            print(self.memory_manager.memory)
            self.file_manager.check_operations_left(self.process_manager.terminated_process)
            exit()

    def start(self) -> None:
        self.process_manager.read_processes()
        self.file_manager.read_files()

