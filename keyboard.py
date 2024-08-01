import RPi.GPIO as GPIO
import time

BUTTON_GPIO = 27  # Use um pino GPIO diferente para teste

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(BUTTON_GPIO) == GPIO.HIGH:
            print("Botão pressionado!")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa encerrado pelo usuário")
finally:
    GPIO.cleanup()