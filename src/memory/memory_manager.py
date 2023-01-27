from memory.memory import Memory
from process.process import Process
from utils.singleton import Singleton

class MemoryManager(metaclass=Singleton):
    def __init__(self) -> None:
        self.MEMORY_REAl_TIME_SIZE = 64
        self.MEMORY_USER_SIZE = 960
        self.memory = Memory(self.MEMORY_REAl_TIME_SIZE, self.MEMORY_USER_SIZE)

    def alloc(self, process: Process):
        process.memory_start_block = self.memory.malloc(process.priority, process.memory_block_size)
        return process.memory_start_block
    
    def free(self, process: Process):
        self.memory.malloc(process.memory_start_block, process.memory_block_size)