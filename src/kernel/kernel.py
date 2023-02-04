from process.process_manager import ProcessManager
from file.file_manager import FileManager
from memory.memory_manager import MemoryManager
from kernel.clock import Clock
from resources.resource_manager import ResourceManager
import time
from file.operations import Operation
from sys import argv
from utils.output import Output, DEBUG_MODE_ON

class Kernel:
    def __init__(self) -> None:
        if(len(argv) > 1 and argv[1] == '-d'):
            Output(True).debug(DEBUG_MODE_ON)
            

        self.file_manager = FileManager()
        self.resource_manager = ResourceManager()
        self.memory_manager = MemoryManager()
        self.process_manager = ProcessManager()
        self.clock = Clock()

    def run(self) -> None:
        try:
            self.start()
            # ========================== FILE MANAGER TEST =========================================== 
            # op = Operation('0', '0', 'A', '2')
            # self.file_manager.execute_operation(op, self.process_manager.processes_table[0])
            # print(self.file_manager.disk)
            # op = Operation('2', '1', 'A')
            # self.file_manager.execute_operation(op, self.process_manager.processes_table[2])
            # print(self.file_manager.disk)
            # ========================== END FILE MANAGER TEST =========================================== 

            # ========================== PROCESS SCHEDULING TEST =========================================== 
            print(self.clock.get_miliseconds())
            self.process_manager.insert_process_queue(self.process_manager.processes_table[2])
            self.process_manager.insert_process_queue(self.process_manager.processes_table[3])
            time.sleep(3)
            self.process_manager.insert_process_queue(self.process_manager.processes_table[0])
            self.process_manager.insert_process_queue(self.process_manager.processes_table[1])
            self.process_manager.real_time_thread.join()
            self.process_manager.user_thread.join()
            # print(self.clock.get_miliseconds())
            self.clock.thread.join()
            
        except KeyboardInterrupt:
            print('teste')
            exit()
        # ========================== END PROCESS SCHEDULING TEST =========================================== 

    def start(self) -> None:
        self.process_manager.read_processes()
        self.file_manager.read_files()
        self.clock.thread.start()

