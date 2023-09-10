import socket
import time
from consts import HOST, SERVER_DNS_PORT

equations = [
    '5 * 4',    '6 + 11',
    '6 - 8',    '7 / 2',
    '1 - 8',    '4 + 15',
    '2**8',     '8**6',
    '14 / 5',   '85 % 4',
    '25**4',    '74.58 + 48.20',
    '55 * 7',   '12 + 37',
]


def create_udp_socket() -> socket:
    """
    Create a UDP socket.

    Returns:
        socket: A UDP socket object.

    """
    # Create a UDP socket
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_equation(client_socket: socket, equation: str) -> None:
    """
    Sends an equation to the server and receives the result.

    Args:
        client_socket (socket): The socket object used to communicate with the server.
        equation (str): The equation to be sent to the server.

    Returns:
        None

    """
    # Start timer
    start_time = time.perf_counter()

    # Get IP address of the server
    client_socket.sendto('udp-server'.encode(), (HOST, SERVER_DNS_PORT))
    server_address = client_socket.recv(1024).decode()
    IP_SERVER, PORT_SERVER = server_address.split(':')

    # Send numbers and operation to the server
    client_socket.sendto(
        equation.encode(),
        (IP_SERVER, int(PORT_SERVER))
    )

    # Receive and display the server's response
    result = client_socket.recv(1024).decode()
    end_time = time.perf_counter()
    print(f'\t{equation} = {result}')

    # Calculate connection time
    connection_time = (end_time - start_time) * 1000
    print(f"\tTime: {connection_time:.10f} ms")


def main() -> None:
    """
    Runs the UDP client.

    This function creates a UDP socket and enters a loop that continuously requests user input
    for a list of equations, sends each equation to a server using the UDP socket, and waits for
    user input to exit the program. If a keyboard interrupt is caught, the function prints a
    message indicating that the program is exiting. Finally, the function closes the connection
    with the server by closing the UDP socket.

    Args:
        None

    Returns:
        None

    """
    # Create a UDP socket
    client_socket = create_udp_socket()

    try:
        while True:
            # Request user input
            for equation in equations:
                print(f'Equation: {equation}')
                send_equation(client_socket, equation)

            # Wait for user input to exit
            input()

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        # Close the connection with the server
        client_socket.close()


if __name__ == "__main__":
    main()
