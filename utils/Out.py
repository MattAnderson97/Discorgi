from colorama import init, Fore
init(autoreset=True)


class Out:
    @staticmethod
    def error(message):
        print(Fore.LIGHTRED_EX + "[ERROR] " + message)

    @staticmethod
    def info(message):
        print("[INFO] " + message)
