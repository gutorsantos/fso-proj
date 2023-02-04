from colorama import Fore, Back, Style

# ERROR CODES
NOT_ENOGH_MEMO = 1                      # memory does not have space
NOT_ENOGH_SPACE = 2                     # disk does not have space
NO_PERMISSION_REMOVE_FILE = 3           # doest not have permission
INEXISTENT_REMOVE_FILE = 4              # file does not exist
EXCEEDED_RESOURCES = 5                  # system does not have the requested number of resources
BLOCKED_DUE_RESOURCES = 6               # process was blocked due to cant get requested resources

# SUCESSFUL MESSAGES
SUCESSFUL_REMOVE_FILE  = 7              # file deleted sucessfully
SUCESSFUL_CREATE_FILE = 8               # file created sucessfully

# LOG MESSAGES
START_PROCESS = 9                       # 
PROCESS_INSTRUCTION = 10
PROCESS_RETURN_SIGINT = 11

# DEBUG MESSAGES
DEALLOCATED_RESOURCES = 12
WAITING_FOR_RT_PROCESS = 13
WAITING_FOR_USER_PROCESS = 14
BLOCKED_PROCESS = 15

class Output:

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

    def error(self, code, **kwargs):
        msg = ''
        match code:
            case 1:
                msg = f'O processo {kwargs.pid} não pode ser alocado na memória por falta de espaço'
                
            case 2:
                msg = f'O processo {kwargs.pid} não pode criar o arquivo {kwargs.filename} (falta de espaço).'
            
            case 3:
                msg = f'O processo {kwargs.process.pid} não pode deletar o arquivo {kwargs.operation.file_name} (sem permissão).'
            
            case 4:
                msg = f'O processo {kwargs.process.pid} não pode deletar o arquivo {kwargs.operation.file_name} porque ele não existe.'

            case 5:
                msg = f'O Processo {kwargs.process.pid} não conseguiu ser criado (recursos insuficientes)'

            case 6:
                msg = f'O processo {kwargs.process.pid} foi bloqueado (não conseguiu obter {kwargs.resource} - requisitado: {kwargs.proc_quantity} (disponível {kwargs.max_quantity-kwargs.remaning})).'

            case _:
                msg = 'Error'

        msg = Fore.RED + msg + Fore.RESET
        print(msg)

    def sucess(self, code, **kwargs):
        msg = ''
        match code:
            case 7:
                msg = f'O processo {kwargs.process.pid} deletou o arquivo {kwargs.operation.file_name}.'
                
            case 8:
                msg = f'O processo {kwargs.process.pid} criou o arquivo {kwargs.operation.file_name} (blocos {" ".join(kwargs.block_range)}).'

        msg = Fore.GREEN + msg + Fore.RESET
        print(msg)

    def log(self, code, **kwargs):
        msg = ''
        match code:
            case 9:
                msg = f'''dispatcher =>{kwargs.process}'''
                msg += f'''process {kwargs.process.pid} => \nP{kwargs.process.pid} STARTED'''
                
            case 10:
                msg = f'P{kwargs.process.pid} instruction {kwargs.op}'
            
            case 11:
                msg = f'P{kwargs.process.pid} return SIGINT'
            
        msg = Fore.GREEN + msg + Fore.RESET
        print(msg)

    def debug(self, code, **kwargs):
        if(not self.debug_mode):
            return
        
        msg = ''
        match code:
            case 12:
                msg = 'desalocou recursos'
                
            case 13:
                msg = 'esperando por processo rt...'
            
            case 14:
                msg = 'esperando por processo usuario...'

            case 15:
                msg = 'processo bloqueou'
            
        msg = Fore.GREEN + msg + Fore.RESET
        print(msg)

        