from file.disk import Disk
from file.files import File
from file.operations import Operation
from utils.dir import ROOT_DIR
from process.process import Process
from utils.singleton import Singleton
from utils.output import *

class FileManager(metaclass=Singleton):
    def __init__(self) -> None:
        self.disk: Disk
        self.files: list[File] = []
        self.operations: list = []
        self.out = Output()

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
            self.__init_disk()

    def __init_disk(self):
        for file in self.files:
            self.disk.fill(file.first_block, file.block_size, file.name)

    def allocate(self, filename: str, file_size: int, pid: int):
        start_addr = self.disk.alloc(file_size, filename)

        if(start_addr < 0):
            self.out.error(NOT_ENOGH_SPACE, pid=pid, filename=filename)
            
        return start_addr

    def execute_operation(self, operation: Operation, process: Process):
        self.operations.remove(operation)
        if(operation.operation_id):
            file = list(filter(lambda f: f.name == operation.file_name, self.files))
            
            if(len(file) <= 0):
                self.out.error(INEXISTENT_REMOVE_FILE, pid=process.pid, filename=operation.file_name)
                return
            
            file = file[0]

            if(process.pid != file.created_by and process.pid != 0):
                self.out.error(NO_PERMISSION_REMOVE_FILE, pid=process.pid, filename=operation.file_name)
                return
            
            self.disk.free(file.first_block, file.block_size)
            self.out.sucess(SUCESSFUL_REMOVE_FILE, pid=process.pid, filename=operation.file_name)
        else:
            start_addr = self.allocate(operation.file_name, operation.created_block_size, process.pid)
        
            if(start_addr == -1):
                return

            new_file: File = File(operation.file_name, str(start_addr), str(operation.created_block_size), process.pid)
            self.files.append(new_file)
            block_range = list(range(start_addr, start_addr+operation.created_block_size))
            block_range = list(map(lambda x: str(x), block_range))
            self.out.sucess(SUCESSFUL_CREATE_FILE, pid=process.pid, filename=operation.file_name, block_range=block_range)

    def get_operations(self, pid: int):
        return list(filter(lambda o: o.process_id == pid, self.operations))

