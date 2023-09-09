import socket
import dns.message
import dns.query
import dns.resolver
import threading

# Configuração do endereço e porta do servidor DNS
dns_host = '127.0.0.1'
dns_port = 8053

# Configuração do endereço e porta dos servidores
server_tcp_host = '127.0.0.1'
server_tcp_port = 12345

server_udp_host = '127.0.0.1'
server_udp_port = 54321

# Cache DNS sem tempo de expiração
dns_cache = {}

def handle_dns_query(data, client_address):
    # Cria uma mensagem DNS a partir dos dados recebidos
    request = dns.message.from_wire(data)
    
    # Obtém o nome do domínio a partir da consulta
    domain_name = str(request.question[0].name)
    
    # Verifica se o domínio está no cache
    if domain_name in dns_cache:
        # Se a entrada estiver no cache, reutilize a resposta
        response_data = dns_cache[domain_name]
    else:
        # Se o domínio não estiver no cache, resolva a consulta
        resolver = dns.resolver.Resolver()
        response = resolver.query(domain_name)
        response_data = response.to_wire()
        # Adicione ao cache
        dns_cache[domain_name] = response_data
    
    # Envia a resposta DNS de volta ao cliente
    udp_client_socket.sendto(response_data, client_address)
    
    # Remove a entrada do cache após responder à consulta
    if domain_name in dns_cache:
        del dns_cache[domain_name]

def handle_dns_query_tcp(client_socket):
    data = client_socket.recv(1024)
    response_data = handle_dns_query(data, client_socket.getpeername())
    client_socket.send(response_data)
    client_socket.close()

# Cria um socket UDP para o servidor DNS
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind((dns_host, dns_port))

# Cria um socket TCP para o servidor DNS
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind((dns_host, dns_port))
tcp_server_socket.listen(5)

# Cria um socket UDP para o cliente
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Cria um socket TCP para o cliente
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("Servidor DNS em execução...")

while True:
    # Lida com consultas UDP
    udp_data, udp_client_address = udp_server_socket.recvfrom(1024)
    threading.Thread(target=handle_dns_query, args=(udp_data, udp_client_address)).start()
    print("Conexão UDP estabelecida")
    
    # Lida com consultas TCP
    tcp_connection, tcp_client_address = tcp_server_socket.accept()
    threading.Thread(target=handle_dns_query_tcp, args=(tcp_connection,)).start()
    print("Conexão TCP estabelecida")
