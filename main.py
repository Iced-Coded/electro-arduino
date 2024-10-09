import gsm
import power
import telegram_sim800l
import _thread

# -- Налаштування --

# Ваша адреса, яка буде використана тільки для візуальних цілей.
address = "вул. Степана Бандери, 107"
# Айді чату (Або особистих повідомлень, або груповий чат)
# Можна отримати з-за допомоги цього бота: https://t.me/GetChatID_IL_BOT
chat_id = 0
# Конфігурація GSM модуля
# Пін на ESP32, куди підключений сам GSM модуль
gsm_uart_pin = 21
# Швидкість каналу данних
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

Messages = [
    "🕯️ Світло відсутнє"
]

# Тут код

is_ready = False
is_cellular = False
is_wifi = False

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
    def light_check():
        pass
else:
    raise OSError("Щось пішло не так. Зробіть Issue на GitHub сторінці.")