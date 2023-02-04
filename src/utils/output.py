from colorama import Fore, Back, Style
from utils.singleton import Singleton

# ERROR CODES
NOT_ENOGH_MEMO = 1                      # memory does not have space
NOT_ENOGH_SPACE = 2                     # disk does not have space
NO_PERMISSION_REMOVE_FILE = 3           # doest not have permission
INEXISTENT_REMOVE_FILE = 4              # file does not exist
EXCEEDED_RESOURCES = 5                  # system does not have the requested number of resources
BLOCKED_DUE_RESOURCES = 6               # process was blocked due to cant get requested resources
OPERATION_NOT_PERFORMED = 17            # process cycle number is less than number of operations

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
DEBUG_MODE_ON = 16

class Output(metaclass=Singleton):

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

    def error(self, code, **kwargs):
        msg = Fore.RED + ''
        match code:
            case 1:
                msg += Fore.MAGENTA + f'''\n\ndispatcher =>  ''' + Fore.RED
                msg += f'O processo {kwargs["pid"]} não pode ser alocado na memória por falta de espaço'
                
            case 2:
                msg += Fore.CYAN + f'\tSistema de arquivo => ' + Fore.RED
                msg += f'\tO processo {kwargs["pid"]} não pode criar o arquivo {kwargs["filename"]} (falta de espaço).'
            
            case 3:
                msg += Fore.CYAN + f'\tSistema de arquivo => ' + Fore.RED
                msg += f'O processo {kwargs["process"].pid} não pode deletar o arquivo {kwargs["filename"]} (sem permissão).'
            
            case 4:
                msg += Fore.CYAN + f'\tSistema de arquivo => ' + Fore.RED
                msg += f'\tO processo {kwargs["pid"]} não pode deletar o arquivo {kwargs["filename"]} porque ele não existe.'

            case 5:
                msg += Fore.MAGENTA + f'''\n\ndispatcher => ''' + Fore.RED
                msg += f'O processo {kwargs["pid"]} não conseguiu ser criado (recursos insuficientes)'

            case 6:
                msg += Fore.MAGENTA + f'''\n\ndispatcher => ''' + Fore.RED
                msg += f'\tO processo {kwargs["pid"]} foi bloqueado (não conseguiu obter {kwargs["resource"]} - requisitado: {kwargs["proc_quantity"]} (disponível {kwargs["max_quantity"]-kwargs["remaning"]})).'

            case 17:
                msg += f'A operação "{kwargs["op"]}" não foi executada pois o processo {kwargs["pid"]} encerrou antes'

            case _:
                msg += 'Error'

        msg = msg + Fore.RESET
        print(msg)

    def sucess(self, code, **kwargs):
        msg = Fore.GREEN + ''
        match code:
            case 7:
                msg += Fore.CYAN + f'\tSistema de arquivo => ' + Fore.GREEN
                msg += f'\tO processo {kwargs["pid"]} deletou o arquivo {kwargs["filename"]}.'
                
            case 8:
                msg += Fore.CYAN + f'\tSistema de arquivo => ' + Fore.GREEN
                msg += f'\tO processo {kwargs["pid"]} criou o arquivo {kwargs["filename"]} (blocos {" ".join(kwargs["block_range"])}).'

        msg =  msg + Fore.RESET
        print(msg)

    def log(self, code, **kwargs):
        msg = Fore.MAGENTA + ''
        match code:
            case 9:
                msg += f'''\n\ndispatcher => {kwargs['process']} \n'''
                msg += f'''process {kwargs['pid']} => \nP{kwargs['pid']} STARTED'''
                
            case 10:
                msg += f'P{kwargs["pid"]} instruction {kwargs["op"]}'
            
            case 11:
                msg += f'P{kwargs["pid"]} return SIGINT'
            
        msg = msg + Fore.RESET
        print(msg)

    def debug(self, code, *args, **kwargs):
        if(not self.debug_mode):
            return
        
        msg = Fore.YELLOW + ''
        match code:
            case 12:
                msg += 'desalocou recursos'
                
            case 13:
                msg += 'esperando por processo rt...'
            
            case 14:
                msg += 'esperando por processo usuario...'

            case 15:
                msg += 'processo bloqueou'

            case 16:
                msg += Fore.GREEN + 'DEGUB MODE ON'
            
        msg = msg + Fore.RESET
        print(msg)
