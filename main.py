import RPi.GPIO as GPIO
import subprocess as sub
import time
import random as r


def turn_on(pin_number):
	GPIO.output(pin_number, 1)


def turn_off(pin_number):
	GPIO.output(pin_number, 0)


def main():
	#initialize GPIO pins
	blue_led = 33
	red_led = 32
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(blue_led, GPIO.OUT)
	GPIO.setup(red_led, GPIO.OUT)

	

	sub.run(['mpg321','Electric.mp3', '-k {}'.format(r.randint(0,100)), '-n {}'.format(r.randint(0,100))])


if __name__ == "__main__":
	main()
