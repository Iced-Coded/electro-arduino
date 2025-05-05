from machine import Pin, ADC


class CheckPower:
    def __init__(self, charging_module_GPIO):
        self.GPIO = ADC(Pin(charging_module_GPIO))
        self.GPIO.atten(ADC.ATTN_11DB)
        CheckPower.status(self.GPIO)

    def status(self, GPIO):
        return GPIO.read()
