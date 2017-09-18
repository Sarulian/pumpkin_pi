import RPi.GPIO as GPIO
import subprocess as sub
import time


def light_LED(pin_number, time, brightness):
	print("Do stuff")


def main():
	#initialize GPIO pins
	blue_led = 33
	red_led = 32
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(blue_led, GPIO.OUT)
	GPIO.setup(red_led, GPIO.OUT)

	time.sleep(1)

	while(True):
		print("Blue on.")
		GPIO.output(blue_led, 1)
		GPIO.output(red_led, 0)

		time.sleep(2)

		print("Red on.")
		GPIO.output(blue_led, 0)
		GPIO.output(red_led, 1)

		time.sleep(1)

	# sub.run(['mpg321','monstermoan.mp3'])


if __name__ == "__main__":
	main()
