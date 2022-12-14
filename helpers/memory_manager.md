# Gerenciador de Memória

O gerenciador de memória deve garantir que um processo não acesse as regiões de memória de um outro processo

## Estrutura Memória

- A alocação de memória deve ser implementada como um conjunto de blocos contíguos, onde cada bloco equivale uma palavra da memória real.
- Cada processo deve alocar um segmento contíguo de memória, o qual permanecerá alocado durante toda a execução do processo. 
- Deve-se notar que não é necessário a implementação de memória virtual, swap, nem sistema de paginação. 
- não é necessário gerenciar a memória, apenas verificar a disponibilidade de recursos antes de iniciar um processo.
- tamanho fixo de memória de 1024 blocos
-  64 blocos devem ser reservados para processos de tempo-real e os 960 blocos restantes devem ser compartilhados entre os processos de usuário.