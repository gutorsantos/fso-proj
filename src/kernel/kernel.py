from process.process_manager import ProcessManager
from file.file_manager import FileManager
import time

class Kernel:
    def __init__(self) -> None:
        self.process_manager = ProcessManager()
        self.file_manager = FileManager()

    def run(self) -> None:
        self.start()

        print(self.process_manager.process)
        print(self.file_manager.disk)
        print(self.file_manager.files)
        print(self.file_manager.operations)

    def start(self) -> None:
        self.process_manager.read_processes()
        self.file_manager.read_files()

