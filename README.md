# Containerlab-Nornir-Arista

This project combine **Containerlab** and **Nornir** to implement and automate an **OSPF** lab using Arista Devices. At same time, it have the possibility to use Nornir to check information (show commands) or modify the configuration. The combination of these tools are very powerful, with just two commands you can deploy all the lab and get all the OSPF information. Also, you can modify in "Script2.py" the commands that you want to use.
Notice that the Arista devices actually have a startup config, and is modificable inside  Containerlab/Arista-OSPF/r*/startup-config. Its mandatory mantain the ssh configurations for allow the Nornir connections. 

## Pyoect directory

```plaintext
.
├── Containerlab
│   └── Arista-OSPF
│       ├── arista-ospf.clab.yml
│       └── configs
│           ├── r1
│           │   └── startup-config
│           ├── r2
│           │   └── startup-config
│           ├── r3
│           │   └── startup-config
│           └── r4
│               └── startup-config
├── LICENSE
├── Nornir
│   ├── config.yaml
│   ├── groups.yaml
│   ├── hosts.yaml
│   ├── Nornir1.py
│   └── Nornir2.py
└── README.md



## Features

- Configuración automatizada de dispositivos de red con **Nornir**.
- Laboratorio simulado utilizando **Containerlab** para ejecutar dispositivos Arista.
- Configuración inicial de OSPF en múltiples routers.

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Containerlab](https://containerlab.dev/)
- [Python 3.8+](https://www.python.org/)
- Librerías de Python:
  - `nornir`
  - `nornir_scrapli`
  - `scrapli`

## Instalation

1. **Clone the repository:**

   git clone https://github.com/lucaperyraluca/Containerlab-Nornir-Arista.git
   cd Containerlab-Nornir-Arista

2. **Configure network enviroment:**

   Execute the file arista-ospf.clab.yml with Containerlab:
   containerlab deploy -t Containerlab/Arista-OSPF/arista-ospf.clab.yml
   
