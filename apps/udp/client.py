import socket
import time
from consts import HOST, SERVER_DNS_PORT
from logger import Logger

logger = Logger("UDP CLIENT")

DOMAIN_NAME = "udp-server"
equations = [
    "5 * 4",
    "6 - 8",
    "1 - 8",
    "2**8",
    "14 / 5",
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
            ip_address, server_port = server_address.split(":")

        return (ip_address, int(server_port))

    except Exception as e:
        # Handle any exceptions that may occur during DNS resolution
        logger.log(f"Error resolving domain '{domain_name}': {str(e)}")
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

    client_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Send equation to the server
        client_udp.sendto(equation.encode(), (ip_address, port))

        # Receive the server's response
        result = client_udp.recv(1024).decode()

    finally:
        # Close the client socket
        client_udp.close()

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

    logger.info("UDP Client is running")

    try:
        for equation in equations:
            logger.log(f"Equation: {equation}")

            # Find de ip address of the server
            ip_address, port = find_ip_address(DOMAIN_NAME)

            time_start = time.perf_counter()

            # Resolve the equation
            result = resolve_equation(ip_address, port, equation)
            logger.log(f"Result: {result}")

            time_end = time.perf_counter()
            logger.log(f"Time: {(time_end - time_start) * 1000:.10f}ms")

        input("Press any key to exit...")
        logger.log("Bye!")

    except KeyboardInterrupt:
        logger.log("Exiting...")


if __name__ == "__main__":
    main()
