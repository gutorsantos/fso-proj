from process.process import Process
from utils.dir import ROOT_DIR
from queues.processes_queue import ProcessesQueue

class ProcessManager:
    def __init__(self) -> None:
        self.processes_table: list[Process] = []
        self.queue = ProcessesQueue()
        pass

    def read_processes(self) -> None:
        list = []
        with open(ROOT_DIR+'input/processes.txt') as processes_file:
            list = processes_file.readlines()

        self.processes_table = [Process(p.split(','), id) for (id, p) in enumerate(list)]

        # self.insert_process_queue(self.processes_table[0], 'rt')

    def insert_process_real_time_queue(self, process):
        self.queue.real_time_queue.put(process)

    def insert_process_user_queue(self, process):
        pass #     self.queue.real_time_queue.put(process)

    def insert_process_queue(self, process, type):
        if (type == 'rt'):
            self.insert_process_real_time_queue(process)
        else:
            self.insert_process_user_queue(process)