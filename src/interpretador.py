from src.filas import Filas


class Interpretador:

    def __init__(self, quantum, tabela_processos):
        self.quantum = quantum
        self.tabela = tabela_processos          # Tabela de Processos vivos
        self.num_processos = len(tabela_processos)
        self.filas = Filas()                    # fila de prontos e fila de bloqueados

        self.linhas_log = []
        self.total_interrupcoes = 0             # p/ media de trocas
        self.total_instrucoes = 0               # p/ media de instrucoes

    def registrar(self, mensagem):
        self.linhas_log.append(mensagem)

    def executar(self):
        self.filas.inicializar_processos(self.tabela)

        for p in self.filas.fila_prontos:
            self.registrar(f"Carregando {p.nome_programa}")

        while self.tabela:                     
            # ninguem pronto -> faz o tempo dos bloqueados passar
            if not self.filas.fila_prontos:
                self.filas.atualizar_fila_bloqueados()
                continue

            # redistribui so se tds zeraram
            if all(p.creditos == 0 for p in self.tabela):
                self.filas.redistribuir_creditos(self.tabela)

            processo = self.filas.fila_prontos.pop(0)   # maior credito
            self.executar_quantum(processo)

    def executar_quantum(self, processo):
        self.registrar(f"Executando {processo.nome_programa}")
        processo.estado = "EXECUTANDO"

        # comeca a rodar perde 1 credito
        if processo.creditos > 0:
            processo.creditos -= 1

        executadas = 0
        bloqueou = False
        terminou = False

        while executadas < self.quantum and not bloqueou and not terminou:
            if processo.pc >= len(processo.instrucoes):   
                terminou = True
                break

            instrucao = processo.instrucoes[processo.pc]
            processo.pc += 1                   
            executadas += 1                    

            resultado = self.executar_instrucao(processo, instrucao)
            if resultado == "E/S":
                bloqueou = True
            elif resultado == "SAIDA":
                terminou = True

        self.finalizar_quantum(processo, executadas, bloqueou, terminou)

    def executar_instrucao(self, processo, instrucao):
        if instrucao.startswith("X="):
            processo.x = int(instrucao[2:])
        elif instrucao.startswith("Y="):
            processo.y = int(instrucao[2:])
        elif instrucao == "COM":
            pass                             
        elif instrucao == "E/S":
            self.registrar(f"E/S iniciada em {processo.nome_programa}")
            return "E/S"
        elif instrucao == "SAIDA":
            return "SAIDA"
        else:
            raise ValueError(f"Instrucao invalida em {processo.nome_programa}: {instrucao!r}")
        return "OK"

    def finalizar_quantum(self, processo, executadas, bloqueou, terminou):
        # estatisticas 
        self.total_interrupcoes += 1
        self.total_instrucoes += executadas

        if terminou:
            self.registrar(f"{processo.nome_programa} terminado. X={processo.x}. Y={processo.y}")
            processo.estado = "TERMINADO"
            self.tabela.remove(processo)
        else:
            # só regista o "interrompendo..." se o programa nãao terminou
            palavra = "instrução" if executadas == 1 else "instruções"
            self.registrar(f"Interrompendo {processo.nome_programa} após {executadas} {palavra}")

        # atualiza fila de bloqueados pq caso o atual blouqueie, ele ainda n perca 1 tb
        self.filas.atualizar_fila_bloqueados()

        if bloqueou:
            self.filas.inserir_na_fila_bloqueados(processo) 
        elif not terminou:
            processo.estado = "PRONTO"
            self.filas.inserir_na_fila_prontos(processo)    

    def estatisticas(self):
        return {
            "media_trocas": self.total_interrupcoes / self.num_processos,
            "media_instrucoes": self.total_instrucoes / self.total_interrupcoes,
            "quantum": self.quantum,
        }