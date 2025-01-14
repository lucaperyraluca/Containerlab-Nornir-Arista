from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

#nr = InitNornir(config_file="config.yaml")

def main():
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=send_command, command="show version")
    print_result(result)

if __name__ == "__main__":
    main()
