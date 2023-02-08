from memory.memory import Memory
from process.process import Process
from utils.singleton import Singleton

class MemoryManager(metaclass=Singleton):
    def __init__(self) -> None:
        self.MEMORY_REAl_TIME_SIZE = 64
        self.MEMORY_USER_SIZE = 960
        self.memory = Memory(self.MEMORY_REAl_TIME_SIZE, self.MEMORY_USER_SIZE)
        self.allocated_process = []

    def alloc(self, process: Process):
        if(process.pid in self.allocated_process):
            return process.memory_start_block

        process.memory_start_block = self.memory.malloc(process.priority, process.memory_block_size, process.pid)
        if(process.memory_start_block >= 0):
            self.allocated_process.append(process.pid)
        return process.memory_start_block
    
    def free(self, process: Process):
        self.memory.free(process.memory_start_block, process.memory_block_size)
        self.allocated_process.remove(process.pid)