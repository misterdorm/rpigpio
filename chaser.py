#!/usr/bin/python

import sys, os
lib_path = os.path.abspath('.')
sys.path.append(lib_path)

from lights import GREEN, RED, YELLOW, BLUE, WHITE, on, off
from time import sleep

def main():

  sleeptime = 0.05

  while True:
    off(WHITE)
    on(RED)
    sleep(sleeptime)

    off(RED)
    on(YELLOW)
    sleep(sleeptime)

    off(YELLOW)
    on(GREEN)
    sleep(sleeptime)

    off(GREEN)
    on(BLUE)
    sleep(sleeptime)

    off(BLUE)
    on(WHITE)
    sleep(sleeptime)


if __name__ == "__main__":
  main()
