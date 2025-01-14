from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

#nr = InitNornir(config_file="config.yaml")

def main():
    # Inicializa Nornir con la configuración
    nr = InitNornir(config_file="config.yaml")
    
    # Ejecuta un comando en todos los dispositivos usando Scrapli
    result = nr.run(task=send_command, command="show version")
    
    # Imprime los resultados
    print_result(result)

if __name__ == "__main__":
    main()
