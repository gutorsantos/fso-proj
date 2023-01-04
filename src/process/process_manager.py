from process.process import Process

class ProcessManager:
    process_queue = []
    def __init__(self) -> None:
        pass

    def read_processes(self) -> None:
        list = []
        with open('/home/gustavo/Projetos/fso-proj/src/input/processes.txt') as processes_file:
            list = processes_file.readlines()

        self.process_queue = [Process(p.split(','), id) for (id, p) in enumerate(list)]
