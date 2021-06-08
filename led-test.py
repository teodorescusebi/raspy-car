from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import time
import thread

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)

# GPIO.output(23,GPIO.HIGH)
# GPIO.output(23,GPIO.LOW)

connected = False

while not connected:
	try:
		gamepad = InputDevice('/dev/input/event7')
		connected = True
		print ("Controller detected")
	except Exception as e:
		print("Controller not detected")
		time.sleep(3)
	

isFliking = False

def rightBlinkerFunction():
	if GPIO.input(24) == 1:
		GPIO.output(24, GPIO.LOW)
		print("E aprins, l-am stins")
	else:
		GPIO.output(24, GPIO.HIGH)
		print("E stins, l-am aprins")

def rightFlicker():
	while isFliking:
		rightBlinkerFunction()
		print("pas1")
		time.sleep(0.5)
		rightBlinkerFunction()
		print("pas2")
		time.sleep(0.5)

for event in gamepad.read_loop():
	if event.type == 1: 
		if event.code == 310:
			if event.value == 1:
				if isFliking:
					isFliking = False
				else:
					isFliking = True
					thread.start_new_thread(rightFlicker, ())