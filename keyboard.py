import RPi.GPIO as GPIO
from pynput.keyboard import Controller
import time

# Configuração do GPIO
BUTTON_GPIO = 27  # Use o mesmo pino GPIO que funcionou antes

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Inicializa o controlador de teclado
keyboard = Controller()

try:
    print("Aguardando pressionamento do botão para simular a tecla 'p'...")
    button_pressed = False
    while True:
        if GPIO.input(BUTTON_GPIO) == GPIO.HIGH:
            if not button_pressed:
                print("Botão pressionado - Simulando tecla 'p'")
                keyboard.press('p')
                keyboard.release('p')
                button_pressed = True
        else:
            button_pressed = False
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa encerrado pelo usuário")
finally:
    GPIO.cleanup()
