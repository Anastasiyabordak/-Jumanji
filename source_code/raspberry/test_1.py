import time

import argparse
import serial

item = serial.Serial()
item.baudrate = 9600   #115200
item.parity = serial.PARITY_NONE
item.bytesize = serial.EIGHTBITS
item.stopbits = 1
item.timeout = 5
item.port = '/dev/ttyACM0'
item.open()

LED_COUNT = 22  # Number of LED pixels.

stripes_collors = [1, 2, 3, 4]
shutdown_color = (0, 0, 0)

MAX_COUNT = 4
MIN_COUNT = 1

led_counters = [0, 0, 0, 0]

USERS = 0

DELAY = 0.08

def send(buf):
    global item
    if not item.is_open:
        item.open()
    print(buf)
    item.write(bytes(buf))


def switch_off_led(led_number):
    # try:
    #    for i in led_number:
    #        stripes[0][i] = shutdown_color
    # except TypeError:
    #    stripes[0][led_number] = shutdown_color
    ##stripe[led_number] = shutdown_color
    ##stripe.show()
    #item.open()
    send([led_number, led_number, 5])
    #item.close()


def switch(user, led_number, led_off):
    color = stripes_collors[user]
    send([led_off, led_number, color])
    
    
def switch_on_led(user, led_counter):
    color = stripes_collors[user]
    send([led_counter, led_counter, color])


def set_line_count(count):
    if count > MAX_COUNT or count < MIN_COUNT:
        raise Exception('value should be in [1, 4]')
    global USERS
    USERS = count
    
    
def win(user):
    color = stripes_collors[user]
    send([255, 129 + user, color])
    global item
    
    i = item.read()
    print('y: ', i)
    if i == b'':
        return False
    else:
        i = int(i)
        
    if chr(i) == '1':
        return True
    else:
        return False


def rainbow():
    for i in range(4):
        global led_counters
        led_counters = [0, 22, 44, 66]
        move_user(i, 1)


def set_default():
    for user in range(USERS):
        led_counters[user] = LED_COUNT * (user + 1) - 1


def switch_def_users():
    for user in range(USERS):
        switch_on_led(user, led_counters[user])


def move_user(line: int, offset: int):
    global led_counters
    if led_counters[line] < LED_COUNT * line:
        offset = 0

    led_counters[line] -= offset
    if led_counters[line] < LED_COUNT * line:
        #if win(line):
        #    set_default()
        #    return True
        #else:
        #    return False
        return True
    else:
        switch(line, led_counters[line] + offset, led_counters[line])
        return False


def start_test():
    try:
        while True:
            for user in range(USERS):
                if move_user(user, 1):
                    input()
                    end_of_game()
                    return
                time.sleep(1)
    except KeyboardInterrupt:
        pass
        #end_of_game()


def clear_stripe():
    send([255, 128, 255])


def init(test_mode=False):
    clear_stripe()
    global led_counters
    set_default()
    switch_def_users()
    if test_mode:
        start_test()


def end_of_game():
    clear_stripe()


def start_the_game(users: int, test_mode: bool):
    set_line_count(users)
    init(test_mode)


if __name__ == "__main__":
    start_the_game(MAX_COUNT, True)
