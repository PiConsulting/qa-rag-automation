from components.send import send_requests
from components.config import URL, INPUT_FILE_PATH

if __name__ == "__main__":
    send_requests(INPUT_FILE_PATH, URL)


