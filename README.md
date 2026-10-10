# Escalonador de Processos

> Exercício-Programa (EP1) desenvolvido para a disciplina de Sistemas Operacionais do curso de Sistemas de Informação da Escola de Artes, Ciências e Humanidades da Universidade de São Paulo (EACH-USP)..

Este projeto implementa um escalonador de tarefas em uma máquina fictícia com um único processador, criando um sistema simples de multiprogramação. Assim, a aplicação funciona como um interpretador de comandos que gerencia o ciclo de vida dos processos, simulando trocas de contexto, gestão de prioridades, alocação de tempo de CPU e bloqueios por operações de Entrada e Saída (E/S).

## Sumário

* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Principais Funcionalidades](#-principais-funcionalidades)
* [Organização de Arquivos](#-organização-de-arquivos)
* [Como Executar a Aplicação](#-como-executar-a-aplicação)
* [Grupo](#-grupo)

## Tecnologias Utilizadas

O projeto foi desenvolvido inteiramente com bibliotecas do python para garantir fácil execução:

* **Python**: Linguagem para toda a lógica de leitura, interpretação e simulação de escalonamento.
* **OS & Subprocess**: Utilizados para a manipulação de caminhos de diretórios, geração automatizada de pastas de log e execução de scripts em lote para testes.

## Principais Funcionalidades

A aplicação foi concebida para gerenciar com precisão as transições de estado dos processos, resolvendo desafios clássicos de escalonamento dinâmico:

* **Algoritmo Baseado em Créditos:** Escalonamento dinâmico e preventivo, onde processos perdem créditos ao rodar e a CPU é sempre entregue ao processo com maior saldo na fila de prontos.
* **Gestão de E/S e Bloqueios:** Os processos que puxam instruções de E/S são suspensos e alocados em uma Fila de Bloqueados (FIFO), aguardando um tempo específico ditado por ciclos de outros processos na CPU.
* **Redistribuição Dinâmica:** Mecanismo automático que restaura os créditos originais de todos os processos quando o sistema entra em escassez total de créditos.
* **Automação de Testes:** Capacidade de rodar lotes de testes programáticos, variando o tamanho do *quantum*, gerando estatísticas de desempenho e exportando relatórios automatizados (`logXX.txt`).

## Organização dos Arquivos

O projeto encontra-se modularizado na seguinte estrutura:

* **`Escalonador.py`**: Ponto de entrada principal que gerencia o carregamento, a criação das estruturas e a chamada do interpretador.
* **`automacao.py`**: Script para automatizar a execução de testes com vários valores de *quantum* para análise estatística.
* **Módulos do Sistema (`src/`)**:
  * **`bcp.py`**: Estrutura de dados do Bloco de Controle de Processo, armazenando o estado, PC, registradores (X, Y) e créditos.
  * **`filas.py`**: Classe responsável por organizar e manipular a Fila de Prontos, por créditos, e a Fila de Bloqueados, por tempo de espera.
  * **`interpretador.py`**: Lê e executa as instruções simuladas (`X=`, `Y=`, `COM`, `E/S`, `SAIDA`) e aciona as preempções.
  * **`leitor.py`**: Lê e faz o parse da pasta de entrada transformando os arquivos `.txt` em objetos BCP.
  * **`exportador.py`**: Formata e exporta de forma isolada os logs de execução e estatísticas finais.
* **`programas/`**: Pasta contendo os 10 arquivos de programas (`01.txt` a `10.txt`), o `prioridades.txt` e o `quantum.txt`.
* **`logs/`**: Pasta gerada contendo os logs do sistema após a execução.

## Como Executar a Aplicação

### Pré-requisitos

* Ter o **Python** instalado em sua máquina.
* Garantir que a pasta `programas/` contendo os scripts dos processos se encontra na raiz do projeto.

### Execução Padrão

Para rodar a simulação com o *quantum* definido atualmente no arquivo `programas/quantum.txt`:

1. Abra o terminal na pasta raiz do projeto.
2. Execute o arquivo principal:
   ```bash
   python Escalonador.py
   ```
O log gerado aparecerá automaticamente dentro da pasta `logs/`.

### Execução em Lote/Bateria de Testes

Para avaliar o sistema e gerar automaticamente logs para 10 valores diferentes de *quantum*:

1. No terminal, na raiz do projeto, execute o script de automação:
   ```bash
   python automacao.py
   ```
2. Ao final do processamento, acesse a pasta `logs/` para conferir os arquivos exportados e as estatísticas geradas para análise.

## 👥 Grupo

Este projeto foi desenvolvido pelo grupo:

* **Ana Beatriz** - [@bianatriz](https://github.com/bianatriz)
* **Arthur Brandão** - [@ArthurBrandaoM](https://github.com/ArthurBrandaoM)
* **Beatriz dos Santos** - [@beatriz7227](https://github.com/beatriz7227)
* **Caio Gaspar** - [@Caio-Gaspar](https://github.com/Caio-Gaspar)
* **Fernanda Yumi** - [@feyumiii](https://github.com/feyumiii)
