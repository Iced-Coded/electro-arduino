import machine
from machine import UART, Pin
import network
import time
from sim800 import SIM800

wlan = network.WLAN(network.STA_IF)

# Конфігурація GSM модуля
# Пін на ESP32, куди підключений сам GSM модуль
gsm_uart_pin = 1
# Швидкість каналу данних
gsm_baud = 115200
# Назва мережі Wi-Fi
wifi_ssid = "Alexandro"
# Пароль мережі Wi-Fi
wifi_password = "qwerty123"
# 0 = використовувати тільки Wi-Fi
# 1 = використовувати тільки стільникову мережу
# 2 = використовувати як Wi-Fi, так і стільникову мережу
mode = 0

# Конфігурація телеграмм
# Отримати токен можна тут: https://t.me/BotFather
bot_token = ""
# Айді чату (Або особистих повідомлень, або груповий чат)
# Можна отримати з-за допомоги цього бота: https://t.me/GetChatID_IL_BOT
chat_id = 0

is_connected_wifi = False
is_connected_cellular = False

if mode == 0 or 2:
    wlan.active(True)
    wlan.connect({wifi_ssid}, {wifi_password})
    if wlan.isconnected() == True:
        print("Успішно під'єднався до Wi-Fi!")
        wlan.active(False)
        is_connected_wifi = True
    else:
        print("Wi-Fi не знайдено або модуль не працює...")
elif mode == 1 or 2:
    # Ініціалізовуємо GSM-модуль
    sim800 = SIM800(uart_pin={gsm_uart_pin}, baud={gsm_baud})
    is_connected_cellular = True