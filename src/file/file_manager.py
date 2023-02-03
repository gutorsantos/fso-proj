from file.disk import Disk
from file.files import File
from file.operations import CreateOperation, DeleteOperation, Operation
from utils.dir import ROOT_DIR
from process.process import Process
from utils.singleton import Singleton

class FileManager(metaclass=Singleton):
    def __init__(self) -> None:
        self.disk: Disk
        self.files: list[File] = []
        self.operations: list = []

    def read_files(self) -> None:
        list = []
        with open(ROOT_DIR+'input/files.txt') as files_file:
            list = files_file.readlines()
            num_files = int(list[1].strip())

            disk_size = list[0].strip()
            file_list = list[2:num_files+2]
            operation_list = list[num_files+2:len(list)]

            self.disk = Disk(disk_size)
            self.files = [File(*f.split(',')) for f in file_list]
            self.operations = [Operation(*o.split(',')) for o in operation_list]
            # print(self.operations)
            # self.operations = [CreateOperation(*o.split(',')) if o.split(',') == '0' else DeleteOperation(*o.split(',')) for o in operation_list]
            self.__init_disk()

    def __init_disk(self):
        for file in self.files:
            self.disk.fill(file.first_block, file.block_size, file.name)

    def allocate(self, filename: str, file_size: int, pid: int):
        start_addr = self.disk.alloc(file_size, filename)
        if(start_addr < 0):
            print(f'O processo {pid} não pode criar o arquivo {filename} (falta de espaço).')

        return start_addr

    def execute_operation(self, operation: Operation, process: Process):
        self.operations.remove(operation)
        if(operation.operation_id):
            file = list(filter(lambda f: f.name == operation.file_name, self.files))
            if(len(file) <= 0):
                print(f'O processo {process.pid} não pode deletar o arquivo {operation.file_name} porque ele não existe.')
                return
            file = file[0]

            if(process.pid != file.created_by and process.pid != 0):
                print(f'O processo {process.pid} não pode deletar o arquivo {operation.file_name} (sem permissão).')
                return
            self.disk.free(file.first_block, file.block_size)
            print(f'O processo {process.pid} deletou o arquivo {operation.file_name}.')
        else:
            start_addr = self.allocate(operation.file_name, operation.created_block_size, process.pid)
        
            if(start_addr == -1):
                return

            new_file: File = File(operation.file_name, str(start_addr), str(operation.created_block_size), process.pid)
            self.files.append(new_file)
            block_range = list(range(start_addr, start_addr+operation.created_block_size))
            block_range = list(map(lambda x: str(x), block_range))
            print(f'O processo {process.pid} criou o arquivo {operation.file_name} (blocos {" ".join(block_range)}).')

    def get_operations(self, pid: int):
        return list(filter(lambda o: o.process_id == pid, self.operations))

