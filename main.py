import gsm
import power
import telegram_sim800l as telegram
import _thread
from utime import sleep

# -- Налаштування --

# Ваша адреса, яка буде використана тільки для візуальних цілей.
address = "вул. Степана Бандери, 107"
# Айді чату (Або особистих повідомлень, або груповий чат)
# Можна отримати з-за допомоги цього бота: https://t.me/GetChatID_IL_BOT
chat_id = 0
# Конфігурація GSM модуля
# Пін на ESP32, куди підключений сам GSM модуль
gsm_uart_pin = 21
# Швидкість каналу даних
gsm_baud = 115200
# Назва мережі Wi-Fi
wifi_ssid = "Alexandro"
# Пароль мережі Wi-Fi
wifi_password = "qwerty123"
# Режим підключення до інтернету
# 0 = використовувати тільки Wi-Fi
# 1 = використовувати тільки стільникову мережу
mode = 0
# Дозвіл на підключення до роумінгової мережі.
# Це включає у себе "Національний Роумінг" так і звичайний, міжнаціональний роумінг
roaming = True
# Аналоговий порт куди під'єднаний модуль зарядки (TP4046), за стандартом, це GPIO0
charging_module_analogue_port = 0
# Токен Вашого боту.
token = ""

Messages = [
    f"🕯️ Електропостачання відсутнє по адресі '{address}'."
    f"💡 Електропостачання відновилося по адресі '{address}'."

]

# Тут код

is_ready = False
is_cellular = False
is_wifi = False
is_power_outage = False

connected = gsm.ConnectToInternet(mode, wifi_ssid, wifi_password, gsm_uart_pin, gsm_baud, roaming)
if connected:
    is_ready = True
    if mode == 0:
        is_wifi = True
    if mode == 1:
        is_cellular = True
else:
    raise OSError("Щось пішло не так. Зробіть Issue на GitHub сторінці.")

if is_ready == True:
    # ТИМЧАСОВО: Заготовка під підключення модуля живлення
    def check_power():
        power_status = power.CheckPower(charging_module_analogue_port)
        current_power = True # 1 = є, 2 = нема
        if power_status < 1 and current_power == True:
            current_power = False
            telegram.SendMessage(Messages[0], chat_id, mode, token)
        elif power_status > 1 and current_power != True:
            current_power = True
            telegram.SendMessge(Messages[1], chat_id, mode, token)
    while True:
        async check_power()
        sleep(10)
else:
    raise OSError("Щось пішло не так. Зробіть Issue на GitHub сторінці.")
