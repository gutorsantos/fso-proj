class Process:
    def __init__(self, process: list[str], id) -> None:
        self.id = id
        self.starting_time = int(process[0].strip())
        self.priority = int(process[1].strip())
        self.process_time = int(process[2].strip())
        self.memory_block = int(process[3].strip())
        self.printer_id = int(process[4].strip())
        self.scanner_request = int(process[5].strip())
        self.modem_request = int(process[6].strip())
        self.disk_id = int(process[7].strip())

    def __repr__(self) -> str:
        return f'Processo {self.id} iniciou no momento {self.starting_time}, possui prioridade {self.priority}, quota de processamento {self.process_time}, ocupa {self.memory_block}'