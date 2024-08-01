import RPi.GPIO as GPIO
from pynput.keyboard import Controller
import time

# Configuração do GPIO
BUTTON_GPIO = 27  # Use o mesmo pino GPIO que funcionou antes

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Inicializa o controlador de teclado
keyboard = Controller()

def button_callback(channel):
    print("Botão pressionado - Simulando tecla 'p'")
    keyboard.press('p')
    keyboard.release('p')

# Adiciona detecção de borda com a função de callback
GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, callback=button_callback, bouncetime=200)

try:
    print("Aguardando pressionamento do botão para simular a tecla 'p'...")
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa encerrado pelo usuário")
finally:
    GPIO.cleanup()