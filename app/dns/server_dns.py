import socket
from threading import Thread
from .consts import HOST, SERVER_DNS_PORT
from .dns_handler import handle_udp_dns_query


def main() -> None:
    """
    Initializes UDP and TCP sockets for the DNS server and starts listening for incoming queries.
    """

    # Cria um socket UDP para o servidor DNS
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((HOST, SERVER_DNS_PORT))

    # Cria um socket TCP para o servidor DNS
    # tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcp_socket.bind((HOST, SERVER_DNS_PORT))
    # tcp_socket.listen(5)

    print("Servidor DNS em execução...")

    while True:
        # Lida com consultas UDP
        udp_data, udp_client_address = udp_socket.recvfrom(1024)
        Thread(
            target=handle_udp_dns_query,
            args=(udp_socket, udp_data, udp_client_address)
        ).start()

        print("Conexão UDP estabelecida")

        # # Lida com consultas TCP
        # data = tcp_socket.recv(1024)
        # Thread(
        #     target=handle_dns_query_tcp,
        #     args=(tcp_socket,)).start()
        # print("Conexão TCP estabelecida")


if __name__ == "__main__":
    main()
