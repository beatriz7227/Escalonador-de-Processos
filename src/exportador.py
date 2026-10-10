import os

class ExportadorLog:
    # guarda os arquivos exportados na pasta logs
    def __init__(self, caminho="logs"):
        self.caminho = caminho
        # cria pasta para os logs se ela não existir
        os.makedirs(self.caminho, exist_ok=True)

    # gera o arquivo do log
    def exportar(self, quantum, linhas_log, estatisticas):
        # formatação do nome do arquivo
        nome_arquivo = "log{:02d}.txt".format(quantum)
        caminho_completo = os.path.join(self.caminho, nome_arquivo)

        print(f"A gerar ficheiro {caminho_completo}")

        # abre o arquivo para alteração
        with open(caminho_completo, "w", encoding="utf-8") as f:
            # histórico de eventos de escalonamento
            for linha in linhas_log:
                f.write(linha + "\n")
            
            # estatísticas finais
            f.write(f"MEDIA DE TROCAS: {estatisticas['media_trocas']}\n")
            f.write(f"MEDIA DE INSTRUCOES: {estatisticas['media_instrucoes']}\n")
            f.write(f"QUANTUM: {estatisticas['quantum']}\n")
            
        return caminho_completo