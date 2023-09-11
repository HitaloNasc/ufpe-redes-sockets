<p align="center">
  <img align="center" src='https://user-images.githubusercontent.com/54161035/200095500-d5fec4ba-c97e-4f19-9e39-6764418a736b.png' />
</p>
<p align="center">UNIVERSIDADE FEDERAL DE PERNAMBUCO-UFPE</p>
<p align="center">CENTRO DE INFORMÁTICA</p>

##

<p align="center">
  <img align="center" src='https://img.shields.io/badge/status-development-blue' />
  <img align="center" src='https://img.shields.io/badge/version-1.0-blue' />
  <img align="center" src='https://img.shields.io/badge/release%20date-setember/2023-blue' />
</p>

# Redes de computadores - Projeto de Sockets

## Estrutura de diretórios

```
.
├── apps
│   ├── dns
│   │   ├── consts.py
│   │   ├── __init__.py
│   │   └── server.py
│   ├── tcp
│   │   ├── client.py
│   │   ├── consts.py
│   │   ├── __init__.py
│   │   └── server.py
│   └── udp
│       ├── client.py
│       ├── consts.py
│       ├── __init__.py
│       └── server.py
├── dns_server.bat
├── dns_server.sh
├── README.md
├── setup.bat
├── setup.sh
├── tcp_client.bat
├── tcp_client.sh
├── tcp_server.bat
├── tcp_server.sh
├── udp_client.bat
├── udp_client.sh
├── udp_server.bat
└── udp_server.sh

```

- O diretório `apps/` contém os aplicativos DNS, TCP e UDP.
- `setup.bat` é um Batch Script para preparar uma venv para execução dos aplicativos.
- `setup.sh` é um script shell para preparar uma venv para execução dos aplicativos.
- `dns_server.bat`, `tcp_server.bat`, `tcp_client.bat`, `udp_server.bat` e `udp_client.bat` são Batch Script para executar os aplicativos correspondentes.
- `dns_server.sh`, `tcp_server.sh`, `tcp_client.sh`, `udp_server.sh` e `udp_client.sh` são scripts shell para executar os aplicativos correspondentes.

## Pré-requisitos

Antes de executar os aplicativos, certifique-se de ter o Python instalado em seu sistema.

## Executando os Aplicativos com os scripts preparados

Siga as etapas abaixo para executar cada aplicativo:

### Preparando uma venv (Opcional)

1. Abra um terminal no diretório raiz.

2. Execute o seguinte comando para criar um venv:
   
   No Windows

   ```bash
   ./setup.bat
   ```

   No Linux

   ```bash
   ./setup.sh
   ```

### Servidor DNS

1. Abra um terminal no diretório raiz.

2. Execute o seguinte comando para iniciar o servidor DNS:

   No Windows

   ```bash
   ./dns_server.bat
   ```

   No Linux

   ```bash
   ./dns_server.sh
   ```

### Servidor UDP

1. Abra um terminal no diretório raiz.

2. Execute o seguinte comando para iniciar o servidor UDP:
   
   No Windowns

   ```bash
   ./udp_server.bat
   ```
   No Linux

   ```bash
   ./udp_server.sh
   ```

### Cliente UDP

1. Abra um terminal no diretório raiz.

2. Execute o seguinte comando para iniciar o cliente UDP:

   No Windows

   ```bash
   ./udp_client.bat
   ```

   No Linux

   ```bash
   ./udp_client.sh
   ```

### Servidor TCP

1. Abra um terminal no diretório raiz.

2. Execute o seguinte comando para iniciar o servidor TCP:

   No Windows

   ```bash
   ./tcp_server.bat
   ```

   No Linux

   ```bash
   ./tcp_server.sh
   ```

### Cliente TCP

1. Abra um terminal no diretório raiz.

2. Execute o seguinte comando para iniciar o cliente TCP:

   No Windows

   ```bash
   ./tcp_client.bat
   ```

   No Linux

   ```bash
   ./tcp_client.sh
   ```

## Executando os Aplicativos manualmente

Siga as etapas abaixo para executar cada aplicativo:

### Preparando uma venv (Opcional)

1. Abra um terminal no diretório raiz.

2. Execute o seguinte comando para criar um venv:

    ```bash
    python -m venv venv
   
3. Execute o seguinte comando para ativar a venv:

    ```bash
    source venv/bin/activate

### Servidor DNS

1. Abra um terminal no diretório raiz.

2. Navegue até o diretóro `apps/dns`.

3. Execute o seguinte comando para iniciar o servidor DNS:

   ```bash
   python server.py

### Servidor UDP

1. Abra um terminal no diretório raiz.

2. Navegue até o diretóro `apps/udp`.

3. Execute o seguinte comando para iniciar o servidor UDP:

   ```bash
   python server.py

### Cliente UDP

1. Abra um terminal no diretório raiz.

2. Navegue até o diretóro `apps/udp`.

3. Execute o seguinte comando para iniciar o cliente UDP:

   ```bash
   python client.py

### Servidor TCP

1. Abra um terminal no diretório raiz.

2. Navegue até o diretóro `apps/tcp`.

3. Execute o seguinte comando para iniciar o servidor TCP:

   ```bash
   python server.py

### Cliente TCP

1. Abra um terminal no diretório raiz.

2. Navegue até o diretóro `apps/tcp`.

3. Execute o seguinte comando para iniciar o cliente TCP:

   ```bash
   python client.py

## Autores

| [<img src="https://avatars.githubusercontent.com/u/54161035?v=4" width=115><br><sub>Hítalo Nascimento</sub>](https://github.com/HitaloNasc) | [<img src="https://avatars.githubusercontent.com/u/100882928?v=4" width=115><br><sub>Ingrid Freire</sub>](https://github.com/ingridfsl) | 
| :--------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
