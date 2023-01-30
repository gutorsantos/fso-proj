class Process:
    def __init__(self, process: list[str], id) -> None:
        '''Contexto de software'''

        ## Identificacao
        self.pid = id
        # self.uid = uid (?)
       
        ## Quotas
        self.starting_time = int(process[0].strip())
        self.process_time = int(process[2].strip())
        self.aging = 0
        self.printer_id = int(process[4].strip())
        self.scanner_request = int(process[5].strip())
        self.modem_request = int(process[6].strip())
        self.disk_id = int(process[7].strip())

        ## Privilegios
        self.priority = int(process[1].strip())
        
        '''Fim do contexto de software'''

        ''' Espaco de enderecamento '''
        self.memory_start_block = -1
        self.memory_block_size = int(process[3].strip())

        ''' Fim do espaco de enderecamento '''

        ''' Contexto de hardware
            não existe nesse contexto
            os registradores foram abstraidos
        '''
        

    def __repr__(self) -> str:
        return f'Processo {self.pid} iniciou no momento {self.starting_time}, possui prioridade {self.priority}, quota de processamento {self.process_time}, ocupa {self.memory_block_size}'