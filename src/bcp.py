# Bloco de Controle de Processo que contém todo o contexto do processo
class BCP:
    def __init__(self, nome_programa, instrucoes, prioridade):
        self.nome_programa = nome_programa  
        self.instrucoes = instrucoes       
        self.pc = 0                        
        self.estado = "PRONTO"             
        self.prioridade = prioridade       
        self.creditos = prioridade         
        self.x = 0                          
        self.y = 0                          
        self.tempo_espera_es = 0           

    def __repr__(self):
        return f"[{self.nome_programa}] Prioridade/Créditos: {self.prioridade} | Instruções: {len(self.instrucoes)}"