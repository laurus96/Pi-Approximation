import itertools as it
import sys
import signal
import math
import time


def signal_handler(sig, frame, pi_value=3.14):
    """This function ask if the user want to continue to approximate PI"""
    print('You pressed Ctrl+C')
    answer = str(input('Do you want to stop calculate Pi? [yes/no]'))
    
    if answer == 'no':
        return
    else:
        print(pi_value)
        sys.exit(0)

    #main 

if __name__ == '__main__':

    den = float(0.0)
    num = int(0)
    pi_app = float(0.0)
    

    for n in it.count():
        den = (2 * n) + 1
        num = (-1) ** n


        pi_app = pi_app + (num / den)
        print(pi_app*4)
        time.sleep(2)

        signal.signal(signal.SIGINT, signal_handler)


