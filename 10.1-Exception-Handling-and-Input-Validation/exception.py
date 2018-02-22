#!/bin/python

import time, sys

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCTRL + c was pressed.  Exiting...")
    sys.exit()


