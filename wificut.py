'''
Author: www.github.com/JuanBindez
Description: destroy wifi
Python Version: 3.10
year: 2022
Local: Brazil
'''

import os
import time


def wifi_up():
    os.system("ifconfig wlp2s0 up")

def wifi_down():
    os.system("ifconfig wlp2s0 down")


while 1 < 2:
    wifi_down()
    time.sleep(5)
    wifi_up()
    time.sleep(5)


