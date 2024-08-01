import RPi.GPIO as GPIO
from pynput.keyboard import Controller, Key
import time

# Configuração do GPIO
BUTTON_GPIO = 17  # Substitua este número pelo GPIO que você está usando

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Inicializa o controlador de teclado
keyboard = Controller()

def button_callback(channel):
    # Simula a tecla "p"
    keyboard.press('p')
    keyboard.release('p')
    print("Tecla 'p' pressionada")

# Configura o evento de detecção de borda no botão
GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, callback=button_callback, bouncetime=200)

try:
    print("Aguardando pressionamento do botão...")
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programa encerrado pelo usuário")

finally:
    GPIO.cleanup()
