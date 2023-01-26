from utils.ascii_table import make_table

class Memory:
    def __init__(self, real_time_size, user_size) -> None:
        self.real_time_size = real_time_size
        self.user_size = user_size
        self.size = self.real_time_size + self.user_size
        self.bit_map = ['0']*self.size

    def __repr__(self):
        return make_table(self.bit_map)

    def __can_alloc(self, priority, block_size):
        init_addr = 0 if not priority else self.real_time_size
        max_addr = self.real_time_size if not priority else self.size

        if(block_size > max_addr):
            return -1

        for index in range(init_addr, max_addr):
            if(self.bit_map[index] == '0'):
                space = self.bit_map[index:block_size]
                if('1' not in space):
                    return index

        return -1    
    
    def malloc(self, priority, block_size):
        start_addr = self.__can_alloc(priority, block_size)
        for i in range(start_addr, block_size):
            self.bit_map[i] = '1'

    def free(self, start_addr, block_size):
        for i in range(start_addr, block_size):
            self.bit_map[i] = '0'
