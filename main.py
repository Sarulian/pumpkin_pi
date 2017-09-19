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
	GPIO.output(blue_led, 0)
	GPIO.output(red_led, 0)

	for i in range(r.randint(3,12)):
		total = 200
		length = r.randint(int(total/10),int(total/3))
		start = r.randint(0,total-length)
		turn_on(blue_led)
		sub.run(['mpg321','Electric.mp3', '-k {}'.format(start), '-n {}'.format(start+length)])
		turn_off(blue_led)
		time.sleep(r.random()/2)
		i += 1

	freq = 200
	duty = 0
	brightening = True
	p = GPIO.PWM(red_led, freq)
	sub.Popen(['mpg321','monstermoan.mp3'])
	p.start(duty)
	while True:
		p.ChangeDutyCycle(duty)
		if brightening:
			duty += 1
		else
			duty -= 1

		if duty == 100:
			brightening = False
		if duty == 0:
			brightening = True


if __name__ == "__main__":
	main()
