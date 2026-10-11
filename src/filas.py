from src.bcp import BCP

class Filas:
    def __init__(self):
        self.fila_prontos = []
        self.fila_bloqueados = []

    # carrega todos os processos inicialmente na fila de prontos
    def inicializar_processos(self, tabela_processos):
        for processo in tabela_processos:
            self.fila_prontos.append(processo)
        
        self.ordenar_por_creditos()

    # como o sort do python é estável, ele mantém a ordem de chegada em caso de empate nos créditos
    def ordenar_por_creditos(self):
        self.fila_prontos.sort(key=lambda x: x.creditos, reverse=True)

    def inserir_na_fila_prontos(self, processo):
        self.fila_prontos.append(processo)
        self.ordenar_por_creditos()

    def inserir_fim_fila_prontos(self, processo):
        # usado quando o processo zera os créditos, assim vai para o fim da fila como um processo comum
        processo.estado = "PRONTO"
        self.fila_prontos.append(processo)

    def redistribuir_creditos(self, tabela_processos):
        # restaura os créditos baseados na prioridade original de cada processo que ainda está
        for processo in tabela_processos:
            processo.creditos = processo.prioridade
        self.ordenar_por_creditos()

    def inserir_na_fila_bloqueados(self, processo):
        # bloqueio dura o tempo de 2 processos passarem pela CPU
        processo.tempo_espera_es = 2
        processo.estado = "BLOQUEADO"
        self.fila_bloqueados.append(processo)

    def atualizar_fila_bloqueados(self):
        # itera sobre uma cópia da lista para permitir tirar os itens durante o loop
        for processo in self.fila_bloqueados[:]:
            processo.tempo_espera_es -= 1

            # se o tempo de espera zerou, o processo acorda e volta para os prontos
            if processo.tempo_espera_es <= 0:
                self.fila_bloqueados.remove(processo)
                processo.estado = "PRONTO"
                self.inserir_na_fila_prontos(processo)