import time, sys

## Funkcja zatrzymująca działanie programu
def stop(k):
    if k.upper()=='X':
        print('\nbye-bye\n')
        time.sleep(2)
        sys.exit()