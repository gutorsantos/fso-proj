class Disk:
    def __init__(self, disk: list[str]) -> None:
        self.blocks = int(disk[0].strip())
        self.filled_segments = int(disk[1].strip())

    def __repr__(self) -> str:
        return f'O disco possui tamanho {self.blocks} blcoos e possui {self.filled_segments} segmentos ocupados'