import RPi.GPIO as GPIO
import time

# Configuração do GPIO
BUTTON_GPIO = 27  # Escolha um pino GPIO disponível

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Aguardando pressionamento do botão...")

try:
    while True:
        # Verifique o estado do botão
        if GPIO.input(BUTTON_GPIO) == GPIO.HIGH:
            print("Botão pressionado!")
            # Aguarde enquanto o botão estiver pressionado
            while GPIO.input(BUTTON_GPIO) == GPIO.HIGH:
                time.sleep(0.1)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa encerrado pelo usuário")
finally:
    GPIO.cleanup()