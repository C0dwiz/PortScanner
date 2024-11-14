import socket
from colorama import Fore, Style, init
import argparse

init(autoreset=True)


class PortScanner:
    def __init__(self, host: str, start_port: int, end_port: int):
        self.host = host
        self.start_port = start_port
        self.end_port = end_port

    def scan_ports(self):
        print(
            f"\n{Fore.CYAN}Сканирование портов {self.start_port}-{self.end_port} на хосте {self.host}...{Style.RESET_ALL}"
        )
        open_ports = []

        for port in range(self.start_port, self.end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((self.host, port))
                if result == 0:
                    print(f"{Fore.GREEN}[+] Порт {port} открыт{Style.RESET_ALL}")
                    open_ports.append(port)
                else:
                    print(f"{Fore.RED}[-] Порт {port} закрыт{Style.RESET_ALL}")

        print(
            f"\n{Fore.YELLOW}Сканирование завершено. Открытые порты: {open_ports}{Style.RESET_ALL}"
        )


def main():
    parser = argparse.ArgumentParser(description="Сканер открытых портов")
    parser.add_argument("host", type=str, help="Хост для сканирования")
    parser.add_argument("start_port", type=int, help="Начальный порт для сканирования")
    parser.add_argument("end_port", type=int, help="Конечный порт для сканирования")

    args = parser.parse_args()

    scanner = PortScanner(args.host, args.start_port, args.end_port)
    scanner.scan_ports()


if __name__ == "__main__":
    main()
