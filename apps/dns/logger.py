class Logger:
    def __init__(self, title: str):
        self.title = title.upper()
        self.green = "\033[92m"
        self.blue = "\033[93m"
        self.reset = "\033[0m"

    def log(self, message):
        print(f"{self.blue}[LOG]{self.reset} {self.title} - {message}")

    def info(self, message):
        print(f"{self.green}[INFO]{self.reset} {self.title} - {message}")
