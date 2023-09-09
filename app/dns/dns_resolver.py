import dns.resolver

dns_cache = {}


def resolve_dns_query(domain_name: str) -> bytes:
    """
    Resolve uma consulta DNS para um nome de domínio.

    Args:
        domain_name (str): O nome de domínio a ser resolvido.

    Returns:
        bytes: Os dados da resposta DNS.

    """
    if domain_name in dns_cache:
        # Se a entrada estiver no cache, reutilize a resposta
        return dns_cache[domain_name]
    else:
        # Se o domínio não estiver no cache, resolva a consulta
        resolver = dns.resolver.Resolver()
        response = resolver.query(domain_name)
        response_data = response.to_wire()
        # Adicione ao cache
        dns_cache[domain_name] = response_data
        return response_data
