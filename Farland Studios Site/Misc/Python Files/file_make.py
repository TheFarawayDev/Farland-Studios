import enquiries
import os
import sys
import time
import clear
import random

def fragment():
    options = ['Confirm', 'Cancel']
    choice = enquiries.choose('Choose one of these options: ', options)
    if choice == 'Confirm':
        print('Confirmed')
        time.sleep(1)
        os.system('clear')
        time.sleep(1)
        os.system('clear')
        print('Fragmenting')
        time.sleep(1)
        os.system('clear')
        print('Fragmenting.')
        time.sleep(1)
        os.system('clear')
        print('Fragmenting..')
        time.sleep(1)
        os.system('clear')
        print('Fragmenting...')

fragment()