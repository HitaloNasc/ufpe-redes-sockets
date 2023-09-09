import socket
import dns.message
from .dns_resolver import resolve_dns_query


def handle_udp_dns_query(udp_socket: socket, data: bytes, client_address: socket._RetAddress) -> None:
    """
    Handles a UDP DNS query.

    Args:
        udp_socket (socket): The UDP socket to handle the query.
        data (bytes): The data received in the query.
        client_address (socket._RetAddress): The address of the client making the query.

    Returns:
        None

    """

    # Cria uma mensagem DNS a partir dos dados recebidos
    request = dns.message.from_wire(data)

    # Obtém o nome do domínio a partir da consulta
    domain_name = str(request.question[0].name)

    # Verifica se o domínio está no cache e resolve a requisição
    response = resolve_dns_query(domain_name)

    # Envia a resposta DNS de volta ao cliente
    udp_socket.sendto(response, client_address)


# def handle_dns_query_tcp(tcp_socket: socket, data: bytes, client_address:  socket._RetAddress):

#     response_data = handle_dns_query(data, tcp_socket.getpeername())
#     tcp_socket.send(response_data)
#     tcp_socket.close()
