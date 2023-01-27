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

    def insert_process_queue(self, process: Process):
        if (process.priority):
            self.queue.user_queue.put(process)
        else:
            self.queue.real_time_queue.put(process)