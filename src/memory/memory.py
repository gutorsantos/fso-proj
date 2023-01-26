from utils.ascii_table import make_table

class Memory:
    def __init__(self, size) -> None:
        self.size = size
        self.bit_map = ['0']*self.size

    def __repr__(self):
        return make_table(self.bit_map)