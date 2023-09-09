import socket
import time


equations = [

    '5 * 4', '6 + 11', '6 - 8',
    '7 / 2', '1 - 8', '4 + 15',
    '2**8', '8**6', '14 / 5',
    '85 % 4', '25 **4', '74.58 + 48.20',
    '55 * 7', '12 + 37', '3**9'

]

# Configuração do endereço e porta do servidor
host = '127.0.0.1'  # Endereço do servidor (localhost)
port = 12345       # Porta do servidor


# Criação do socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Conecta-se ao servidor
client_socket.connect((host, port))

while True:
    # Solicita entrada do usuário
    for equation in equations:
        equation = equation

        # Inicia a contagem de tempo
        start_time = time.perf_counter()

        # Envia os números e a operação para o servidor
        client_socket.send(equation.encode())

        # Recebe e exibe a resposta do servidor
        result = client_socket.recv(1024).decode()
        end_time = time.perf_counter()
        print(equation)
        print(f"Resultado: {result}")

        # Calcula o tempo de conexão
        connection_time = (end_time - start_time)*1000
        print(f"Tempo de conexão: {connection_time:.10f} ms")

    # Esperar tecla para sair
    input()

    # Fecha a conexão com o servidor
    client_socket.close()
    break
