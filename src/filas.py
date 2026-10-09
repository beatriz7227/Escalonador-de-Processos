from src.bcp import BCP

class Filas:
    def __init__(self):
        self.fila_prontos = []
        self.fila_bloqueados = []

    def inicializar_processos(self, tabela_processos):
        for processo in tabela_processos:
            self.fila_prontos.append(processo)
        
        self.ordenar_por_creditos()

    def ordenar_por_creditos(self):
        self.fila_prontos.sort(key=lambda x: x.creditos, reverse=True)

    def inserir_na_fila_prontos(self, processo):
        self.fila_prontos.append(processo)
        self.ordenar_por_creditos()

    def inserir_fim_fila_prontos(self, processo):
        processo.estado = "PRONTO"
        self.fila_prontos.append(processo)

    def descontar_credito(self, processo):
        if processo.creditos > 0:
            processo.creditos -= 1
            self.ordenar_por_creditos()
        if processo.creditos == 0:
            self.fila_prontos.remove(processo)
            self.inserir_fim_fila_prontos(processo)
        
    def verificar_todos_zerados(self):
        if not self.fila_prontos:
            return False
            
        for processo in self.fila_prontos:
            if processo.creditos > 0:
                return False
        return True

    def redistribuir_creditos(self, tabela_processos):
        for processo in tabela_processos:
            processo.creditos = processo.prioridade
        self.ordenar_por_creditos()

    def inserir_na_fila_bloqueados(self, processo):
        processo.tempo_espera_es = 2
        processo.estado = "BLOQUEADO"
        self.fila_bloqueados.append(processo)

    def atualizar_fila_bloqueados(self):
        for processo in self.fila_bloqueados[:]:
            processo.tempo_espera_es -= 1
            
            if processo.tempo_espera_es <= 0:
                self.fila_bloqueados.remove(processo)
                processo.estado = "PRONTO"
                self.inserir_na_fila_prontos(processo)