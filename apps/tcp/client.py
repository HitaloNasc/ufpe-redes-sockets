import socket
import time
from consts import HOST, SERVER_DNS_PORT

DOMAIN_NAME = 'tcp-server'
equations = [
    '6 + 11',
    '7 / 2',
    '4 + 15',
    '8**6',
    '85 % 4',
]


def find_ip_address(domain_name: str) -> tuple:
    """
    Finds the IP address of a domain name using a DNS server.

    Args:
        domain_name (str): The domain name to be resolved.

    Returns:
        tuple: A tuple containing the IP address (str) and the server port (int) of the domain name.
    """
    try:
        # Create a UDP socket for DNS resolution
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_udp:
            # Send a DNS query to resolve the domain name
            client_udp.sendto(DOMAIN_NAME.encode(), (HOST, SERVER_DNS_PORT))
            server_address = client_udp.recv(1024).decode()
            ip_address, server_port = server_address.split(':')

        return (ip_address, int(server_port))

    except Exception as e:
        # Handle any exceptions that may occur during DNS resolution
        print(f"Error resolving domain '{domain_name}': {str(e)}")
        return (None, None)


def resolve_equation(ip_address: str, port: int, equation: str) -> str:
    """
    Sends an equation to the server and receives the result.

    Args:
        ip_address (str): The IP address of the server.
        port (int): The port number to bind the socket to.
        equation (str): The equation to be sent to the server.

    Returns:
        str: The result of the equation.

    """

    client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_tcp.connect((ip_address, port))

    # Send equation to the server
    client_tcp.sendall(equation.encode())

    # Receive the server's response
    result = client_tcp.recv(1024).decode()

    # Close the client socket
    client_tcp.close()

    # Return the result
    return result


def main() -> None:
    """
    Executes the main routine of the TCP client.

    Args:
        None

    Returns:
        None
    """

    for equation in equations:
        print(f'Equation: {equation}')

        time_start = time.perf_counter()

        # Find de ip address of the server
        ip_address, port = find_ip_address(DOMAIN_NAME)

        # Resolve the equation
        result = resolve_equation(ip_address, port, equation)
        print(f'\tResult: {result}')

        time_end = time.perf_counter()
        print(f'\tTime: {(time_end - time_start) * 1000:.10f}ms')

    input('Press any key to exit...')
    print('Bye!')


if __name__ == '__main__':
    main()
