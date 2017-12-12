# Following code is tested with Raspberry Pi 3
# Import the Libraries Required
import RPi.GPIO as GPIO
import time

SERVO_PIN = 32

def ang2duty (angle):
        DutyCycle = (angle/18)
        return DutyCycle

if __name__ == '__main__':
	# Setting the GPIO Mode to BOARD => Pin Count Mapping 
	GPIO.setmode(GPIO.BOARD)

	# Setting the GPIO Mode to BCM => GPIO Mapping 
	# Uncomment below line for to use GPIO number
	# GPIO.setmode(GPIO.BCM)

	# Setting the GPIO 18 as PWM Output 
	GPIO.setup(SERVO_PIN,GPIO.OUT)

	# Disable the warning from the GPIO Library
	GPIO.setwarnings(False)

	# Starting the PWM and setting the initial position of the servo with 50Hz frequency 
	servo = GPIO.PWM(SERVO_PIN,50)
	servo.start(0)
	while True:
		try:
			# Changing the Duty Cycle to rotate the motor 
			servo.ChangeDutyCycle(1)
			# Sleep for 5 Seconds 
			time.sleep(5)
                        # Changing the Duty Cycle to rotate the motor 
			servo.ChangeDutyCycle(3)
			# Sleep for 5 Seconds 
			time.sleep(5)
                        servo.ChangeDutyCycle(6)
			# Sleep for 5 Seconds 
			time.sleep(5)
                        servo.ChangeDutyCycle(9)
			# Sleep for 5 Seconds 
			time.sleep(5)
                        servo.ChangeDutyCycle(12)
			# Sleep for 5 Seconds 
			time.sleep(5)

		except KeyboardInterrupt:
			servo.stop()
			GPIO.cleanup()
# End of the Script
