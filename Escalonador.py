from src.leitor import carregar_sistema
from src.filas import Filas
from src.interpretador import Interpretador
from src.exportador import ExportadorLog

def main():
    print("Carregando sistema...")
    quantum, tabela_processos = carregar_sistema("programas")
    print(f"\nQuantum definido: {quantum}")

    print("Tabela de Processos Carregada:")
    for processo in tabela_processos:
        print(processo)

    filas = Filas()
    filas.inicializar_processos(tabela_processos)

    print("Tabela de Processos Ordenada:")
    for processo in filas.fila_prontos:
        print(processo)

    interpretador = Interpretador(quantum, tabela_processos)
    interpretador.executar()
        
    est = interpretador.estatisticas()

    exportador = ExportadorLog() #agora os logs são arquivos ao invés de prints no terminal
    exportador.exportar(quantum, interpretador.linhas_log, est)
    
    print("Execução finalizada e log exportado.")

if __name__ == "__main__":
    main()