from file.disk import Disk
from file.files import File
from file.operations import Operation

class FileManager:
    disk: Disk
    files: list[File] = []
    operations: list[Operation] = []
    def __init__(self) -> None:
        # self.operations = [Operation()]
        pass

    def read_files(self) -> None:
        list = []
        with open('/home/gustavo/Projetos/fso-proj/src/input/files.txt') as files_file:
            list = files_file.readlines()
            num_files = int(list[1].strip())

            disk_list = list[0:2]
            file_list = list[2:num_files+2]
            operation_list = list[num_files+2:len(list)]

            self.disk = Disk(disk_list)
            self.files = [File(f.split(',')) for f in file_list]
            self.operations = [Operation(o.split(',')) for o in operation_list]



