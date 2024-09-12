import machine
from machine import UART, Pin
import utelegram
import time

uart = UART(1, baudrate=9600, tx=17, rx=16)

# Гайд по APN:
# lifecell - internet
# Kyivstar - internet
# Vodafone UA - internet
apn = 'internet'
is_connected = False

def send_at_command(command, timeout=1000):
    uart.write(command + "\r\n")
    time.sleep_ms(timeout)
    response = uart.read()
    return response

def check_gsm():
    print("Перевіряю те, чи працює SIM800L")
    response = send_at_command('AT')

def check_network():
    print("Перевіряю\Під'єдную мобільну мережу")
    response = send_at_command('AT+CREG?')
    if response == 1 or 3:
        print(response)
    else:
        raise Exception("Мобільна мережа не знайдена.")

def configurate_gsm(apn):
    print("Налаштовую зв'язок...")
    send_at_command('AT+SAPBR=3,1,"CONTYPE","GPRS"')
    send_at_command(f'AT+SAPBR=3,1,"APN","{apn}"')
    send_at_command('AT+SAPBR=1,1')
    response = send_at_command('AT+SAPBR=2,1')
    print(response)

