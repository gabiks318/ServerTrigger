import requests
import logging


class ServerTrigger:

    def __init__(self):
        file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

        file_handler = logging.FileHandler('main.log')
        file_handler.setLevel(logging.INFO)

        self.logger = logging.getLogger("Server Trigger")

        file_handler.setFormatter(file_format)
        file_handler.setLevel(logging.INFO)
        self.logger.addHandler(file_handler)

        self.logger.setLevel(logging.INFO)

    def trigger_url(self, url: str, name: str) -> int:
        try:
            res = requests.post(url=url)
        except Exception as e:
            self.logger.info(f"ERROR - {name} - {url} - {repr(e)}")
            return -1
        if res.status_code == 200:
            self.logger.info(f"{name} - {url}")
        else:
            self.logger.error(f"ERROR - {name} - {url} - {repr(res.content.decode())}")
        return res.status_code
