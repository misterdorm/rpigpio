#!/usr/bin/python

import sys, os
lib_path = os.path.abspath('.')
sys.path.append(lib_path)

from lights import GREEN, RED, YELLOW, BLUE, WHITE, on, off
from time import sleep

def main():

  while True:
    on(RED)
    sleep(0.2)
    on(YELLOW)
    sleep(0.1)
    on(GREEN)
    sleep(0.05)
    on(BLUE)
    sleep(0.025)
    on(WHITE)

    sleep(0.5)

    off(WHITE)
    sleep(0.025)
    off(BLUE)
    sleep(0.05)
    off(GREEN)
    sleep(0.1)
    off(YELLOW)
    sleep(0.2)
    off(RED)

    sleep(0.5)


if __name__ == "__main__":
  main()
