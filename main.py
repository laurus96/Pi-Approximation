import itertools as it
import sys
import signal
from time import sleep
from os import system, name

import PyQt5

pi = float(0.0)

def signal_handler(sig, frame):
    """This function ask if the user want to continue to approximate PI"""

    clear()
    print('You pressed Ctrl+C')
    answer = str(input('Do you want to stop calculate Pi? [yes/no]'))
    
    if answer == 'no':
        return
    else:
        print(pi)
        sys.exit(0)

def clear():
    """ This fuction clear the terminal (windows, macosx adn linux)"""
    
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#main 

if __name__ == '__main__':
    
    den = float(0.0)
    num = int(0)
    pi_app = float(0.0)
    

    for n in it.count():
        
        den = (2 * n) + 1
        num = (-1) ** n

        pi_app = pi_app + (num / den) #this calculate (pi/4)

        pi = pi_app * 4
        print(pi)
        sleep(0.5)
        clear()

        signal.signal(signal.SIGINT, signal_handler)


