# Gerenciador de Processos

O gerenciador de processos deve ser capaz de agrupar os processos em quatro níveis de prioridades.

## Fila - FIFO

- O programa deve ter duas filas de prioridades distintas: a fila de processos de tempo real e a fila de processos de usuários.
- Processos de usuário devem utilizar múltiplas filas de prioridades com realimentação. Para isso, devem ser mantidas três filas com prioridades distintas
- processos de usuário podem ser preemptados e o quantum deve ser definido de 1 milissegundo
- As filas devem suportar no máximo 1000 processos
