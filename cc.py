import pyfirmata

comport = "COM7"
board = pyfirmata.Arduino(comport)
led_1 = board.get_pin("d:7:0")
led_2 = board.get_pin("d:6:0")
led_3 - board.get_pin("d:5:0")
led_4 - board.get_pin("d:4:0")
led_5 - board.get_pin("d:3:0")


def led(total):
    if total == 0:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total == 1:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total == 2:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif total == 3:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif total == 4:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif total == 5:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
