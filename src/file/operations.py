class Operation:
    def __init__(self, operation: list[str]) -> None:
        self.process_id = int(operation[0].strip())
        self.operation_id = int(operation[1].strip())
        self.file_name = operation[2].strip()
        self.created_block_size = int(operation[3].strip()) if self.operation_id == 0 else -1

    def __repr__(self) -> str:
        return f'Operação do processo {self.process_id} de { "criação" if self.operation_id == 0 else "remoção" } do arquivo {self.file_name}'