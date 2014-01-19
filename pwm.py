#!/usr/bin/python

import sys, os, time
lib_path = os.path.abspath('.')
sys.path.append(lib_path)

from lights import GREEN, RED, YELLOW, BLUE, WHITE, on, off, toggle
from time import sleep

import RPi.GPIO as GPIO

def main():

  on(RED)

  p = GPIO.PWM(11, 50)
  p.start(0)

  for dc in range(0, 101, 1):
    p.ChangeDutyCycle(dc)
    sleep(0.05)

  p.ChangeDutyCycle(0)
  sleep(2)

  p.ChangeDutyCycle(100)

  p.stop()

if __name__ == "__main__":
  main()
