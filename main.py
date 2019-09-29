import itertools as it
import sys
import signal
import math

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

    for x in it.count():
        print(x)
        
        signal.signal(signal.SIGINT, signal_handler)


