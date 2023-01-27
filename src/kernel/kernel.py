from process.process_manager import ProcessManager
from file.file_manager import FileManager
# from resource.resource_manager import ResourceManager
from memory.memory_manager import MemoryManager
import time
from kernel.clock import Clock

class Kernel:
    def __init__(self) -> None:
        self.process_manager = ProcessManager()
        self.file_manager = FileManager()
        self.resource_manager = ResourceManager()
        self.memory_manager = MemoryManager()
        self.clock = Clock()

    def run(self) -> None:
        self.start()
        # time.sleep(3)
        # print(self.clock.get_miliseconds())
        # self.clock.thread.join()

    def start(self) -> None:
        self.process_manager.read_processes()
        self.file_manager.read_files()
        # self.clock.thread.start()

