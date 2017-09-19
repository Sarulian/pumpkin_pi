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
	start_button = 37
	GPIO.setmode(GPIO.BOARD)
	# outputs
	GPIO.setup(blue_led, GPIO.OUT)
	GPIO.setup(red_led, GPIO.OUT)
	GPIO.output(blue_led, 0)
	GPIO.output(red_led, 0)
	# inputs
	GPIO.setup(start_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	# main loop
	while True:
		if GPIO.input(start_button):

			# emmit shock sounds of random lengths with blue LED
			for i in range(r.randint(3,12)):
				total = 55
				length = r.randint(int(total/7),int(total/2))
				start = r.randint(0,total-length)
				turn_on(blue_led)
				sub.run(['mpg321','ESPARK1.mp3', '-k {}'.format(start), '-n {}'.format(start+length)])
				turn_off(blue_led)
				time.sleep(r.random()/3)
				i += 1

			# one last shock of max length
			turn_on(blue_led)
			sub.run(['mpg321','ESPARK1.mp3'])
			turn_off(blue_led)


			# play heartbeat sound with red led pulsing in beat
			play_sound = sub.Popen(['mpg321','heartbeat.mp3','-l 3'])
			freq = 200
			duty = 0
			brightening = True
			p = GPIO.PWM(red_led, freq)
			p.start(duty)
			while True:
				p.ChangeDutyCycle(duty)
				if brightening:
					duty += 1
				else:
					duty -= 1

				if duty == 100:
					brightening = False
				if duty == 0:
					brightening = True

				try:
					play_sound.wait(timeout=0.0045)
					break
				except sub.TimeoutExpired:
					continue

			# monster moan to finish it off
			turn_on(blue_led)
			p.ChangeDutyCycle(100)
			sub.run(['mpg321','monstermoan.mp3'])
			turn_off(blue_led)
			p.stop()



if __name__ == "__main__":
	main()
