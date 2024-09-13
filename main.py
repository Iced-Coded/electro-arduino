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
        raise Exception("Мобільна мережа не знайдена.")

# Це все виконується аби отримати IP-адресу нашому GSM модулю.
def configurate_gsm(apn):
    print("Налаштовую зв'язок...")
    send_at_command('AT+SAPBR=3,1,"CONTYPE","GPRS"')
    send_at_command(f'AT+SAPBR=3,1,"APN","{apn}"')
    send_at_command('AT+SAPBR=1,1')
    response = send_at_command('AT+SAPBR=2,1')
    print(response)
