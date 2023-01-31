from process.process_manager import ProcessManager
from file.file_manager import FileManager
from memory.memory_manager import MemoryManager
from kernel.clock import Clock
from resources.resource_manager import ResourceManager
import time

class Kernel:
    def __init__(self) -> None:
        self.file_manager = FileManager()
        self.resource_manager = ResourceManager()
        self.memory_manager = MemoryManager()
        self.process_manager = ProcessManager()
        self.clock = Clock()

    def run(self) -> None:
        self.start()
        print(self.clock.get_miliseconds())
        self.process_manager.insert_process_queue(self.process_manager.processes_table[2])
        time.sleep(7)
        self.process_manager.insert_process_queue(self.process_manager.processes_table[0])
        self.process_manager.insert_process_queue(self.process_manager.processes_table[1])
        self.process_manager.real_time_thread.join()
        self.process_manager.user_thread.join()
        # print(self.clock.get_miliseconds())
        self.clock.thread.join()

    def start(self) -> None:
        self.process_manager.read_processes()
        self.file_manager.read_files()
        self.clock.thread.start()

