from utils.ascii_table import make_table

class Disk:
    def __init__(self, size) -> None:
        self.size = int(size.strip())
        self.bit_map = ['0']*self.size

    def __repr__(self):
        return make_table(self.bit_map) 
    
    def __str__(self):
        return self.__repr__()
    

    def __first_fit(self, block_size):
        if(block_size > self.size):
            return -1

        for index in range(self.size):
            if(self.bit_map[index] == '0'):
                space = self.bit_map[index:index+block_size]
                if(space.count('0') == block_size):
                    return index

        return -1    

    def alloc(self, block_size, filename):
        start_addr = self.__first_fit(block_size)

        if(start_addr < 0):
            return -1

        for i in range(start_addr, start_addr+block_size):
            self.bit_map[i] = filename
            
        return start_addr

    def fill(self, start_addr, block_size, filename):
        for i in range(start_addr, start_addr+block_size):
            self.bit_map[i] = filename

    def free(self, start_addr, block_size):
        for i in range(start_addr, start_addr+block_size):
            self.bit_map[i] = '0'