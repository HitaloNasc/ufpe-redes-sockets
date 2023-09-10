import socket
from consts import DOMAINS, HOST, SERVER_DNS_PORT

dns_cache = {}


def resolve_dns_query(domain_name: str) -> str:
    """
    Resolve a DNS query for a domain name.

    Args:
        domain_name (str): The domain name to be resolved.

    Returns:
        str: A string containing DNS response data. IP_ADDRESS:PORT

    Raises:
        Exception: Raises an exception if the domain is not found.

    """
    if domain_name in dns_cache:
        # If the entry is in the cache, reuse the response
        print('\tDomain found in cache')

        return dns_cache[domain_name]
    else:
        # If the domain is not in the cache, resolve the query
        response_data = DOMAINS[domain_name]
        print('\tDomain resolved')

        if not response_data:
            raise Exception('Domain not found')

        # Add to the cache
        dns_cache[domain_name] = response_data

        return response_data


def handle_udp_dns_query(udp_socket: socket, data: bytes, client_address: socket) -> None:
    """
    Handles a UDP DNS query.

    Args:
        udp_socket (socket): The UDP socket used for communication.
        data (bytes): The DNS query data received from the client.
        client_address (socket): The address of the DNS client.

    Returns:
        None

    """
    # Get the domain name from the query
    domain_name = data.decode()

    # Check if the domain is in the cache and resolve the request
    ip_address = resolve_dns_query(domain_name)
    print(f'\tDomain name: {domain_name}')
    print(f'\tIP address: {ip_address}')

    response = ip_address.encode()

    # Send the DNS response back to the client
    udp_socket.sendto(response, client_address)


def main() -> None:
    """
    Main function for running a UDP DNS server.

    Returns:
        None
    """
    # Create a UDP socket for the DNS server
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((HOST, SERVER_DNS_PORT))
    print("DNS Server is running...")

    while True:
        # Handle UDP queries
        udp_data, udp_client_address = udp_socket.recvfrom(1024)
        print("UDP connection established")
        handle_udp_dns_query(udp_socket, udp_data, udp_client_address)


if __name__ == "__main__":
    main()
