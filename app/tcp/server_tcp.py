import socket

# Configuração do endereço e porta do servidor
host = '127.0.0.1'  # Endereço do servidor (localhost)
port = 12345       # Porta do servidor

# Criação do socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket a um endereço e porta
server_socket.bind((host, port))

# Define quantas conexões o servidor pode esperar em fila
server_socket.listen(1)
print(f"Servidor aguardando conexão em {host}:{port}...")

# Aceita uma conexão
client_socket, client_address = server_socket.accept()

print(f"Conexão estabelecida com {client_address}")

while True:

    # Recebe a equação do cliente
    equation = client_socket.recv(1024).decode()
    if not equation:
        break
    
    try:
        # Usa a função eval para calcular a expressão
        result = eval(equation)

        # Envia o resultado de volta para o cliente
        client_socket.send(str(result).encode())
    except Exception as e:
        # Se ocorrer um erro ao calcular a expressão, envie uma mensagem de erro
        client_socket.send(str(e).encode())


# Fecha a conexão com o cliente e o servidor
client_socket.close()
server_socket.close()
