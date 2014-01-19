#!/usr/bin/python

import sys, os
lib_path = os.path.abspath('.')
sys.path.append(lib_path)

from lights import GREEN, RED, YELLOW, BLUE, WHITE, on, off, toggle
from time import sleep

def main():

  on(RED)
  off(YELLOW)
  on(GREEN)
  off(BLUE)
  on(WHITE)

  while True:
    toggle(RED)
    toggle(YELLOW)
    toggle(GREEN)
    toggle(BLUE)
    toggle(WHITE)
    sleep(0.1)


if __name__ == "__main__":
  main()
