class Operation:
    def __init__(self, process_id: str, operation_id: str, file_name: str, created_block_size:str='-1') -> None:
        self.process_id = int(process_id.strip())
        self.operation_id = int(operation_id.strip())
        self.file_name = file_name.strip()
        self.created_block_size = int(created_block_size.strip())
        
    def __repr__(self) -> str:
        return f'Operação do processo {self.process_id} de "criação" do arquivo {self.file_name} ({self.created_block_size} blocos)'

class CreateOperation(Operation):
    def __init__(self, process_id: str, operation_id: str, file_name: str, created_block_size: str) -> None:
        super().__init__(process_id, operation_id, file_name) 
        self.created_block_size = int(created_block_size.strip())

    def __repr__(self) -> str:
        return f'Operação do processo {self.process_id} de "criação" do arquivo {self.file_name} ({self.created_block_size} blocos)'
    
class DeleteOperation(Operation):
    def __init__(self, process_id: str, operation_id: str, file_name: str) -> None:
        super().__init__(process_id, operation_id, file_name) 

    def __repr__(self) -> str:
        return f'Operação do processo {self.process_id} de "remoção" do arquivo {self.file_name}'