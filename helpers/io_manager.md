# Gerenciador de E/S

O gerenciador de E/S deve ser responsável por administrar a alocação e a liberação de todos os recursos disponíveis, garantindo uso exclusivo dos mesmos

- ele deve gerenciar os seguintes recursos:
    * 1 scanner
    * 2 impressoras
    * 1 modem
    * 2 dispositivos SATA
- todos os processos, com exceção daqueles de tempo-real podem obter qualquer um desses
recursos.
- O pseudo-SO deve garantir que cada recurso seja alocado para um proceso por vez.
- não há preempção na alocação dos dispositivos de E/S. 
- processos de tempo-real não precisam de recursos de I/O