# Containerlab-Nornir-Arista

Este proyecto combina el uso de **Containerlab** y **Nornir** para implementar y automatizar un laboratorio de redes con **OSPF** utilizando dispositivos Arista.

## Directorio del proyecto

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



## Características

- Configuración automatizada de dispositivos de red con **Nornir**.
- Laboratorio simulado utilizando **Containerlab** para ejecutar dispositivos Arista.
- Configuración inicial de OSPF en múltiples routers.

## Requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Containerlab](https://containerlab.dev/)
- [Python 3.8+](https://www.python.org/)
- Librerías de Python:
  - `nornir`
  - `nornir_scrapli`
  - `scrapli`

## Instalación

1. **Clona el repositorio:**

   git clone https://github.com/lucaperyraluca/Containerlab-Nornir-Arista.git
   cd Containerlab-Nornir-Arista

2. **Configura el entorno de red:**

   Ejecuta el archivo arista-ospf.clab.yml con Containerlab:
   containerlab deploy -t Containerlab/Arista-OSPF/arista-ospf.clab.yml
   
