import socket
from consts import HOST, SERVER_UDP_PORT


def create_udp_socket(host: str, port: int) -> socket:
    """
    Creates a UDP socket with the given host and port.

    Args:
        host (str): The IP address or hostname of the server.
        port (int): The port number to bind the socket to.

    Returns:
        socket: The created UDP socket.

    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    return server_socket


def handle_client_request(server_socket: socket) -> None:
    """
    Receives a client request and handles it by evaluating an equation and returning the result to the client.

    Args:
        server_socket (socket): The server socket object.

    Returns:
        None: This function does not return anything.

    """
    data, client_address = server_socket.recvfrom(1024)
    print(f"Connection established with {client_address}")

    if not data:
        return

    equation = data.decode()

    try:
        result = eval(equation)
        print(f'\t{equation} = {result}')
        server_socket.sendto(str(result).encode(), client_address)
    except Exception as e:
        server_socket.sendto(str(e).encode(), client_address)


def main():
    """
    The main function that creates a UDP server for evaluating mathematical expressions.
    """
    server_socket = create_udp_socket(HOST, SERVER_UDP_PORT)
    print(f"UDP Server is listening on {HOST}:{SERVER_UDP_PORT}...")

    try:
        while True:
            handle_client_request(server_socket)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
