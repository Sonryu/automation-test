from pyfirmata2 import Arduino, util
import time

#finir porta do arduino
porta = 'COM3'
board = Arduino(porta)

led_pinos = [2, 3, 4, 5]

for pino in led_pinos:
    board.digital[pino].mode = 1 #define como saida

print("Conectado ao Arduino")

while True:
    for pino in led_pinos:
        board.digital[pino].write(1) #liga o led
        time.sleep(1)
        board.digital[pino].write(0) #desliga o led