from datetime import datetime

class Logger:
    def __init__(self, filename="app.log"):
        self.filename = filename

    def log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        with open(self.filename, "a") as f:
            f.write(log_entry)
        print(log_entry.strip())

if __name__ == "__main__":
    logger = Logger()
    logger.log("Application started")