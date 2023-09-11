import socket
from consts import HOST, SERVER_TCP_PORT
from logger import Logger

logger = Logger("TCP SERVER")


def create_tcp_socket(host: str, port: int) -> socket:
    """
    Creates a TCP socket with the given host and port.

    Args:
        host (str): The IP address or hostname of the server.
        port (int): The port number to bind the socket to.

    Returns:
        socket: The created TCP socket.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    return server_socket


def handle_client_request(client_socket: socket) -> None:
    """
    Receives and handles client requests by evaluating mathematical expressions and returning the result.

    Args:
        client_socket (socket): The client socket object.

    Returns:
        None: This function does not return anything.
    """
    client_address = client_socket.getpeername()
    logger.log(f"Connection established with {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        equation = data.decode()
        try:
            result = eval(equation)
            logger.log(f"{equation} = {result}")
            client_socket.send(str(result).encode())
        except Exception as e:
            client_socket.send(str(e).encode())

    client_socket.close()


def main():
    """
    The main function that creates a TCP server for evaluating mathematical expressions.
    """
    server_socket = create_tcp_socket(HOST, SERVER_TCP_PORT)
    logger.info(f"TCP Server is running on {HOST}:{SERVER_TCP_PORT}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            handle_client_request(client_socket)
    except KeyboardInterrupt:
        logger.log("Exiting...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
