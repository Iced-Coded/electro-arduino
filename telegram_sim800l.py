import urequests
from sim800 import SIM800TCPIP


# Класс на те, аби надсилати повідомлення.
class SendMessage:
    def __init__(self, message, chat_id, mode):
        # Отримати токен можна тут: https://t.me/BotFather
        self.token = ""
        # Посилання на API телеграмму, яке ми й будемо використовувати у GET запиті
        self.tg_url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={message}"
        if mode == 0:
            response = urequests.get(self.tg_url)
            if response == 200 or 204 or "200" or "204":
                pass
            else:
                raise ConnectionError(f"Got '{response}' from api.telegram.bot")
        elif mode == 1:
            sim800 = SIM800TCPIP(uart_pin=1)
            sim800.http_init()
            sim800.http_set_param("URL", f"{self.tg_url}")
            response = sim800.http_get()
            if response == 200 or 204 or "200" or "204":
                sim800.http_terminate()
            else:
                raise ConnectionError(f"Got '{response}' from api.telegram.bot")
