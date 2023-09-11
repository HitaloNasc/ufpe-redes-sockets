import socket
from consts import DOMAINS, HOST, SERVER_DNS_PORT
from logger import Logger

logger = Logger("DNS SERVER")

dns_cache = {}


def resolve_dns_query(domain_name: str) -> str:
    """
    Resolve a DNS query for a domain name.

    Args:
        domain_name (str): The domain name to be resolved.

    Returns:
        str: A string containing DNS response data. IP_ADDRESS:PORT

    """
    if domain_name in dns_cache:
        # If the entry is in the cache, reuse the response
        logger.info("Domain found in cache")
        return dns_cache[domain_name]
    else:
        # If the domain is not in the cache, resolve the query
        response_data = DOMAINS[domain_name]
        logger.info("Domain resolved")

        # Add to the cache
        dns_cache[domain_name] = response_data
        return response_data


def main() -> None:
    """
    Main function for running a DNS server.

    Returns:
        None
    """
    # Create a UDP socket for the DNS server
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((HOST, SERVER_DNS_PORT))
    logger.info(f"DNS Server is running on {HOST}:{SERVER_DNS_PORT}")

    try:
        while True:
            # Handle DNS queries
            data, client_address = udp_socket.recvfrom(1024)
            logger.log("UDP connection established")

            # Get the domain name from the query
            domain_name = data.decode()
            logger.log(f"Domain name: {domain_name}")

            # Check if the domain is in the cache and resolve the request
            ip_address = resolve_dns_query(domain_name)

            if not ip_address:
                raise Exception("Domain not found")

            logger.log(f"IP address: {ip_address}")

            response = ip_address.encode()

            # Send the DNS response back to the client
            udp_socket.sendto(response, client_address)

    except KeyboardInterrupt:
        logger.log("Exiting...")

    finally:
        udp_socket.close()


if __name__ == "__main__":
    main()
