class File:
    def __init__(self, file: list[str]) -> None:
        self.name = file[0].strip()
        self.first_block = int(file[1].strip())
        self.size_block = int(file[2].strip())

    def __repr__(self) -> str:
        return f'Arquivo {self.name} está no bloco {self.first_block} tem tamanho {self.size_block} blocos'