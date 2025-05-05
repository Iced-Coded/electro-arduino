import machine
from machine import UART, Pin
import network
import time
from sim800 import SIM800

wlan = network.WLAN(network.STA_IF)


class ConnectToInternet:
    def __init__(self, mode, wifi_ssid="", wifi_password="", uart_pin=0, baud=0, roaming=True):
        if mode == 0:
            self.wifi(wifi_ssid, wifi_password)
        elif mode == 1:
            self.cellular(uart_pin, baud, roaming)
        else:
            raise ValueError(f"Відсутній режим підключення до інтернету.\nЯк тобі це тільки вдалося..?")

    def wifi(self, wifi_ssid, wifi_password):
        if wifi_ssid == "":
            raise ValueError("Перемінна wifi_ssid не може бути пустою!")
        else:
            wlan.active(True)
            wlan.connect({wifi_ssid}, {wifi_password})
            if wlan.isconnected() == True:
                wlan.active(False)
                return True
                #return ("Успішно під'єднався до Wi-Fi!")
            else:
                raise ConnectionError("Wi-Fi не був знайдений, або, модуль не працює.")

    def cellular(self, uart_pin, baud, roaming):
        sim800 = SIM800(uart_pin={uart_pin}, baud={baud})
        registration_response = sim800.send_command("AT+CGREG?")
        if registration_response == 1:
            return True
            #return ("Успішно під'єднався до стільникової мережі!")
        elif registration_response == 3 or 4 or 6 or 7:
            raise ConnectionRefusedError("Стільникова мережа або не доступна, або оператор відхилив ваш запит на реєстрацію.")
        elif registration_response == 5:
            if roaming == True:
                return True
                #return ("Успішно під'єднався до стільникової мережі!")
            elif roaming == False:
                raise ConnectionAbortedError("Модуль намагався підключитися до роумінгової мережі, але, така дія була заборонена користувачем.")
