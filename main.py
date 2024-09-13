import machine
from machine import UART, Pin
import utelegram
import time

# UART ми використовуємо аби комунікувати з GSM модулем, тобто,
# ми звертаємося до піна на нашій основній платі, аби передавати/отримувати
# данні від модуля на цьому піну.
uart = UART(1, baudrate=9600, tx=17, rx=16)

# Гайд по APN:
# lifecell - internet
# Kyivstar - internet
# Vodafone UA - internet
apn = 'internet'
is_connected = False

# Надіслати АТ команду
# https://microchip.ua/simcom/2G/SIM800%20Series_AT%20Command%20Manual_V1.12.pdf
def send_at_command(command, timeout=1000):
    uart.write(command + "\r\n")
    time.sleep_ms(timeout)
    response = uart.read()
    return response

# Перевірка на те, чи активний GSM-модуль.
def check_gsm():
    print("Перевіряю те, чи працює SIM800L")
    response = send_at_command('AT')


# Перевірка наявності мобільної мережі
# Якщо надсилають "1", то мережа успішно знайдена, якщо "3",
# то знайдена мережа у роумінгу.
# Інші записи - це або відсутність або заборона підключення до мережі.
def check_network():
    print("Перевіряю наявність мобільної мережі")
    response = send_at_command('AT+CREG?')
    if response == 1 or 3:
        print(response)
    else:
        print("Wi-Fi не знайдено або модуль не працює...")
elif mode == 1 or 2:
    # Ініціалізовуємо GSM-модуль
    sim800 = SIM800(uart_pin={gsm_uart_pin}, baud={gsm_baud})
    is_connected_cellular = True

