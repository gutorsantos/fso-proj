# Gerenciador de Arquivos

O gerenciador de arquivos deve permitir que os processos possam criar e deletar arquivos, de acordo com o modelo de alocação determinado

- permitir que cada processo possa criar e deletar arquivos
- Na criação de um
arquivo, os dados devem ficar residentes no disco, mesmo após o encerramento do processo
- O sistema de
arquivos fará a alocação por meio do método de alocação contígua
- algoritmo a ser usado no armazenamento do disco seja o **first-fit**
- o sistema de arquivos deve garantir que os processos de tempo real possam criar (se
tiver espaço) e deletar qualquer arquivo (mesmo que não tenha sido criado pelo processo)
- Por outro lado, os processos comuns do usuário, só podem deletar arquivos que tenham sido criados por eles, e podem criar quantos arquivos desejarem, no tamanho que for solicitado (se houver espaço suficiente).
- O sistema de arquivos terá como entrada um arquivo com extensão .txt, que contém a quantidade
total de blocos no disco, a especificação dos segmentos ocupados por cada arquivo, as operações a serem realizadas por cada processo.
- após o pseudo-SO executar todos os processos, ele deve mostrar na tela do computador um
mapa com a atual ocupação do disco, descrevendo quais arquivos estão em cada bloco, e quais são os
blocos vazios (identificados por 0)