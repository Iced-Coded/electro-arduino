import machine
from machine import UART, Pin
import network
import time
from sim800 import SIM800

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

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

is_connected_wifi = False
is_connected_cellular = False

if mode == 0 or 2:
    sta_if.active(True)
    sta_if.connect({wifi_ssid}, {wifi_password})
    if sta_if.isconnected() == True:
        print("Успішно під'єднався до Wi-Fi!")
        ap_if.active(False)
        is_connected_wifi = True
    else:
        print("Wi-Fi не знайдено або модуль не працює...")
elif mode == 1 or 2:
    # Ініціалізовуємо GSM-модуль
    sim800 = SIM800(uart_pin={gsm_uart_pin}, baud={gsm_baud})
    is_connected_cellular = True
