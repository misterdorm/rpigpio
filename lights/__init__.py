#!/usr/bin/python

import RPi.GPIO as GPIO

pins = {
	'RED':    16,
  'YELLOW': 18,
  'GREEN':  22,
  'BLUE':   11,
  'WHITE':  15,
}

GREEN="GREEN"
RED="RED"
YELLOW="YELLOW"
BLUE="BLUE"
WHITE="WHITE"

initd = False

def init():
  global initd
  GPIO.setmode(GPIO.BOARD)
  for color in pins:
    GPIO.setup(pins[color], GPIO.OUT)
  initd = True

def on(color):
  if not initd:
    init()
  GPIO.output(pins[color], GPIO.HIGH)

def off(color):
  if not initd:
    init()
  GPIO.output(pins[color], GPIO.LOW)

