from process.process_manager import ProcessManager
from file.file_manager import FileManager
import time

class Kernel:
    def __init__(self) -> None:
        self.process_manager = ProcessManager()
        self.file_manager = FileManager()

    def run(self) -> None:
        self.start()

        print(self.process_manager.processes_table)
        print(self.file_manager.disk)
        print(self.file_manager.files)
        print(self.file_manager.operations)

        # Simular clock?
        # https://stackoverflow.com/questions/28008549/limit-while-loop-to-run-at-30-fps-using-a-delta-variable-c
        # miliseconds = 0
        # now = time.time() * 1000
        # last_frame = time.time() * 1000
        # while True:
        #     now = (time.time() * 1000)
        #     delta = now - last_frame
        #     last_frame = now

        #     # if(delta < 1):
        #     #     time.sleep(1)
        #     miliseconds += delta
        #     print(miliseconds)

    def start(self) -> None:
        self.process_manager.read_processes()
        self.file_manager.read_files()

