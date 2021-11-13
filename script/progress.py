from time import sleep
import sys

unit = 20

for i in range(unit + 1):
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write("[%-20s] %d%%" % ('='*i, (100 / unit)*i))
    sys.stdout.flush()
    sleep(0.25)
