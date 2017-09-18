# import RPi.GPIO as GPIO
import subprocess as sub


def main():
	#initialize GPIO pins
	# GPIO.setmode(GPIO.BOARD)

	path = sub.Popen(['ls','-a'],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	print(output)


if __name__ == "__main__":
	main()
