import RPi.GPIO as GPIO
import subprocess as sub
import time


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

	

	p = sub.Popen(['mpg321','monstermoan.mp3'])
	time.sleep(2)
	p.kill()


if __name__ == "__main__":
	main()
