from utils.ascii_table import make_table
from utils.singleton import Singleton
from utils.output import *

class Memory(metaclass=Singleton):
    def __init__(self, real_time_size, user_size) -> None:
        self.real_time_size = real_time_size
        self.user_size = user_size
        self.size = self.real_time_size + self.user_size
        self.bit_map = ['0']*self.size
        self.out = Output()

    def __repr__(self):
        return make_table(self.bit_map) 

    # def __get_free_blocks(self, priority):
    #     pivot = 0 if not priority else self.real_time_size
    #     max_len = self.real_time_size if not priority else self.size
    #     free_block_sizes = []
    #     while pivot < max_len:
    #         if self.bit_map[pivot] == '1':
    #             pivot += 1
    #             continue
    #         start = pivot
    #         while pivot < max_len and self.bit_map[pivot] == '0':
    #             pivot += 1
    #         end = pivot - 1
    #         free_block_sizes.append([start, end - start + 1])
    #         pivot += 1
    #     return free_block_sizes

    
    # def __best_fit(self, priority, mem_block_size):
    #     free_block = self.__get_free_blocks(priority)
    #     free_block = list(filter(lambda x: x[1] >= mem_block_size, free_block))
    #     free_block = list(map(lambda x: (x[0], x[1]-mem_block_size), free_block))

    #     if (not len(free_block)):
    #         return -1

    #     start_addr, _ = min(free_block, key=lambda x: x[1])

    #     return start_addr
    
    def __can_alloc(self, priority, size):
        if(priority > 0):
            if(size <= self.user_size):
                return 0 
            return -1
        
        if(size <= self.real_time_size):
            return 0
        return -1

    def malloc(self, priority, mem_block_size, pid):
        start_addr = self.__can_alloc(priority, mem_block_size)

        if(start_addr == -1):
            self.out.error(NOT_ENOGH_MEMO, pid=pid)
            return start_addr

        for i in range(start_addr, start_addr+mem_block_size):
            self.bit_map[i] = '1'

        # self.out.debug(self)
        return start_addr

    def free(self, start_addr, block_size):
        for i in range(start_addr, start_addr+block_size):
            self.bit_map[i] = '0'
