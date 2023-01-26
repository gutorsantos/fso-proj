from memory.memory import Memory

class MemoryManager:
    def __init__(self) -> None:
        self.MEMORY_REAl_TIME_SIZE = 64
        self.MEMORY_USER_SIZE = 960
        self.memory = Memory(self.MEMORY_REAl_TIME_SIZE, self.MEMORY_USER_SIZE)