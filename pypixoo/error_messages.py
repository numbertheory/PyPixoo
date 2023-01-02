from colorama import init, Fore, Back, Style


class errorPrint():
    def __init__(self):
        init()
        self.fores = {
            "black": Fore.BLACK,
            "red": Fore.RED,
            "green": Fore.GREEN,
            "yellow": Fore.YELLOW,
            "blue": Fore.BLUE,
            "magenta": Fore.MAGENTA,
            "cyan": Fore.CYAN,
            "white": Fore.WHITE
        }
        self.backs = {
           "black": Back.BLACK,
           "red": Back.RED,
           "green": Back.GREEN,
           "yellow": Back.YELLOW,
           "blue": Back.BLUE,
           "magenta": Back.MAGENTA,
           "cyan": Back.CYAN,
           "white": Back.WHITE
        }
        self.brightness = {
            "dim": Style.DIM,
            "normal": Style.NORMAL,
            "bright": Style.BRIGHT
        }

    def out(self, text_string, **kwargs):
        br = self.brightness.get(kwargs.get("br", "normal"))
        fg = self.fores.get(kwargs.get("fg", "white"))
        bg = self.backs.get(kwargs.get("bg", "black"))
        print(f"{br}{fg+bg}{text_string}{Style.RESET_ALL}")
