import os
import subprocess

def executar_testes(lista_quanta):
    caminho = os.path.join("programas", "quantum.txt")
    
    for q in lista_quanta:
        # sobrescreve o arquivo com o quantum atual
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(str(q) + "\n")
            
        print(f"Executando para quantum = {q}")
        # executa o escalonador principal
        subprocess.run(["python", "Escalonador.py"])
        
    print("Testes concluídos. Arquivos gerados.")

if __name__ == "__main__":
    # como o tamanho máximo de um programa no sistema é de 21 comandos, testar números pares de 2 a 20 cobre desde cenários com muitas trocas de contexto até execuções quase constantes/sem parar
    testes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    executar_testes(testes)