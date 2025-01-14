# Containerlab-Nornir-Arista

This project combine **Containerlab** and **Nornir** to implement and automate an **OSPF** lab using Arista Devices. At same time, it have the possibility to use Nornir to check information (show commands) or modify the configuration. The combination of these tools are very powerful, with just two commands you can deploy all the lab and get all the OSPF information. Also, you can modify in "Script2.py" the commands that you want to use.
Notice that the Arista devices actually have a startup config, and is modificable inside  Containerlab/Arista-OSPF/r*/startup-config. Its mandatory mantain the ssh configurations for allow the Nornir connections. 

## Proyect directory

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

```

## Features

- Configuración automatizada de dispositivos de red con **Nornir**.
- Laboratorio simulado utilizando **Containerlab** para ejecutar dispositivos Arista.
- Configuración inicial de OSPF en múltiples routers.

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Containerlab](https://containerlab.dev/)
- [Python 3.8+](https://www.python.org/)
- Python libraries:
  - `nornir`
  - `nornir_scrapli`
  - `scrapli`
  - An image of Arista downloaded from it page: Arista requires its users to register with arista.com before downloading any images. Once you created an account and logged in,
    go to the software downloads section and download ceos64 tar archive for a given release.
    Once downloaded, import the archive with docker:
    **import container image and save it under ceos:4.32.0F name**
        docker import cEOS64-lab-4.32.0F.tar.xz ceos:4.32.0F

## Instalation

1. **Clone the repository:**

   git clone https://github.com/lucaperyraluca/Containerlab-Nornir-Arista.git
   cd Containerlab-Nornir-Arista

2. **Configure network enviroment:**

   Execute the file arista-ospf.clab.yml with Containerlab:
   containerlab deploy -t Containerlab/Arista-OSPF/arista-ospf.clab.yml

3. **Execute Nornir to check devices:**

   You need to modify the file "hosts.yaml" and replace the IP for the correct ones. The IP od each device were assigned by Containerlab automatically, and are showed after execute 
   "containerlab deploy -t Containerlab/Arista-OSPF/arista-ospf.clab.yml".
   After modify these parameters (ips), ypu can modify the command or commands to check information. As default, is charged on "Nornir2.py" the follow commands:
   commands = ["show ip ospf nei", "show ip ospf interface brief", "show ip route"] but can be replaced for wherever you want.
