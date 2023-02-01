class File:
    def __init__(self, file: list[str]) -> None:
        self.name = file[0].strip()
        self.first_block = int(file[1].strip())
        self.block_size = int(file[2].strip())
        self.created_by = 0

    def __repr__(self) -> str:
        return f'Arquivo {self.name} está no bloco {self.first_block} tem tamanho {self.block_size} blocos'