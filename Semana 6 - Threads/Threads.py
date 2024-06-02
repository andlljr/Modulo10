import threading
import time

# Função que cada thread irá executar
def soma_parcial(lista, resultado, indice):
    # Somar a lista parcial inserida
    soma = sum(lista)
    # Salvar o valor no array resultado do índice
    resultado[indice] = soma

def calcular_soma_com_threads(lista_numeros):
    # Inicializar contagem de tempo
    inicio = time.time() 
    
    # Dividir a lista em 2
    meio = len(lista_numeros) // 2
    # Salvar listas separadas para realizar a soma nos arrays
    parte1 = lista_numeros[:meio]
    parte2 = lista_numeros[meio:]
    # Criar lista onde será inserido o resultado
    resultado = [0, 0]

    # Criando as threads chamando a função e adiconando os parâmetros
    thread1 = threading.Thread(target=soma_parcial, args=(parte1, resultado, 0))
    thread2 = threading.Thread(target=soma_parcial, args=(parte2, resultado, 1))
    # Iniciando as threads
    thread1.start()
    thread2.start()
    # Esperando as threads terminarem
    thread1.join()
    thread2.join()

    # Soma o resultado gerado por cada Thread
    soma_total = sum(resultado)

    # Finaliza a contagem do tempo
    fim = time.time() 
    # Calcula o tempo de processamento
    tempo_processamento = fim - inicio  

    # Retorna a soma das duas listas e o tempo levado para operação
    return soma_total, tempo_processamento

def main():
    # Testes
    lista1 = [1, 2, 3, 4, 5]
    soma1, tempo1 = calcular_soma_com_threads(lista1)
    print(f"Teste 1 - Lista: {lista1}, Soma: {soma1}, Tempo de processamento: {tempo1:.6f} segundos")

    lista2 = [-2, -1, 0, 1, 2]
    soma2, tempo2 = calcular_soma_com_threads(lista2)
    print(f"Teste 2 - Lista: {lista2}, Soma: {soma2}, Tempo de processamento: {tempo2:.6f} segundos")

    lista3 = [999, 554, 239, 102, 23]
    soma3, tempo3 = calcular_soma_com_threads(lista3)
    print(f"Teste 3 - Lista: {lista3}, Soma: {soma3}, Tempo de processamento: {tempo3:.6f} segundos")


if __name__ == "__main__":
    main()
